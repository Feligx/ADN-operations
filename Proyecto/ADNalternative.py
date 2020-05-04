# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:45:40 2020

@author: Feligx
"""
import random
import ADNfuncs

def Search4Codons(x):
    amino_dict=ADNfuncs.Codons()
    amino_result=[]
    a=True
    while a==True:
        if x in amino_dict:
            a=amino_dict[x]
            amino_result.append(a)
            print("su última búsqueda fue : {0}".format(amino_result))
                
            ans=input("¿Quiere buscar otro aminoácido?  [Si / No] : ")    
            if ans == "Si":
                a=True
                x=input("Ingrese el siguiente aminoácido a buscar")
            elif ans== "No":
                a=False
            else:
                print("no es una respuesta válida, se cerrará la ejecución")
                a=False
        elif x not in amino_dict:
            a=False
            print("Asegúrese de que escribió bien el nombre del aminoácido, recuerde que es: Nombreamino_abrev (Nombreaminocompleto)")
             
    return "su última búsqueda fue: {0}".format(amino_result)



def ADNtest():

    b=int(input("¿De qué longitud quieres la cadena de ADN?"))

    letters=['A','T','C','G']

    ADN=""

    for i in range (0,b):
        a=random.choice(letters)
        ADN+=a
    print(ADN)
    
    c=str(input("escribe la cadena en ARN"))

    ARN= ADNfuncs.TRANSCRIPTION(ADN)
    print(ARN)
    if ARN==c:
        print("Respuesta correcta")
    else:
        print("Respuesta incorrecta, la respuesta correcta sería: {0}".format(ARN))