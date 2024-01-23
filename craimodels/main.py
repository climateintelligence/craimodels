import pkgutil
import pathlib
import yaml

def raw_text():
    return pkgutil.get_data(__name__, "models/info-models.yml")

def info_models():
    path = pkgutil.get_data(__name__, "models/info-models.yml")
    return yaml.safe_load(path)

def model_dir():
    return pathlib.Path(__file__).parent / "models/"

def metadata():
    info_dict = {}
    info = info_models()
    for key in info.keys():
        info_dict[key] = [
            {"name": "dataset_name", "value": key, "title": info[key]["description"]},
            {"name": "file", "value": info[key]["file"], "title": "Enter the URL of the netcdf file or ZIP archive."},
            {"name": "variable_name", "value": info[key]["variable_name"], "title": info[key]["variable_name"]}
        ]
    return info_dict