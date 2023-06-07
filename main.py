from lista import Lista
from persona import Persona
from menu import Menu
def test():
    lista=Lista()
    lista.leerArchivo()
    menu=Menu()
    menu.opciones(lista)
    lista.mostrarLista()
if __name__=='__main__':
    test()
    