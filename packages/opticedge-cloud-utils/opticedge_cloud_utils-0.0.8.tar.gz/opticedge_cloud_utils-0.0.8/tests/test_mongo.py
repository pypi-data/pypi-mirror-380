import unittest
from unittest.mock import patch, MagicMock
import importlib

# Path of the module under test
MODULE_PATH = "opticedge_cloud_utils.mongo"


class TestMongo(unittest.TestCase):
    def setUp(self):
        # Import fresh module each test to reset _mongo_client
        if MODULE_PATH in globals():
            globals().pop(MODULE_PATH)
        self.module = importlib.import_module(MODULE_PATH)
        if hasattr(self.module, "_mongo_client"):
            self.module._mongo_client = None

    def tearDown(self):
        # Clear cached client after each test
        if hasattr(self.module, "_mongo_client"):
            self.module._mongo_client = None
        importlib.reload(self.module)

    @patch(f"{MODULE_PATH}.get_secret")
    @patch(f"{MODULE_PATH}.MongoClient")
    def test_get_mongo_client_creates_client_and_pings(
        self, mock_mongo_client_cls, mock_get_secret
    ):
        fake_uri = "mongodb://user:pass@host:27017"
        # Arrange mock get_secret(project_id, secret_name)
        mock_get_secret.return_value = fake_uri

        fake_client = MagicMock()
        fake_client.admin.command.return_value = {"ok": 1}
        mock_mongo_client_cls.return_value = fake_client

        # Call with expected args (project_id and uri_secret)
        client = self.module.get_mongo_client(project_id="test-project", uri_secret="mongo-uri")

        # Verify get_secret called with project_id and secret name
        mock_get_secret.assert_called_once_with("test-project", "mongo-uri")
        mock_mongo_client_cls.assert_called_once_with(fake_uri)
        fake_client.admin.command.assert_called_once_with("ping")

        self.assertIs(client, fake_client)
        self.assertIs(self.module._mongo_client, fake_client)

    @patch(f"{MODULE_PATH}.get_secret")
    @patch(f"{MODULE_PATH}.MongoClient")
    def test_get_mongo_client_returns_cached_client_on_subsequent_calls(
        self, mock_mongo_client_cls, mock_get_secret
    ):
        fake_uri = "mongodb://user:pass@host:27017"
        mock_get_secret.return_value = fake_uri

        fake_client = MagicMock()
        fake_client.admin.command.return_value = {"ok": 1}
        mock_mongo_client_cls.return_value = fake_client

        first = self.module.get_mongo_client(project_id="test-project", uri_secret="mongo-uri")
        second = self.module.get_mongo_client(project_id="test-project", uri_secret="mongo-uri")

        # get_secret and MongoClient should only be called once (cached)
        mock_get_secret.assert_called_once_with("test-project", "mongo-uri")
        mock_mongo_client_cls.assert_called_once_with(fake_uri)
        self.assertIs(first, second)
        self.assertIs(self.module._mongo_client, first)

    @patch(f"{MODULE_PATH}.get_secret")
    @patch(f"{MODULE_PATH}.MongoClient")
    def test_get_mongo_client_ping_failure_raises_and_does_not_cache(
        self, mock_mongo_client_cls, mock_get_secret
    ):
        fake_uri = "mongodb://user:pass@host:27017"
        mock_get_secret.return_value = fake_uri

        bad_client = MagicMock()
        bad_client.admin.command.side_effect = Exception("ping failed")
        mock_mongo_client_cls.return_value = bad_client

        with self.assertRaises(Exception) as ctx:
            self.module.get_mongo_client(project_id="test-project", uri_secret="mongo-uri")

        mock_get_secret.assert_called_once_with("test-project", "mongo-uri")
        mock_mongo_client_cls.assert_called_once_with(fake_uri)
        bad_client.admin.command.assert_called_once_with("ping")

        # module should not cache the bad client
        self.assertIsNone(self.module._mongo_client)
        self.assertIn("ping failed", str(ctx.exception))

    @patch(f"{MODULE_PATH}.get_secret")
    @patch(f"{MODULE_PATH}.MongoClient")
    def test_get_mongo_db_returns_database_object(
        self, mock_mongo_client_cls, mock_get_secret
    ):
        fake_uri = "mongodb://user:pass@host:27017"
        mock_get_secret.return_value = fake_uri

        fake_db = MagicMock(name="fake_db")
        fake_client = MagicMock()
        fake_client.admin.command.return_value = {"ok": 1}
        fake_client.__getitem__.return_value = fake_db
        mock_mongo_client_cls.return_value = fake_client

        # Call exclusively with keyword args to avoid positional ambiguity
        db = self.module.get_mongo_db(db_name="opticedge", project_id="test-project", uri_secret="mongo-uri")
        self.assertIs(db, fake_db)
        fake_client.__getitem__.assert_called_once_with("opticedge")
        mock_get_secret.assert_called_once_with("test-project", "mongo-uri")


if __name__ == "__main__":
    unittest.main()
