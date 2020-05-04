# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 17:11:23 2020

@author: Feligx
"""
def Uppercase_it(x):
    x=x.upper()
    return x

def TRANSCRIPTION (x):
    if "a" or "t" or "c" or "g" in x:
        X=Uppercase_it(x)
    ARN=""
    BasesN=["A","T","C","G"]
    for i in X:
        if i in BasesN:
           if i == "A":
              ARN=ARN+"U"
           elif i == "T":
              ARN=ARN+"A"
           elif i == "C":
               ARN=ARN+"G"
           elif i == "G":
               ARN=ARN+"C"
           else:
               print("no es una cadena de ADN")
    return ARN

#LOPA=list of possible aminoacids

def create_LOPA():          #esta función crea una lista con todos los posibles aminoacidos y los codones que les codifican
    txt=open("codones/lopa.txt","r")
    LOPAtxt=[]
    LOPA_=txt.readlines()
    txt.seek(0)
    for i in range (len(LOPA_)):
        LOPA=txt.readline()
        LOPA=LOPA.rstrip("\n")
        LOPAtxt.append(LOPA)
    return LOPAtxt


def Aminoacids (): #esta función crea un diccionario a partir de la lista creada anteriormente.
    codons=create_LOPA()
    aminoacid_dict={}
    for i in codons:
        cod1=open("codones/"+i, "r", encoding="utf8")
        aminoacid=[]
        cod1_=cod1.readlines()
        cod1.seek(0)
        for i in range(len(cod1_)):
            cod2=cod1.readline()
            cod2=cod2.rstrip("\n")
            aminoacid.append(cod2)
            aminoacid_dict[aminoacid[i]]=aminoacid[0]
    return aminoacid_dict


def Codons ():
    codons=create_LOPA()
    aminoacid_dict={}
    for i in codons:
        cod1=open("codones/"+i, "r", encoding="utf8")
        aminoacid=[]
        cod1_=cod1.readlines()
        cod1.seek(0)
        for i in range(len(cod1_)):
            cod2=cod1.readline()
            cod2=cod2.rstrip("\n")
            aminoacid.append(cod2)
            aminoacid_dict[aminoacid[0]]=aminoacid[1:]
    return aminoacid_dict


def Divideincodons(x):
    counter=0
    codons_list=[]
    x=x.upper()
    if "T" in x:
        x=TRANSCRIPTION(x)
    elif "a" or "u" or "c" or "g" in x:
        x=Uppercase_it(x)
    for i in range(int(len(x)/3)):
        counter1=counter+3
        a=x[counter:counter1]
        counter+=3
        codons_list.append(a)
    return codons_list
        

def Search4Amino(x):
    amino_dict=Aminoacids()
    codon_list=Divideincodons(x)
    amino_result=[]
    msg=""
    counter=0
    for i in codon_list:
        if (i in amino_dict) and amino_dict[i]=="Met (Metionina) *Inicio*":
            for i in codon_list[counter:]:
                if i in amino_dict:
                    a=amino_dict[i]
                    amino_result.append(a)
                    if a == "STOP":
                        break    
        counter += 1
    if amino_result == []:
        msg="No hay un codon de inicio para comenzar la traducción"
    if msg != "":
        return msg
    else:
        return amino_result

