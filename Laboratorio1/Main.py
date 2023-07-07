import os
import time
import datetime
from Trig_Class import Trig
from data_manage import limpiar_datalog  
from data_manage import guardar_operacion


Trigo = Trig()
Seno = Trig.sin()
Cos = Trig.cos()
Tang = Trig.tan()


#print(f"El Seno de pi es: {Seno}")
#print(f"El Coseno de pi es: {Cos}")
#print(f"La Tangente de pi es: {Tang}")

  
def imprimir_menu(): #Imprime menu de opciones en pantalla.
    print("            CALCULADORA")
    print("Digite 1 para calcular el seno de Pi")
    print("Digite 2 para calcular el coseno de Pi")
    print("Digite 3 para calcular la tangente de Pi")
    print("Digite 4 para salir del programa\n")

def main_calculadora(Seno, Cos, Tang): 
    imprimir_menu()
    select = int(input(" "))
    if select == 1:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        print("\nSENO")
        print(f"El Seno de pi es: {Seno}")
        guardar_operacion(Operacion='Seno',Resultado=Seno) #hace un backup de la solucion de la operacion en un archivo de respaldo
        time.sleep(2.5) #detiene la ejecucion del codigo por unos instantes 
        os.system('clear')
        main_calculadora(Seno,Cos,Tang)
    elif select == 2:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        print("\nCOSENO")
        print(f"El coseno de pi es: {Cos}")
        guardar_operacion(Operacion='Coseno',Resultado=Cos) #hace un backup de la solucion de la operacion en un archivo de respaldo
        time.sleep(2.5) #detiene la ejecucion del codigo por unos instantes 
        os.system('clear')
        main_calculadora(Seno,Cos,Tang)
    elif select == 3:
        os.system('clear')  #limpia la terminal para imprimir desde cero en ella
        print("\nTANGENTE")
        print(f"El Tangente de pi es: {Tang}")
        guardar_operacion(Operacion='Tangente',Resultado=Tang) #hace un backup de la solucion de la operacion en un archivo de respaldo
        time.sleep(2.5) #detiene la ejecucion del codigo por unos instantes 
        os.system('clear')
        main_calculadora(Seno,Cos,Tang)  
    else:
        return""   #fin del programa

#Limpia el archivo de respaldo y ejecuta la funcion principal / Muestra opciones en pantalla y espera seleccion del usuario.
limpiar_datalog()
main_calculadora(Seno,Cos,Tang)

