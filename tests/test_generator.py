from scripts.generator import generate_pipeline


def test_generate_pipeline_exists():
    assert callable(generate_pipeline)
