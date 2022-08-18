from hydra import compose, initialize
import os
import glob

class Config:
    def __init__(self) -> None:
        self.__config: dict = {}
        self.read_files()

    def read_files(self,config_path: str=os.getcwd()+'/conf/target/') -> None:
        for filename in glob.iglob(config_path + '**/*.yaml', recursive=True):
            (type, object) = (filename.split('/')[-2],filename.split('/')[-1].split('.')[0])
            with initialize(version_base=None, config_path=f'../conf/target/{type}'):
                if not type in self.__config:
                    self.__config[type] = {} 
                if not object in self.__config[type]:
                    self.__config[type][object] = compose(config_name=object)


    def get_config(self) -> dict:
        return self.__config

config = Config()
print(config.get_config())