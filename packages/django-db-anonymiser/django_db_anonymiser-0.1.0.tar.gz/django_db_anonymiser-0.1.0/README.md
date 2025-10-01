# django-db-anonymiser
Django app to create configurable anonymised DB dumps.

django-db-anonymiser provides a django app with a management command `dump_and_anonymise`.
This command runs a `pg_dump` against a postgresql DB, applies anonymisation functions to 
data dumped from the DB and then writes the anonymised dump to S3.
See here for lite-api's example anonymisation configuration; https://github.com/uktrade/lite-api/blob/dev/api/conf/anonymise_model_config.yaml

This pattern is designed as a replacement for Lite's old DB anonymisation process (although it is general purpose and can be used for any django project which uses postgresql).
The previous process was baked in to an airflow installation and involved making
a `pg_dump` from production, anonymising that dump with python and pushing the 
file to S3. See; https://github.com/uktrade/lite-airflow-dags/blob/master/dags/export_lite_db.py

django-db-anonymiser follows the same overall pattern, but aims to achieve it
through a django management command instead of running on top of airflow.  In addition,
the configuration for how DB columns are anonymised can be configured in simple YAML.

**Note:** This repository depends upon code forked from https://github.com/andersinno/python-database-sanitizer
This is housed under the `database_sanitizer` directory and has been forked from the above repository 
because it is unmaintained.

## Getting started

- Add `faker>=4.18.0`, `boto3>=1.26.17` to python requirements; it is assumed python/psycopg and co are already installed.
- Either add this github repository as a submodule to your django application named `django_db_anonymiser` or install the python package (django-db-anonymiser)[] from PyPI.
- Add `django_db_anonymiser.db_anonymiser` to `INSTALLED_APPS`
- Set the following django settings;
    - `DB_ANONYMISER_CONFIG_LOCATION` - the location of your anonymisation yaml file
    - `DB_ANONYMISER_AWS_ENDPOINT_URL` - optional, custom URL for AWS (e.g. if using minio)
    - `DB_ANONYMISER_AWS_ACCESS_KEY_ID` - AWS access key ID for the S3 bucket to upload dumps to
    - `DB_ANONYMISER_AWS_SECRET_ACCESS_KEY` - AWS secret key for the S3 bucket to upload dumps to
    - `DB_ANONYMISER_AWS_REGION` - AWS region for the S3 bucket to upload dumps to
    - `DB_ANONYMISER_AWS_STORAGE_BUCKET_NAME` - AWS bucket name for the S3 bucket to upload dumps to

## Running tests

For local unit testing from the root of the repository run:

    $ poetry run pytest

**Note:** Currently for full test coverage, it is necessary to run tests in circleci, where we spin up a postgres db and test
the `db_anonymiser` command directly

## Publishing

Publishing to PyPI is currently a manual process:

1. Acquire API token from [Passman](https://passman.ci.uktrade.digital/secret/0f3d699a-1c7a-4e92-a235-6c756f678dd5/).
   - Request access from the SRE team.
   - _Note: You will need access to the `platform` group in Passman._
2. Run `poetry config pypi-token.pypi <token>` to add the token to your Poetry configuration.

Update the version, as the same version cannot be published to PyPI.

```
poetry version patch
```

More options for the `version` command can be found in the [Poetry documentation](https://python-poetry.org/docs/cli/#version). For example, for a minor version bump: `poetry version minor`.

Build the Python package.

```
poetry build
```

Publish the Python package.

_Note: Make sure your Pull Request (PR) is approved and contains the version upgrade in `pyproject.toml` before publishing the package._

```
poetry publish
```

Check the [PyPI Release history](https://pypi.org/project/dbt-platform-helper/#history) to make sure the package has been updated.

For an optional manual check, install the package locally and test everything works as expected.
