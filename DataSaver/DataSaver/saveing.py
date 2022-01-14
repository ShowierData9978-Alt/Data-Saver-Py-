from .Exceptions import NotJsonFile, NotJsonFormat, FileDoesNotExist, NotEnoughtStructure
import json
from .CodeGenerator.codegen import CodeGenerator as gen
from os.path import exists
import pathlib


class DataSaver:
    def __init__(self, KeyStructure: tuple):

        self.KeyStructure = KeyStructure

    def Add(self, io, Data:any):
        if pathlib.Path(io).suffix == ".json":
            if exists(pathlib.Path(io)):
                with open(io, 'r+') as f:

                    if f.read(1).__str__() == '{':
                        if len(self.KeyStructure) <= 2:
                              #exec(self.GeneratePyCode(Data,io))
                              self.picode = self.GeneratePyCode(Data,io)
                              open("DataSaver/DataSaver/CodeGenerator/CustumWrite.py",'w').write("")
                              with open("DataSaver/DataSaver/CodeGenerator/CustumWrite.py",'a') as f :
                               
                               for NL in self.picode:
                                   print(NL)
                                   f.write(f"{NL}")
                              from DataSaver.DataSaver.CodeGenerator.CustumWrite import write
                              write()
                                  
                            

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
           key =  f'[{a}]{key}'
        g += 'import json\n'
        g += 'def Write():\n'
       

        g += '\tdict1 = {}\n'
        
        g += f'\tdict1{key}.update({data})\n'
        
        g += f"\tf = open('{fp}','r+')\n"
        
        g += '\tjson.dump(dict1,f)\n'
        return g.__str__()
       

