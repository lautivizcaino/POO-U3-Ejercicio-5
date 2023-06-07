from zope.interface import implementer
import csv
from nodo import Nodo
from persona import Persona
from interface import Interfaz
from indiceExcepcion import IndiceException

@implementer(Interfaz)
class Lista:
    __comienzo:Nodo
    __cantidad:int
    def __init__(self) -> None:
        self.__comienzo=None
        self.__cantidad=0
    def agregarPersona(self,elemento):
        nodo=Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__cantidad+=1
    def mostrarLista(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getElemento())
            aux=aux.getSiguiente()
        
    def leerArchivo(self):
        file=open('personas.csv',encoding='utf-8')
        reader=csv.reader(file,delimiter=';')
        for row in reader:
            unaPersona=Persona(row[0],int(row[1]),row[2])
            nodo=Nodo(unaPersona)
            self.agregarPersona(unaPersona)
        file.close()

    def insertarElemento(self):
        posicion=int(input('Ingrese la posicion del elemento a ingresar: '))
        contador=0
        if posicion>=0 and posicion<=self.__cantidad:
            nom=input('Ingrese nombre: ')
            edad=int(input('Ingrese edad: '))
            dni=input('Ingrese DNI: ')
            unaPersona=Persona(nom,edad,dni)
            nodo=Nodo(unaPersona)
            if posicion==0:
                self.agregarPersona(unaPersona)
            else:
                post=self.__comienzo
                anterior=self.__comienzo
                while post!=None and contador<posicion:
                    anterior=post
                    post=post.getSiguiente()
                    contador+=1
                if contador==posicion:
                    anterior.setSiguiente(nodo)
                    nodo.setSiguiente(post)

        else:
            raise IndiceException('La posicion insertada no es válida')
                

    def agregarElemento(self):
        nom=input('Ingrese nombre: ')
        edad=int(input('Ingrese edad: '))
        dni=input('Ingrese DNI: ')
        unaPersona=Persona(nom,edad,dni)
        nodo=Nodo(unaPersona)
        nodo.setSiguiente(None)
        if self.__comienzo==None:
            self.__comienzo=nodo
        else:
            p=self.__comienzo
            while p!=None:
                anterior=p
                p=p.getSiguiente()
            anterior.setSiguiente(nodo)
            self.__cantidad+=1

    def mostrarElemento(self):
        posicion=int(input('Ingrese la posicion del elemento a ingresar: '))
        contador=0
        if posicion>=0 and posicion<=self.__cantidad:
            if posicion==0:
                print(self.__comienzo.getElemento())
            else:
                aux=self.__comienzo
                while aux!=None and contador<posicion:
                    aux=aux.getSiguiente()
                    contador+=1
                if contador==posicion:
                    print(aux.getElemento())

        else:
            raise IndiceException('La posicion insertada no es válida')