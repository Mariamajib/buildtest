import pytest
import os
import random
import shutil
import string
import tempfile
import unittest
import uuid
import logging
import re

#from buildtest.defaults import console
#from buildtest.buildsystem.builders import Builder
#import regex_check
from buildtest.buildsystem.checks import (
regex_check,
is_file,
is_dir
)

logger = logging.getLogger(__name__)

from buildtest.utils.file import (
    create_dir,
    create_file,
    is_dir,
    is_file,
    is_symlink,
    load_json,
    read_file,
    remove_file,
    resolve_path,
    search_files,
    walk_tree,
    write_file,
)

def test_regex_check():
    #assert regex_check.regex_check(builder) == True
    file_name = str(uuid.uuid4())
    assert not is_file(file_name)
    #assert is_file("/bin/bash")

#x = " "
#b = buildtest.buildsystem.base.BuilderBase
test_regex_check()
