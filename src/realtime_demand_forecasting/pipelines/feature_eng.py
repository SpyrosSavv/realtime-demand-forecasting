from kedro.pipeline import Pipeline, node
from .nodes import rename_columns

def create_feature_eng_pipeline() -> Pipeline:
    return Pipeline(
        [
            node(
                func=rename_columns,
                inputs=["train_data", "params:feature_engineering.rename_columns"],
                outputs="renamed_data"
            )
        ]
    )