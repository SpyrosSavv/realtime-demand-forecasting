from kedro.pipeline import Pipeline, node
from .nodes import make_target

def create_training_pipeline() -> Pipeline:
    return Pipeline([
        node(
            func=make_target,
            inputs=["features", "params:training.target_params"],
            outputs="data_with_target"
        )
    ])