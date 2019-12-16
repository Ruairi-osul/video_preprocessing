import json

def json_to_dict(file_path):
    """
    Given a path to a JSON file, returns a dictionary containing
    The contents of that file
    
    Params:
        - file_path: the path to the JSON file
    """
    with open(file_path) as f:
        output = json.load(f)
    return output