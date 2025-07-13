from app.pipelines.base_multilingual_uncased_sentiment import (
    NlptownBertBaseMultilingualUncasedSentiment,
)
from app.pipelines.base_pipeline import BasePipeline
from app.pipelines.distilbert_base_uncased_finetuned_sst2_english import (
    DistilBertBaseUncasedFineTunedSst2English,
)
from app.pipelines.types import PipelineType


class PipelineFactory:
    """
    Factory class to create pipeline instances.
    """

    @staticmethod
    def get_pipeline(pipeline_type: PipelineType) -> BasePipeline:
        """
        Returns an instance of the specified pipeline type.

        :param pipeline_type: The type of pipeline to create.
        :return: An instance of the specified pipeline.
        """
        match pipeline_type:
            case PipelineType.distilbert_base_uncased_finetuned_sst2_english:
                return DistilBertBaseUncasedFineTunedSst2English()
            case PipelineType.base_multilingual_uncased_sentiment:
                return NlptownBertBaseMultilingualUncasedSentiment()
            case _:
                raise ValueError(f"Unknown pipeline type: {pipeline_type}")
