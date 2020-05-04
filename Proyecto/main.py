#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:32:25 2020

@author: lovelace
"""
import ADNfuncs
import ADNalternative

def MainMenu():
    op1="- 1: Transcribir un fragmento"
    op2="- 2: Traducir un fragmento"
    op3="- 3: Buscar un Codon a partir de un Aminoácido"
    op4="- 4: Dividir en codones un fragmento de ADN"
    op5="- 5: Hacer un test de Transcripción"
    op6="- 6: Imprimir un diccionario de todos los aminoácidos y sus respectivos codones"
    op7="- 7: Buscar un Aminoácido a partir de un Codon"
    op8="- 8: Ver de nuevo las opciones"
    op9="- 9: Nada"
    print("¿Que desea hacer?")
    print("Las opciones son: \n{0} \n{1} \n{2} \n{3} \n{4} \n{5} \n{6} \n{7} \n{8}".format(op1,op2,op3,op4,op5,op6,op7,op8,op9))
    c=True
    while c == True:
        a=input("responda aquí el número de la opción: ")
        if a == "1":
            x=input("ingrese la cadena de ADN que desea transcribir: ")
            result=ADNfuncs.TRANSCRIPTION(x)
            print(result)
            continuar=input("¿Desea hacer alguna otra cosa? [si/no]: ")
            if continuar == "si":
                c=True
            elif continuar == "no":
                c=False
            else:
                c=False 
                
        elif a == "2":
            x=input("ingrese la cadena de ADN/ARN a traducir: ")
            result=ADNfuncs.Search4Amino(x)
            print(result)
            continuar=input("¿Desea hacer alguna otra cosa? [si/no]: ")
            if continuar == "si":
                c=True
            elif continuar == "no":
                c=False
            else:
                c=False
                
        elif a == "3":
            print("Note que debe escribir correctamente el nombre del aminoácido para que sea posible buscarlo, la forma es: Forma abreviada del aminoácido (Forma competa del aminoácido) \nLas mayús son importantes en el principio de los nombres al igual que el espacio entre el nombre y el paréntesis. \n" )
            x=input("ingrese el aminoácido a partir del cual buscar: ")
            result=ADNalternative.Search4Codons(x)
            print(result)
            continuar=input("¿Desea hacer alguna otra cosa? [si/no]: ")
            if continuar == "si":
                c=True
            elif continuar == "no":
                c=False
            else:
                c=False
                
        elif a == "4":
            x=input("Ingese el fragmento de ADN a separar en codones: ")
            result=ADNfuncs.Divideincodons(x)
            print(result)
            continuar=input("¿Desea hacer alguna otra cosa? [si/no]: ")
            if continuar == "si":
                c=True
            elif continuar == "no":
                c=False
            else:
                c=False
                
        elif a == "5":
            result=ADNalternative.ADNtest()
            print(result)
            continuar=input("¿Desea hacer alguna otra cosa? [si/no]: ")
            if continuar == "si":
                c=True
            elif continuar == "no":
                c=False
            else:
                c=False
                
        elif a == "6":
            result=ADNfuncs.Aminoacids()
            print(result)
            continuar=input("¿Desea hacer alguna otra cosa? [si/no]: ")
            if continuar == "si":
                c=True
            elif continuar == "no":
                c=False
            else:
                c=False
        elif a == "9":
            c=False
            print ("Ok, ¡Hasta luego!")
            continuar=input("¿Desea hacer alguna otra cosa? [si/no]: ")
            if continuar == "si":
                c=True
            elif continuar == "no":
                c=False
            else:
                c=False
            
        elif a== "8":
            print("Las opciones son: \n{0} \n{1} \n{2} \n{3} \n{4} \n{5} \n{6} \n{7}".format(op1,op2,op3,op4,op5,op6,op7,op8)) 
            continuar=input("¿Desea hacer alguna otra cosa? [si/no]: ")
            if continuar == "si":
                c=True
            elif continuar == "no":
                c=False
            else:
                c=False
        elif a== "7":
            x=input("Escriba el codon con el que se buscará: ")
            result= ADNfuncs.Search4Amino(x)
            print(result)
        else:
            print("¡esa no es una opción!")
        
    if c== False and a != "9":
        print("Ok, ¡Hasta luego!")
        
        
MainMenu()