import os
from unittest.mock import patch

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TransactionTestCase

import boto3
import pytest
from moto import mock_aws


@pytest.mark.skipif(os.getenv("CIRCLECI") != "true", reason="Skipped because test requires real postgres db.")
@mock_aws
class TestDumpAndAnonmyiseCommand(TransactionTestCase):
    def setUp(self):
        self.aws = boto3.client("s3", region_name=settings.DB_ANONYMISER_AWS_REGION)
        self.aws.create_bucket(
            Bucket=settings.DB_ANONYMISER_AWS_STORAGE_BUCKET_NAME,
            CreateBucketConfiguration={
                "LocationConstraint": settings.DB_ANONYMISER_AWS_REGION
            },
        )

    @patch(
        "django_db_anonymiser.db_anonymiser.management.commands.dump_and_anonymise.run"
    )
    @patch(
        "django_db_anonymiser.db_anonymiser.management.commands.dump_and_anonymise.Configuration"
    )
    def test_dump_and_anonymise_calls_anonymiser(
        self, mocked_configuration, mocked_anonymiser_run
    ):
        call_command(
            "dump_and_anonymise", keep_local_dumpfile=False, skip_s3_upload=True
        )
        call_args, call_kwargs = mocked_anonymiser_run.call_args
        assert (
            call_kwargs["url"]
            == f"postgresql://{settings.DATABASES['default']['USER']}:{settings.DATABASES['default']['PASSWORD']}@{settings.DATABASES['default']['HOST']}:{settings.DATABASES['default']['PORT']}/{settings.DATABASES['default']['NAME']}"
        )
        assert call_kwargs["config"] == mocked_configuration.from_file.return_value
        assert call_kwargs["output"].name == "/tmp/anonymised.sql"
        # Ensure skip_s3_upload was respected
        bucket_contents = self.aws.list_objects(
            Bucket=settings.DB_ANONYMISER_AWS_STORAGE_BUCKET_NAME
        ).get("Contents", [])
        assert bucket_contents == []

    def test_dump_and_anonymise_writes_sql(self):
        user = User.objects.create(
            first_name="Bob",
            last_name="Benson",
            email="bob.benson@example.net",  # /PS-IGNORE
            username="bob.benson",
        )
        call_command(
            "dump_and_anonymise", keep_local_dumpfile=True, skip_s3_upload=True
        )
        dump_sql = ""
        with open(f"/tmp/{settings.DB_ANONYMISER_DUMP_FILE_NAME}") as f:
            dump_sql = f.read()
        assert user.username in dump_sql
        assert user.first_name not in dump_sql
        assert user.last_name not in dump_sql
        assert user.email not in dump_sql

    def test_dump_and_anonymise_writes_to_s3(self):
        call_command("dump_and_anonymise", keep_local_dumpfile=False)
        bucket_contents = self.aws.list_objects(
            Bucket=settings.DB_ANONYMISER_AWS_STORAGE_BUCKET_NAME
        ).get("Contents", [])
        assert bucket_contents[0]["Key"] == settings.DB_ANONYMISER_DUMP_FILE_NAME

    @patch(
        "django_db_anonymiser.db_anonymiser.management.commands.dump_and_anonymise.os.remove"
    )
    def test_dump_and_anonymise_clears_local_file(self, mocked_os_remove):
        call_command("dump_and_anonymise")
        mocked_os_remove.assert_called_with(
            f"/tmp/{settings.DB_ANONYMISER_DUMP_FILE_NAME}"
        )

    @patch(
        "django_db_anonymiser.db_anonymiser.management.commands.dump_and_anonymise.os.remove"
    )
    def test_dump_and_anonymise_keeps_local_file(self, mocked_os_remove):
        call_command("dump_and_anonymise", keep_local_dumpfile=True)
        assert not mocked_os_remove.called
