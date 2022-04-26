from models.LinkedList import LinkedList

def inserir_inicio(lista_ligada,elemento):
    LinkedList.insert_at_start(lista_ligada, elemento)
    return lista_ligada

def inserir_final(lista_ligada, elemento):
    LinkedList.insert_at_end(lista_ligada, elemento)
    return lista_ligada

def inserir_depois_de_outro_elemento(lista_ligada , novo, elemento):
    LinkedList.insert_after_item(lista_ligada , novo, elemento)
    return lista_ligada

def inserir_elemento_antes_de_outro(lista_ligada , novo, elemento):
    LinkedList.insert_before_item(lista_ligada , novo, elemento)
    return lista_ligada

def inserir_index(lista_ligada, elemento,index):
    LinkedList.insert_at_index(lista_ligada,elemento,index)
    return lista_ligada

def verificar_numero_elementos(lista_ligada):
    return LinkedList.get_count(lista_ligada)

def verificar_pais(lista_ligada, elemento):
    return LinkedList.search_item(lista_ligada, elemento)

def eliminar_primeiro(lista_ligada):
    return LinkedList.delete_at_start(lista_ligada)

def eliminar_ultimo(lista_ligada):
    return LinkedList.delete_at_end(lista_ligada)

def eliminar_pais(lista_ligada, elemento):
    return LinkedList.delete_element_by_value(lista_ligada, elemento)