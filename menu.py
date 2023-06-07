from lista import Lista
class Menu:
    __opcion:int
    def __init__(self):
        self.__opcion=int
    def opciones(self,lista):
        while self.__opcion!=0:
            print('\n1 - Insertar Elemento\n2 - Agregar Elemento\n3 - Mostrar Elemento\n0 - Salir\n')
            self.__opcion=int(input('Ingrese la opción a ejecutar: '))
            if self.__opcion==1:
                print('OPCION 1\n')
                lista.insertarElemento()
            elif self.__opcion==2:
                print('OPCION 2\n')
                lista.agregarElemento()
            elif self.__opcion==3:
                print('OPCION 3\n')
                lista.mostrarElemento()
        else:
            print('\nHA SALIDO DEL SISTEMA')