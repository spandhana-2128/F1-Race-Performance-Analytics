import pandas as pd

def basic_driver_summary(df: pd.DataFrame) -> pd.DataFrame:
    # Update column names after we inspect the selected F1 dataset.
    required = {"driver", "position"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return (
        df.groupby("driver", as_index=False)
          .agg(
              races=("position", "count"),
              avg_finish=("position", "mean"),
          )
          .sort_values("avg_finish")
    )
