#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from core import core
objCore = core()
class funciones:
    def __init__(self):
        init = True      
    def menu(self):
        print("MENÚ PRINCIPAL:")
        print("----------------------")
        print("1. Tomar Agua")
        print("2. Tomar Café")
        print("3. Tomar Gaseosa")
        print("4. Comer")
        print("5. Ir al Baño")
        print("6. Revisar celular")   
        print("7. Charla Grupal")
        print("8. Salir al lunch")
        print("9. Llegar de lunch")
        print("10. Entrada laboral")
        opcion = raw_input("Escriba una opción: ")
        return opcion
    def procesaOpcion(self,opcion):
        salida = ''
        if int(opcion) == 1:
            salida = objCore.tomaAgua(opcion)
        elif int(opcion) == 2:
            salida = objCore.tomaCafe(opcion)
        elif int(opcion) == 10:
            salida = objCore.entradaLaboral(opcion)
        return salida
            
        