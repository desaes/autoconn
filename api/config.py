import hydra
from hydra import compose
import os

cwd = os.getcwd()
print(cwd)
hydra.initialize_config_dir(config_dir=f'/conf/itsm')
aranda_conf = compose(config_name='aranda')