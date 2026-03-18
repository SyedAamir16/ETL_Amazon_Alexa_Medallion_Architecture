from dataclasses import dataclass


@dataclass(frozen=True)
class PipelineConfig:
    input_path: str
    database: str = "amazon_alexa"
    warehouse_dir: str = "warehouse"

    @property
    def bronze_table(self) -> str:
        return f"{self.database}.bronze_reviews"

    @property
    def silver_table(self) -> str:
        return f"{self.database}.silver_reviews"

    @property
    def gold_variation_table(self) -> str:
        return f"{self.database}.gold_variation_summary"

    @property
    def gold_daily_table(self) -> str:
        return f"{self.database}.gold_daily_review_summary"

    @property
    def gold_feedback_table(self) -> str:
        return f"{self.database}.gold_feedback_summary"
