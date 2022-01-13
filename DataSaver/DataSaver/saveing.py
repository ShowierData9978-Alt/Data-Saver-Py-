from .Exceptions import NotJsonFile, NotJsonFormat, FileDoesNotExist, NotEnoughtStructure
import json
from .codegen import CodeGenerator as gen
from os.path import exists
import pathlib


class DataSaver:
    def __init__(self, KeyStructure: tuple):

        self.KeyStructure = KeyStructure

    def Add(self, io, Data: any):
        if pathlib.Path(io).suffix == ".json":
            if exists(pathlib.Path(io)):
                with open(io, 'r+') as f:

                    if f.read(1).__str__() == '{':
                        if len(self.KeyStructure) <= 2:
                            self.keys = []
                            for a in range(len(self.KeyStructure)):
                                self.keys.append(self.KeyStructure[a])
                           

                            

                        else:
                            raise NotEnoughtStructure

                    else:
                        raise NotJsonFormat(pathlib.Path(io))
            else:
                raise FileDoesNotExist(pathlib.Path(io))
        else:
            raise NotJsonFile(f"{pathlib.Path(io)} is not a .json file")



    def GeneratePyCode(self,data,fp):
        g = gen()
        key = ""
        for a in self.KeyStructure:
           key =  f'[{a}] {key}'
        g += 'dict = {}'
        g += f"f = open({fp},'r+')"
        g += 'f.write()'
       

