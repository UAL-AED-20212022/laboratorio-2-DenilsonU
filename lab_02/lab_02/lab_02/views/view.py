from models.LinkedList import LinkedList
from models.Node import Node
import controllers.controllers

def main():
    lista_ligada = LinkedList()
    while True:
        comandos = input().split(" ")
        if comandos[0] == "RPI":
            RPI(lista_ligada, comandos[1])
        if comandos[0] == "RPF":
            RPF(lista_ligada, comandos[1])
        if comandos[0] == "RPDE":
            RPDE(lista_ligada, comandos[2], comandos[1])
        if comandos[0] == "RPAE":
            RPAE(lista_ligada, comandos[2], comandos[1])
        if comandos[0] == "RPII":
            RPII(lista_ligada,int(comandos[2]),comandos[1])
        if comandos[0] == "VNE":
            VNE(lista_ligada)
        if comandos[0] == "VP":
            VP(lista_ligada, comandos[1])
        if comandos[0] == "EPE":
            EPE(lista_ligada)
        if comandos[0] == "EUE":
            EUE(lista_ligada)
        if comandos[0] == "EP":
            EP(lista_ligada, comandos[1])
        

def RPI(lista_ligada, elemento):
    controllers.controllers.inserir_inicio(lista_ligada,elemento)
    LinkedList.traverse_list(lista_ligada)

def RPF(lista_ligada, elemento):
    controllers.controllers.inserir_final(lista_ligada, elemento)
    LinkedList.traverse_list(lista_ligada)

def RPDE(lista_ligada, novo, elemento):
    controllers.controllers.inserir_depois_de_outro_elemento(lista_ligada, novo ,elemento)
    LinkedList.traverse_list(lista_ligada)

def RPAE (lista_ligada , novo, elemento):
    controllers.controllers.inserir_elemento_antes_de_outro(lista_ligada , novo, elemento)
    LinkedList.traverse_list(lista_ligada)
 
def RPII (lista_ligada, elemento,index):
    controllers.controllers.inserir_index(lista_ligada,elemento, index )
    LinkedList.traverse_list(lista_ligada)

def VNE(lista_ligada):
    contagem = controllers.controllers.verificar_numero_elementos(lista_ligada)
    print(f"O numero de elementos são {contagem}.")

def VP(lista_ligada, elemento):
    if controllers.controllers.verificar_pais(lista_ligada, elemento) == False:
       print(f"O país {elemento} não se encontra na lista.")
    else:
        print(f"O país {elemento} encontra-se na lista.")

def EPE(lista_ligada):
    controllers.controllers.eliminar_primeiro(lista_ligada)
    print(f"O primeiro país da lista foi eliminado com sucesso.")

def EUE(lista_ligada):
    controllers.controllers.eliminar_ultimo(lista_ligada)
    print(f"O ultimo país da lista foi eliminado com sucesso.")

def EP(lista_ligada,elemento):
    if controllers.controllers.verificar_pais(lista_ligada, elemento) == False:
       print(f"O país {elemento} não se encontra na lista.")
    
    else:
        controllers.controllers.eliminar_pais(lista_ligada,elemento)
        print(f"O país {elemento} ,foi eliminado com sucesso.")