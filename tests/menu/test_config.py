import os
from jsonschema import validate
from buildtest.defaults import DEFAULT_SETTINGS_SCHEMA
from buildtest.menu.config import (
    func_config_view,
    func_config_validate,
    func_config_summary,
)
from buildtest.utils.file import walk_tree
from buildtest.schemas.utils import load_schema, load_recipe

pytest_root = os.path.dirname(os.path.dirname(__file__))


def test_view_configuration():
    func_config_view()


def test_valid_config_schemas():

    valid_schema_dir = os.path.join(pytest_root, "examples", "config_schemas", "valid")
    schema_config = load_schema(DEFAULT_SETTINGS_SCHEMA)
    for schema in walk_tree(valid_schema_dir, ".yml"):
        example = load_recipe(os.path.abspath(schema))
        validate(instance=example, schema=schema_config)


def test_config_validate():

    func_config_validate()


def test_config_summary():

    func_config_summary()
