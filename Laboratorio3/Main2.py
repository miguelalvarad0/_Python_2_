import os
import time
import requests as req 


def getPageData():
    url = "https://api.chucknorris.io/jokes/random"
    response = req.get(url)
    #return response.json()[id]['name']
    return response.json()['value']


def getPageCategories():
    url = "https://api.chucknorris.io/jokes/categories"
    response = req.get(url)
    #return response.json()[id]['name']
    return response.json()


def getCategoryJoke(category):
    url = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = req.get(url)
    #return response.json()[id]['name']
    return response.json()['value']


def imprimir_menu(): #Imprime menu de opciones en pantalla.
    print("            CHUK NORRIS JOKES")
    print("Digite 1 para ver un chiste completamente aleatorio")
    print("Digite 2 para ver las categorias de chiste disponibles")
    print("Digite 3 para ver un chiste de una categoria especifica")
    print("Digite 4 para salir del programa\n")

def main(): 
    imprimir_menu()
    select = int(input(" "))
    if select == 1:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        data = getPageData()
        print(data)
        time.sleep(1) #detiene la ejecucion del codigo por unos instantes 
        input("press any key to continue........")
        os.system('clear')
        main()
    elif select == 2:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        data = getPageCategories()
        print(data)
        time.sleep(1) #detiene la ejecucion del codigo por unos instantes 
        input("press any key to continue........")
        os.system('clear')
        main()
    elif select == 3:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        categ = (input("Type a category:  "))
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        data = getCategoryJoke(categ)
        print(data)
        time.sleep(1) #detiene la ejecucion del codigo por unos instantes 
        input("press any key to continue........")
        os.system('clear')
        main()  
    else:
        return""   #fin del programa


main()