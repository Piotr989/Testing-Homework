from homework import take_from_list, calculate
import json
import tempfile
import os

# Checking exceptions
def test_take_from_list_wrong_type():
    try:
        take_from_list([1, 2, 3], "wrong")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    try:
        take_from_list([1, 2, 3], [1, "hello"])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    try:
        take_from_list([1, 2, 3], 0.7)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    try:
        take_from_list([1, 2, 3], 7)
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError"

# Writing to temp files
def test_calculate_with_temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        in_path = os.path.join(tmpdir, "input.json")
        out_path = os.path.join(tmpdir, "output.json")

        # Write input file
        data = {"list": [1, 2, 3, 4, 5], "indices": [0, 2]}
        with open(in_path, "w") as f:
            json.dump(data, f)

        # Call calculate with temp files
        calculate(in_path, out_path)

        # Read and check output
        with open(out_path) as f:
            result = json.load(f)
        assert result == [1, 3]

# Mock function
def test_calculate_with_mock(monkeypatch):
    
    def mock_take_from_list(li, indices):
        return ["wynik"]

    monkeypatch.setattr("homework.take_from_list", mock_take_from_list)

    with tempfile.TemporaryDirectory() as tmpdir:
        in_path = os.path.join(tmpdir, "input.json")
        out_path = os.path.join(tmpdir, "output.json")
        data = {"list": [1, 2, 3], "indices": [0, 2]}
        with open(in_path, "w") as f:
            json.dump(data, f)
        calculate(in_path, out_path)
        with open(out_path) as f:
            result = json.load(f)
        assert result == ["wynik"]