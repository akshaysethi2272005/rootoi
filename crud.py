from schema import User
import json
from rootoierror import *
def _sequel(data):
    _a = ""
    for i in data:
        _a+=str(i) + " "
    return _a
class CRUD_ROOTOI:
    """
    RD - Rootoi Delete
    """
    def __init__(self,project_path ,  project_name , key,column):
        self.user_auth = User(project_path ,  project_name , key )
        self.user_auth_res = self.user_auth.is_verified()
        self.uik = key
        self.col = column
        if(self.user_auth_res['verified'] == True):
            with open(self.user_auth_res['auth'],"r") as self._jf:
                self._jslo = json.load(self._jf)
                if(self._jslo['key'] == self.uik):
                    if(type(column) == int):
                        self._current_operation = True
                    else:
                        raise ValueError("Column must be an integer")
                else:
                    raise RootoiKeyUnverifiedError
        else:
            raise RootoiBaseUnverifiedError
    def write(self, data):
        if(type(data) == list):
            self.pro = self.user_auth_res['project']
            if(self.col == len(data)):
                with open(self.pro , "a") as self.wf:
                    self.strr = ""
                    for i in range(len(data)):
                        self.strr += str(data[i]) + " "
                    self.wf.write(self.strr+"\n")
            else:
                raise ValueError("Column must be Equal")
        else:
            raise ValueError("List datatype Should be used here")
    def read(self):
        self.proo = self.user_auth_res['project']
        self.retrive = []
        with open(self.proo,"r") as self.rf:
            self.newstrr = [i.strip().split(" ") for i in self.rf.readlines()]
            return self.newstrr
    def read_by_row(self,row):
        if(row <= 0):
            self.proo = self.user_auth_res['project']
            self.retrive = []
            with open(self.proo,"r") as self.rf:
                self.newstrr = [i.strip().split(" ") for i in self.rf.readlines()]
                return self.newstrr[row-1]
        else:
            raise ValueError("The Value must be greater than 0")
    def read_by_column(self,col):
        if(col <= 0):
            self.proo = self.user_auth_res['project']
            self.retrive = []
            with open(self.proo,"r") as self.rf:
                self.newstrr = [i.strip().split(" ") for i in self.rf.readlines()]
                self.leni = len(self.newstrr[0])
                self.copi = []
                for i in self.newstrr:
                    self.copi.append(i[col-1])
            return self.copi
        else:
            raise ValueError("The Value must be greater than 0")
    def update(self,row,col,value):
        if(row <= 0 or col <= 0):
            self.proo = self.user_auth_res['project']
            self.retrive = []
            self.blk = []
            self.neww = ""
            with open(self.proo,"r") as self.rf:
                self.newstrr = [i.strip().split(" ") for i in self.rf.readlines()]
                self.newstrr[row-1][col-1] = str(value)
            self.blk.append(self.newstrr)
            open(self.proo,"w").close()
            with open(self.proo, "a") as self.uf:
                for i in self.blk[0]:
                    self._ef = _sequel(i)
                    self.uf.write(self._ef+"\n")
        else:
            raise ValueError("The Value must be greater than 0")
    def delete(self, row, col):
        if(row <= 0 or col <= 0):
            self.proo = self.user_auth_res['project']
            self.retrive = []
            self.blk = []
            self.neww = ""
            with open(self.proo,"r") as self.rf:
                self.newstrr = [i.strip().split(" ") for i in self.rf.readlines()]
                self.newstrr[row-1][col-1] = "RD"
            self.blk.append(self.newstrr)
            open(self.proo,"w").close()
            with open(self.proo, "a") as self.uf:
                for i in self.blk[0]:
                    self._ef = _sequel(i)
                    self.uf.write(self._ef+"\n")
        else:
            raise ValueError("The Value must be greater than 0")
    def delete_by_row(self, row):
        if(row <= 0):
            self.proo = self.user_auth_res['project']
            self.retrive = []
            self.blk = []
            self.neww = ""
            with open(self.proo,"r") as self.rf:
                self.newstrr = [i.strip().split(" ") for i in self.rf.readlines()]
            self.newstrr.pop(row-1)
            self.blk.append(self.newstrr)
            open(self.proo,"w").close()
            with open(self.proo, "a") as self.uf:
                for i in self.blk[0]:
                    self._ef = _sequel(i)
                    self.uf.write(self._ef+"\n")
        else:
            raise ValueError("The Value must be greater than 0")
    def delete_by_column(self,col):
        if(col <= 0):
            self.proo = self.user_auth_res['project']
            self.retrive = []
            self.blk = []
            self.neww = ""
            with open(self.proo,"r") as self.rf:
                self.newstrr = [i.strip().split(" ") for i in self.rf.readlines()]
            for i in self.newstrr:
                i.pop(col-1)
                self.retrive.append(i)
            self.blk.append(self.retrive)
            open(self.proo,"w").close()
            with open(self.proo, "a") as self.uf:
                for i in self.blk[0]:
                    self._ef = _sequel(i)
                    self.uf.write(self._ef+"\n")
        else:
            raise ValueError("The Value must be greater than 0")
