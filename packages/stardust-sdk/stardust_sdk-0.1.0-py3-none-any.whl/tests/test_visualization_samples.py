import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from stardust.visualization.visual import ToAnnotationTool


FIXTURE_DIR = Path(__file__).resolve().parents[1] / "demo" / "visualization_demo"


class VisualizationSamplesTest(unittest.TestCase):
    def setUp(self) -> None:
        self._original_cwd = os.getcwd()
        self._temp_dir = tempfile.TemporaryDirectory()
        os.chdir(self._temp_dir.name)

    def tearDown(self) -> None:
        os.chdir(self._original_cwd)
        self._temp_dir.cleanup()

    def _copy_fixture(self, filename: str) -> str:
        destination = Path(self._temp_dir.name) / filename
        destination.write_text((FIXTURE_DIR / filename).read_text(encoding="utf-8"), encoding="utf-8")
        return str(destination)

    @mock.patch("os.system", return_value=0)
    def test_object_detection_fixture_generates_annotation_payload(self, mock_system: mock.MagicMock) -> None:
        data_path = self._copy_fixture("object_detection.json")
        with mock.patch("time.strftime", return_value="20240101-000000"):
            url = ToAnnotationTool(data_path, "object_detection")

        self.assertTrue(url.endswith("/object_detection/20240101-000000.json"))

        output_path = Path("results/object_detection/20240101-000000.json")
        self.assertTrue(output_path.exists())

        result_payload = json.loads(output_path.read_text(encoding="utf-8"))
        source_payload = json.loads(Path(data_path).read_text(encoding="utf-8"))
        self.assertEqual(result_payload["taskParams"]["value"]["record"]["attachment"], source_payload["attachment"])
        mock_system.assert_called_once()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
