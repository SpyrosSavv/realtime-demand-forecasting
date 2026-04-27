from .pipelines.feature_eng import create_feature_eng_pipeline
from kedro.pipeline import Pipeline

def register_pipelines() -> dict[str, Pipeline]:
    feature_eng_pipeline = create_feature_eng_pipeline()

    return {
        "__default__": feature_eng_pipeline
    }