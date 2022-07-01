import json
import requests
import redis

# API Request
data = requests.get("https://anapioficeandfire.com/api/books")
characterData = data.json()

# Redis config
redis = redis.Redis(
    host= "localhost",
    port= "6379"
)

redis.set("characterData", json.dumps(characterData, separators=(",", ":")))

# print(json.loads(redis.get("characterData")))

from logging import root
import os


class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato


class arbol():
    def __init__(self):
        self.root = None

    def insert(self, a, dato):
       
        if a == None:  
            a = node(dato)
            
        else:
            d = a.dato
            if len(dato) < len(d["name"]):
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato["name"]:
                return a.dato
            else:
                if len(dato) < len(a.dato["name"]):
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

    def height(self, a):
        # if a is None return 0
        if a == None:
            return 0
        # find height of left subtree
        hleft = self.height(a.left)
        # find the height of right subtree
        hright = self.height(a.right)
        # find max of hleft and hright, add 1 to it and return the value
        if hleft > hright:
            return hleft+1
        else:
            return hright+1

    def CheckBalancedBinaryTree(self, a):
        # if tree is empty,return True
        if a == None:
            return True
    # check height of left subtree
        lheight = self.height(a.left)
        rheight = self.height(a.right)

        print(abs(lheight-rheight))
    # if difference in height is greater than 1, return False
        if(abs(lheight-rheight) != 1 and abs(lheight-rheight) != -1 and abs(lheight-rheight) != 0):
            return False
    # check if left subtree is balanced
        lcheck = self.CheckBalancedBinaryTree(a.left)
    # check if right subtree is balanced
        rcheck = self.CheckBalancedBinaryTree(a.right)
    # if both subtree are balanced, return True
        if lcheck == True and rcheck == True:
            return True


tree = arbol()
for book in json.loads(redis.get("characterData")):
            tree.root = tree.insert(tree.root, book)

while True:

    print("Arbol ABB")
    opc = input("\n1.-Ver lista de libros (nombre) \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-balance \n7.-Salir \n\nElige una opcion -> ")

    if opc == '1':
        for book in json.loads(redis.get("characterData")):
            print(book["name"])

    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")

        if tree.buscar(nodo, tree.root) == None:
            print("\nNodo no encontrado...")
        else:
            print("\nNodo encontrado -> ", tree.buscar(nodo, tree.root), " si existe...")
    elif opc == '6':

        if tree.CheckBalancedBinaryTree(tree.root):
            print("El arbol esta balanceado")
        else:
            print("El arbol no esta balanceado")

    elif opc == '7':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()

# DATA

# A Game of Thrones
# A Clash of Kings
# A Storm of Swords
# The Hedge Knight
# A Feast for Crows
# The Sworn Sword
# The Mystery Knight
# A Dance with Dragons
# The Princess and the Queen
# The Rogue Prince