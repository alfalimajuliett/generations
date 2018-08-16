from .base_model import default_config_filename
from shutil import copyfile
copyfile(default_config_filename, "model_parameters.cfg")
