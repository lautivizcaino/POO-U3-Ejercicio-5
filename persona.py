class Persona:
    __nombre:str
    __edad:int
    __dni:str
    def __init__(self,num,edad,dni) -> None:
        self.__nombre=num
        self.__edad=edad
        self.__dni=dni
    def getNom(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getDni(self):
        return self.__dni
    def __str__(self) -> str:
        return 'Nombre:%s Edad:%s DNI:%s'%(self.__nombre,self.__edad,self.__dni)