from deepstate.core.base import AnalysisBackend

# Load the config directly using build_from_config
result = AnalysisBackend.build_from_config("tests/config/test_config.ini")

print("Values and their types:")
for key, val in result.items():
    print(f"  {key} = {val!r}  (type: {type(val).__name__})")

# Assert numeric fields came back as ints, not strings
assert isinstance(result["timeout"], int), f"timeout should be int, got {type(result['timeout'])}"
assert isinstance(result["mem_limit"], int), f"mem_limit should be int, got {type(result['mem_limit'])}"
assert isinstance(result["min_log_level"], int), f"min_log_level should be int, got {type(result['min_log_level'])}"

print("\nAll assertions passed! Types are correctly cast.")
