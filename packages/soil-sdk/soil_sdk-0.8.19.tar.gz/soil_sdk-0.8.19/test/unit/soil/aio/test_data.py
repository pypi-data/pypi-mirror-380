import unittest
import uuid
from unittest.mock import patch

from soil import errors
from soil.aio.data import DataStructure, data
from soil.types import SerializableDataStructure


class TestData(unittest.IsolatedAsyncioTestCase):
    @patch("soil.aio.data.get_alias")
    @patch("soil.aio.data.get_result")
    async def test_data_with_string_id(self, mock_get_result, mock_get_alias):
        mock_get_alias.side_effect = errors.DataNotFound()
        mock_get_result.return_value = {"_id": "test_id", "type": "test_type"}
        with self.assertRaises(errors.DataNotFound):
            await data("test_id")

    @patch("soil.aio.data.get_alias")
    @patch("soil.aio.data.get_result")
    async def test_data_with_alias(self, mock_get_result, mock_get_alias):
        resolved_id = str(uuid.uuid4())
        mock_get_alias.return_value = {
            "alias": {"result_id": resolved_id},
            "result": {
                "_id": resolved_id,
                "type": "test_type",
                "metadata": {"test_key": "test_value"},
            },
        }
        mock_get_result.return_value = {"nothing": "here"}
        result = await data("test_alias")
        self.assertIsInstance(result, DataStructure)
        self.assertEqual(result.id, resolved_id)
        self.assertEqual(result.dstype, "test_type")
        self.assertEqual(result.metadata, {"test_key": "test_value"})  # pyright:ignore[reportAttributeAccessIssue]

    @patch("soil.aio.data.upload_data")
    async def test_data_with_data_object(self, mock_upload_data):
        test_data = {"key": "value"}
        mock_upload_data.return_value = {"_id": "new_id", "type": "dict"}
        result = await data(test_data)
        self.assertIsInstance(result, DataStructure)
        self.assertEqual(result.id, "new_id")
        self.assertEqual(result.dstype, "dict")

    @patch("soil.aio.data.get_alias")
    @patch("soil.aio.data.get_result")
    async def test_data_with_return_type(self, mock_get_result, mock_get_alias):
        class TestType(SerializableDataStructure):
            pass

        mock_get_alias.side_effect = errors.DataNotFound()
        test_id = str(uuid.uuid4())
        mock_get_result.return_value = {
            "_id": test_id,
            "type": "test_type",
            "metadata": {"test_key": "test_value"},
        }
        result = await data(test_id, return_type=TestType)
        self.assertIsInstance(result, DataStructure)
        self.assertEqual(result.id, test_id)  # pyright:ignore[reportAttributeAccessIssue]
        self.assertEqual(result.dstype, "test_type")  # pyright:ignore[reportAttributeAccessIssue]
        self.assertEqual(result.metadata, {"test_key": "test_value"})  # pyright:ignore[reportAttributeAccessIssue]

    @patch("soil.aio.data.upload_data")
    async def test_data_with_metadata(self, mock_upload_data):
        test_data = {"key": "value"}
        test_metadata = {"meta_key": "meta_value"}
        mock_upload_data.return_value = {"_id": "new_id", "type": "dict"}
        result = await data(test_data, metadata=test_metadata)
        self.assertIsInstance(result, DataStructure)
        self.assertEqual(result.id, "new_id")
        self.assertEqual(result.dstype, "dict")
        mock_upload_data.assert_called_once()
        # Check if metadata is passed correctly
        args, _ = mock_upload_data.call_args
        self.assertEqual(args[2], test_metadata)

    @patch("soil.aio.data.get_alias")
    @patch("soil.aio.data.get_result")
    async def test_data_not_found(self, mock_get_result, mock_get_alias):
        mock_get_alias.side_effect = errors.DataNotFound()
        with self.assertRaises(errors.DataNotFound):
            await data("non_existent_alias")


if __name__ == "__main__":
    unittest.main()
