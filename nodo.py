from persona import Persona
class Nodo:
    __elemento: Persona
    __siguiente: object
    def __init__(self,elemento) -> None:
        self.__elemento=elemento
        self.__siguiente=None
    
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getElemento(self):
        return self.__elemento