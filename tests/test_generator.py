from scripts.generator import generate_pipeline

def test_generate_pipeline_returns_string():
    blueprint = {
        "name": "test-pipeline",
        "steps": [{"name": "step1", "command": "echo Hello"}]
    }
    result = generate_pipeline(blueprint)
    assert isinstance(result, str)

