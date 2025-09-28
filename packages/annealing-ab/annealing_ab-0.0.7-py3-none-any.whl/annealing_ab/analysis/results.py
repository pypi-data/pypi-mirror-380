from typing import List, Type

import numpy as np
import pandas as pd

from annealing_ab.loss.losses import BaseLoss


class MultiCriteriaEvaluator:
    """
    Evaluate multiple statistical loss criteria on a pair of datasets.

    Parameters
    ----------
    df1 : pd.DataFrame
        First dataset (subset population).
    df2 : pd.DataFrame
        Second dataset (target population).
    columns : list of str, optional
        List of feature columns to evaluate. If empty, use all columns except fk_key.
    fk_key : str
        Column name to exclude from features (e.g., user_id).
    loss_classes : list of Type[BaseLoss]
        List of loss classes to evaluate.
    """

    def __init__(
        self,
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        ignore_cols: List[str],
        loss_classes: List[Type[BaseLoss]],
        columns: List[str] | None = None,
    ):
        self.df1 = df1.copy()
        self.df2 = df2.copy()

        if not columns:
            self.columns = [col for col in df1.columns if col not in ignore_cols]
        else:
            self.columns = columns

        self.loss_classes = loss_classes

    def evaluate(self) -> pd.DataFrame:
        """
        Compute statistics for all features and all loss criteria.

        Returns
        -------
        pd.DataFrame
            DataFrame where the first column is 'feature', and the remaining
            columns correspond to loss criteria names with their computed values.
        """
        results = []

        for col in self.columns:
            row = {"feature_name": col}

            X = np.array(self.df1[[col]], dtype=float)
            Y = np.array(self.df2[[col]], dtype=float)

            for loss_cls in self.loss_classes:
                loss_instance = loss_cls(X=X, Y=Y)
                loss_name = getattr(loss_instance, "criteria_name", loss_cls.__name__)
                row[loss_name] = loss_instance.calculate_p_value()

            results.append(row)

        return pd.DataFrame(results)
