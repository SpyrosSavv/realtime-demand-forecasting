from kedro.pipeline import Pipeline, node
from .nodes import make_target, split_data

def create_training_pipeline() -> Pipeline:
    return Pipeline([
        node(
            func=make_target,
            inputs=["features", "params:training.target_params"],
            outputs="data_with_target"
        ),
        node(
            func=split_data,
            inputs=["data_with_target","params:training"],
            outputs=["x_train", "x_test", "y_train", "y_test"],
        )
    ])