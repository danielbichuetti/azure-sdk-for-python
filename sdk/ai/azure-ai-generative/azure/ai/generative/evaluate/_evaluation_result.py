from typing import Dict

class EvaluationResult(object):

    def __init__(self, metrics_summary: Dict[str, float], artifacts: Dict[str, str], **kwargs):
        self._metrics_summary = metrics_summary
        self._artifacts = artifacts
        self._tracking_uri = kwargs.get("tracking_uri")
        self._evaluation_id = kwargs.get("evaluation_id")

    @property
    def metrics_summary(self) -> Dict[str, float]:
        return self._metrics_summary

    @property
    def artifacts(self) -> Dict[str, str]:
        return self._artifacts

    @property
    def tracking_uri(self) -> str:
        return self._tracking_uri

    def download_evaluation_artifacts(self, path: str) -> str:
        from mlflow.artifacts import download_artifacts
        for artifact, artifact_uri in self.artifacts.items():
            download_artifacts(
                artifact_uri=artifact_uri,
                tracking_uri=self.tracking_uri,
                dst_path=path
            )
