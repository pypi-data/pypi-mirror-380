import numpy as np
import pandas as pd


class StratifiedSampler:
    def __init__(self, df: pd.DataFrame, strat_columns: list):
        self.df = df
        self.strat_columns = strat_columns
        self.weights = self.compute_strata_weights()

    def compute_strata_weights(self):
        strata_counts = self.df.groupby(self.strat_columns).size()
        total = len(self.df)
        weights = {key: count / total for key, count in strata_counts.items()}
        return weights

    def sample(self, group_size: int, weights: dict = None, random_state: int = 42):
        np.random.seed(random_state)
        if weights is None:
            weights = self.weights

        stats = self.df.groupby(self.strat_columns)
        sub_list = []
        for key, idx in stats.groups.items():
            strats_df = self.df.loc[idx]
            weight = weights[key]
            per_group = min(round(group_size * weight), len(strats_df))

            chosen_idx = np.random.choice(strats_df.index, per_group, replace=False)
            sub_list.append(strats_df.loc[chosen_idx])

        sub_df = pd.concat(sub_list)
        return sub_df
