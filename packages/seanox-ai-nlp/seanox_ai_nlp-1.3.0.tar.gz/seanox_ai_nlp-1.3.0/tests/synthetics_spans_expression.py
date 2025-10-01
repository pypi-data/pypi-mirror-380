# tests/test_synthetics_synthetics.py

from seanox_ai_nlp.synthetics import synthetics, TemplateConditionException
from time import perf_counter
from pathlib import Path
from spacy.cli import download

import pathlib
import random
import copy
import json
import pytest
import re
import importlib

TESTS_PATH = Path("./tests") if Path("./tests").is_dir() else Path(".")
EXAMPLES_PATH = Path("./examples") if Path("./examples").is_dir() else Path("../examples")


def test_synthetics_spans_expression_01():
#    synthetic = synthetics(
#        TESTS_PATH,
#        "synthetics_spans_expression.yaml",
#        {
#            "template": 1
#        }
#    )
#    print()
#    print(synthetic)
    pass