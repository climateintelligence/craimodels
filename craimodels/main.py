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