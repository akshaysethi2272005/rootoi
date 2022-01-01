#user auth schema
import json 
from json import JSONDecodeError
import os 
import pathlib
class User:
    def __init__(self,project_path ,  project_name , key):
        self.project_file = project_path +"\\"+project_name+ ".rootoidb"
        self._json = project_path +"\\"+project_name+ ".json"
        self._module_version = ['0.1.1']
        self._auth_key = key
        self._check1 = os.path.isfile(self.project_file)
        self._check2 = os.path.isfile(self._json)
        self._check3 = pathlib.Path(".\\"+self.project_file).is_file()
        self._check4 = pathlib.Path(".\\"+self._json).is_file()
        self.control = ""
        if(self._check1 == True and self._check2 == True):
            try:
                with open(self._json,"r") as file:
                    self._json_auth_data = json.load(file)
                    self._json_auth_data_keys = self._json_auth_data.keys()
                    if(('version'in self._json_auth_data_keys) and ('gmk' in self._json_auth_data_keys) and ('key'in self._json_auth_data_keys) ):
                        if((self._json_auth_data['version'] == self._module_version[0]) and (self._json_auth_data['gmk'][0] == 'VL@__LOCAL__') and (self._json_auth_data['key'] == self._auth_key)):
                            self.control = self._auth_key 
                        else:
                            raise ValueError
                    else:
                        raise JSONDecodeError
            except Exception as e:
                raise e
        elif(self._check3 == True and self._check4 == True):
            try:
                with open(self._json,"r") as file:
                    self._json_auth_data = json.load(file)
                    self._json_auth_data_keys = self._json_auth_data.keys()
                    if(('version'in self._json_auth_data_keys) and ('gmk' in self._json_auth_data_keys) and ('key'in self._json_auth_data_keys) ):
                        if((self._json_auth_data['version'] == self._module_version[0]) and (self._json_auth_data['gmk'][0] == 'VL@__LOCAL__') and (self._json_auth_data['key'] == self._auth_key)):
                            self.control = self._auth_key 
                        else:
                            raise ValueError
                    else:
                        raise JSONDecodeError
            except Exception as e:
                raise e
        else:
            raise FileNotFoundError
    def is_verified(self) -> dict:
        try:
            return {"verified":True, "key":self.control,"project":self.project_file,"auth": self._json}
        except Exception as e:
            return {"verified":False}
