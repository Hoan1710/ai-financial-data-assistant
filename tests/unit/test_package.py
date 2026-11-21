from importlib import import_module

import pytest


@pytest.mark.parametrize("module", ["contracts.plan", "data_pipeline.snapshot", "nlu.linker", "models.predictor", "engine.execute", "api.main"])
def test_core_modules_are_importable(module):
    import_module(f"finassistant.{module}")
