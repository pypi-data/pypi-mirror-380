import copy
from typing import List, Optional, Tuple, Type

import numpy as np
import pandas as pd

from annealing_ab.analysis.charts import FeatureDistributionVisualizer, LossVisualizer
from annealing_ab.analysis.results import MultiCriteriaEvaluator
from annealing_ab.loss.losses import BaseLoss, KSLoss, LeveneLoss, TTestLoss
from annealing_ab.stratify.stratify_group import StratifiedSampler


class StratAnnealingAB:
    """
    Simulated Annealing algorithm for A/B testing population selection.

    This class implements a simulated annealing optimization algorithm to find
    a subset of the general population that best matches the target population
    based on statistical criteria.

    Parameters
    ----------
    general_population : pd.DataFrame
        The full population from which to select a subset.
    target_population : pd.DataFrame
        The target population to match against. It is taken from the
        general population and at the same time
        the general population does not contain the target.
        The target group can be the general population, when we want to select
        a test and control group from the general one at once, so that they
        describe the general population.
    strat_col: List[str]
        The list of columns to be stratified by.
    class_loss : Type[BaseLoss]
        Class that calculates how well the subset matches the target.
    fk_key : str
        Column name that serves as the foreign key identifier.
    n_sub : int
        Number of samples to select from the general population.
    temperature : float, optional
        Initial temperature for the annealing process, by default 100.0.
    cooling_rate : float, optional
        Rate at which temperature decreases, by default 0.95.
    min_temperature : float, optional
        Minimum temperature threshold, by default 1e-3.
    max_iterations : int, optional
        Maximum number of iterations to run, by default 1000.
    random_state : int or None, optional
        Random seed for reproducible results, by default None.
    early_stop_k : int, optional
        Number of recent iterations to check for early stopping, by default 50.
    early_stop_eps : float, optional
        Minimum improvement threshold for early stopping, by default 1e-4.

    Attributes
    ----------
    temperature : float
        Current temperature of the annealing process.
    cooling_rate : float
        Rate at which temperature decreases.
    min_temperature : float
        Minimum temperature threshold.
    max_iterations : int
        Maximum number of iterations to run.
    random_state : np.random.RandomState
        Random number generator for reproducible results.
    history_loss : list[float]
        History of loss values during optimization.
    early_stop_k : int
        Number of recent iterations to check for early stopping.
    early_stop_eps : float
        Minimum improvement threshold for early stopping.
    fk_key : str
        Column name that serves as the foreign key identifier.
    general_population : pd.DataFrame
        The full population from which to select a subset.
    target_population : pd.DataFrame
        The target population to match against.
    class_loss : Type[BaseLoss]
        Class for calculating match quality.
    n_sub : int
        Number of samples to select from the general population.
    best_subset: pd.DataFrame | None
        selected subset
    """

    def __init__(
        self,
        general_population: pd.DataFrame,
        target_population: pd.DataFrame,
        strat_col: List[str],
        class_loss: Type[BaseLoss],
        fk_key: str,
        n_sub: int,
        temperature: float = 100.0,
        cooling_rate: float = 0.95,
        min_temperature: float = 1e-3,
        max_iterations: int = 1000,
        random_state: Optional[int] = None,
        early_stop_k: int = 50,
        early_stop_eps: float = 1e-4,
    ) -> None:
        self.strat_col = strat_col
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.min_temperature = min_temperature
        self.max_iterations = max_iterations
        self.random_state = np.random.RandomState(random_state)

        self.history_loss = []

        self.early_stop_k = early_stop_k
        self.early_stop_eps = early_stop_eps

        self.fk_key = fk_key

        self.general_population = general_population
        self.target_population = target_population
        self._order_cols()

        self.eval_loss_classes = class_loss
        self.test_stats_criteria = None

        self.n_sub = n_sub

        self.best_subset = None

    def _acceptance_probability(self, old_loss: float, new_loss: float) -> float:
        """
        Calculate the probability of accepting a new solution.

        In simulated annealing, worse solutions can be accepted with a probability
        that decreases as temperature decreases. This helps escape local optima.

        Parameters
        ----------
        old_loss : float
            Loss value of the current solution.
        new_loss : float
            Loss value of the proposed new solution.

        Returns
        -------
        float
            Probability between 0 and 1 of accepting the new solution.
        """
        if new_loss < old_loss:
            return 1.0
        return np.exp((old_loss - new_loss) / self.temperature)

    def _cool_down(self) -> None:
        """
        Reduce the temperature according to the cooling rate.

        Temperature is gradually reduced to make the algorithm more selective
        over time, eventually only accepting better solutions.

        Returns
        -------
        None
        """
        if self.temperature > self.min_temperature:
            self.temperature *= self.cooling_rate
            if self.temperature < self.min_temperature:
                self.temperature = self.min_temperature

    def _early_stop(self) -> bool:
        """
        Check if the algorithm should stop early due to lack of improvement.

        The algorithm stops early if the loss values in the recent window
        have not improved by more than the threshold.

        Returns
        -------
        bool
            True if the algorithm should stop early, False otherwise.
        """
        if len(self.history_loss) > self.early_stop_k:
            window = self.history_loss[-self.early_stop_k :]
            return max(window) - min(window) < self.early_stop_eps
        return False

    def _init_strata_mappings(self, X, Y, strat_col_idxs, sep="_"):
        """
        Initialize strata mappings for fast neighbor selection.

        This method creates index mappings of strata to their positions
        in both subsets. It also identifies shared strata between the two
        populations.

        Parameters
        ----------
        X : np.ndarray
            Subset of selected units.
        Y : np.ndarray
            Remaining units outside the subset.
        strat_col_idxs : list[int]
            Column indices that define stratification.
        sep : str, optional
            Separator used to join column values, by default "_".

        Returns
        -------
        None
        """
        strata_X = np.array([sep.join(map(str, row[strat_col_idxs])) for row in X])
        strata_Y = np.array([sep.join(map(str, row[strat_col_idxs])) for row in Y])

        idx_by_strata_X = {}
        idx_by_strata_Y = {}

        for i, s in enumerate(strata_X):
            idx_by_strata_X.setdefault(s, []).append(i)
        for i, s in enumerate(strata_Y):
            idx_by_strata_Y.setdefault(s, []).append(i)

        shared_strata = set(idx_by_strata_X.keys()) & set(idx_by_strata_Y.keys())
        shared_strata = {s for s in shared_strata if idx_by_strata_X[s] and idx_by_strata_Y[s]}

        self._strata_X = strata_X
        self._strata_Y = strata_Y
        self._idx_by_strata_X = idx_by_strata_X
        self._idx_by_strata_Y = idx_by_strata_Y
        self._shared_strata = shared_strata
        self._strat_col_idxs_cached = strat_col_idxs
        self._sep_cached = sep

    def _propose_swap(self):
        """
        Propose a swap between subset and remainder.

        Randomly selects one element from both populations that belong
        to the same stratum.

        Returns
        -------
        tuple of int
            Index in subset, index in remainder.

        Raises
        ------
        ValueError
            If no common strata exist between the two populations.
        """
        if not self._shared_strata:
            raise ValueError("There are no common strata to share.")
        chosen_strata = self.random_state.choice(list(self._shared_strata))
        list_X = self._idx_by_strata_X[chosen_strata]
        list_Y = self._idx_by_strata_Y[chosen_strata]
        ind_X = int(self.random_state.choice(list_X))
        ind_Y = int(self.random_state.choice(list_Y))
        return ind_X, ind_Y

    def _apply_swap(self, X, Y, ind_X, ind_Y):
        """
        Apply swap and update strata mappings.

        The method swaps one element from the subset with one element
        from the remainder and updates all strata-related mappings.

        Parameters
        ----------
        X : np.ndarray
            Subset array.
        Y : np.ndarray
            Remainder array.
        ind_X : int
            Index in subset.
        ind_Y : int
            Index in remainder.

        Returns
        -------
        tuple of np.ndarray
            Old value from subset and new value from remainder.
        """
        old_val = np.copy(X[ind_X])
        new_val = np.copy(Y[ind_Y])
        X[ind_X], Y[ind_Y] = new_val, old_val
        sep = self._sep_cached
        sX = sep.join(map(str, X[ind_X][self._strat_col_idxs_cached]))
        sY = sep.join(map(str, Y[ind_Y][self._strat_col_idxs_cached]))

        old_strata_X = self._strata_X[ind_X]
        old_strata_Y = self._strata_Y[ind_Y]

        self._strata_X[ind_X] = sX
        self._strata_Y[ind_Y] = sY

        lst = self._idx_by_strata_X[old_strata_X]
        lst.remove(ind_X)
        self._idx_by_strata_X.setdefault(sX, []).append(ind_X)

        lst = self._idx_by_strata_Y[old_strata_Y]
        lst.remove(ind_Y)
        self._idx_by_strata_Y.setdefault(sY, []).append(ind_Y)

        if not self._idx_by_strata_X.get(old_strata_X):
            self._shared_strata.discard(old_strata_X)
        if not self._idx_by_strata_Y.get(old_strata_Y):
            self._shared_strata.discard(old_strata_Y)
        if sX in self._idx_by_strata_Y and self._idx_by_strata_Y[sX]:
            self._shared_strata.add(sX)
        if sY in self._idx_by_strata_X and self._idx_by_strata_X[sY]:
            self._shared_strata.add(sY)

        return old_val, new_val

    def _initial_state(
        self, general_population: pd.DataFrame
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Generate an initial subset and remainder.

        A stratified sample is drawn from the general population.
        The remainder is the general population without this subset.

        Parameters
        ----------
        general_population : pd.DataFrame
            Original dataset.

        Returns
        -------
        tuple of pd.DataFrame
            Subset and remainder DataFrames.
        """
        sampler = StratifiedSampler(general_population, self.strat_col)
        subset = sampler.sample(group_size=self.n_sub)

        general_without_subset = general_population.drop(subset.index)
        return subset, general_without_subset

    def _order_cols(self) -> None:
        """
        Reorder DataFrame columns.

        Moves the foreign key to the first position, followed by stratification
        columns, then all other features.

        Returns
        -------
        None
        """

        def move_fk_key_first(df: pd.DataFrame, key: str, strat_cols: List[str]) -> pd.DataFrame:
            remaining_cols = [c for c in df.columns if c != key and c not in strat_cols]
            new_order = [key] + strat_cols + remaining_cols
            return df[new_order]

        self.general_population = move_fk_key_first(
            self.general_population, self.fk_key, self.strat_col
        )
        self.target_population = move_fk_key_first(
            self.target_population, self.fk_key, self.strat_col
        )

    def loss_chart(self):
        """
        Visualize the loss history over iterations.

        Parameters
        ----------
        None

        Returns
        -------
        None
            The function displays the plot but does not return any value.
        """
        loss_visual = LossVisualizer(self.history_loss)
        loss_visual.plot()

    def distribution_chart(self, plot_type: str):
        """
        Visualize the feature distributions for the subset and target datasets.

        Parameters
        ----------
        plot_type : str
            Type of plot to generate.
            (e.g., 'hist', 'kde').

        Returns
        -------
        None
            The function displays the plots but does not return any value.
        """
        visual = FeatureDistributionVisualizer(
            df1=self.best_subset,
            df2=self.target_population,
            ignore_cols=[self.fk_key] + self.strat_col,
            plot_type=plot_type,
            dataset1_name="subset",
            dataset2_name="target",
        )
        visual.plot_distributions()

    def criteria_p_value_report(
        self, loss_classes: List[Type[BaseLoss]] = [TTestLoss, KSLoss, LeveneLoss]
    ) -> pd.DataFrame:
        """
        Generate a report of statistics for multiple loss criteria.

        Parameters
        ----------
        loss_classes : list of Type[BaseLoss], optional
            List of loss classes to evaluate. Defaults to [TTestLoss, KSLoss, LeveneLoss].

        Returns
        -------
        pd.DataFrame
            DataFrame with feature names in the first column and
            p_value for each loss criterion in the subsequent columns.
        """
        eval_criteria = MultiCriteriaEvaluator(
            df1=self.best_subset,
            df2=self.target_population,
            ignore_cols=[self.fk_key] + self.strat_col,
            loss_classes=loss_classes,
        )
        return eval_criteria.evaluate()

    def _np_float(self, array: np.ndarray):
        """
        Convert array to float type.
        Makes a copy of the array and casts it to float.

        Parameters
        ----------
        array : np.ndarray
            Input array.

        Returns
        -------
        np.ndarray
            Array with dtype=float.
        """
        array = np.copy(array)
        return np.array(array, dtype=float)

    def run(self) -> np.ndarray:
        """
        Run simulated annealing to select subset.

        Iteratively swaps units between subset and remainder while
        optimizing the statistical similarity to the target population.

        Returns
        -------
        pd.DataFrame
            The best subset found.
        """

        f = len(self.strat_col) + 1
        subset, general_without_subset = self._initial_state(self.general_population)

        subset = subset.copy().to_numpy()
        general_without_subset = general_without_subset.copy().to_numpy()
        target_np = self.target_population.copy().to_numpy()

        self.test_stats_criteria = self.eval_loss_classes(
            X=self._np_float(subset[:, f:]), Y=self._np_float(target_np[:, f:])
        )
        current_loss = self.test_stats_criteria.calculate_loss()

        self._init_strata_mappings(
            subset,
            general_without_subset,
            strat_col_idxs=[i for i in range(1, len(self.strat_col) + 1)],
            sep="_",
        )

        for _ in range(self.max_iterations):
            ind_X, ind_Y = self._propose_swap()

            old_val = subset[ind_X].copy()
            new_val = general_without_subset[ind_Y].copy()

            subset[ind_X], general_without_subset[ind_Y] = new_val, old_val

            temp_test_criteria = copy.deepcopy(self.test_stats_criteria)
            temp_test_criteria.update(
                new_val=self._np_float(new_val[f:]),
                old_val=self._np_float(old_val[f:]),
                X=self._np_float(subset[:, f:]),
            )
            new_loss = temp_test_criteria.calculate_loss()

            subset[ind_X], general_without_subset[ind_Y] = old_val, new_val
            if self.random_state.rand() < self._acceptance_probability(current_loss, new_loss):
                old_val_applied, new_val_applied = self._apply_swap(
                    subset, general_without_subset, ind_X, ind_Y
                )
                current_loss = new_loss
                self.test_stats_criteria.update(
                    new_val=self._np_float(new_val_applied[f:]),
                    old_val=self._np_float(old_val_applied[f:]),
                    X=self._np_float(subset[:, f:]),
                )
                self.history_loss.append(current_loss)

            self._cool_down()
            if self._early_stop():
                break

        subset_df = pd.DataFrame(subset, columns=self.target_population.columns)
        self.best_subset = subset_df
        return subset_df
