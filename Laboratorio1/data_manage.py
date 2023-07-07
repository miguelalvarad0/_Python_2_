from datetime import datetime
import time

#borra todo el contenido presente en el archivo 'Datalog.txt'
def limpiar_datalog():
    file = open("log.txt", "w")
    file.write("")
    file.close()
  
#la funcion recibe una operacion y la almacena en el archivo de texto.
def guardar_operacion(Operacion,Resultado):
    input("Presione Enter para guardar y volver al Menu Principal...")#espera la tecla enter para continuar
    print("La operación esta siendo exportada al datalog....... 20%")#notificacion de progreso en almacenamiento de datos.
    time.sleep(1)#detiene la ejecucion del codigo por un segundo
    file = open("log.txt","a") #abre el archivo de texto y agrega contenido al final de este (en una nueva linea)
    file.write("--------------------\n") #escribe contenido en el archivo de texto
    now = datetime.now() #guarda la fecha y hora exacta en una variable 
    string_aux= "Date: " + str(now.day) +"/"+str(now.month)+"/"+ str(now.year)+ "  Time: "+str(now.hour)+":"+ str(now.minute)+"\n"
    file.write(string_aux) #escribe fecha y hora en el archivo de texto con un formato adecuado.

    #segun el tipo de operacion se corren distintas intrucciones para escribir los calculos y resultados en el archivo de text.
    if (Operacion=='Seno'):
        file.write("\nOperación: ")
        file.write(str(Operacion))
        file.write("  Resultado: ")
        file.write(str(Resultado))

    elif (Operacion=='Coseno'):
        file.write("\nOperación: ")
        file.write(str(Operacion))
        file.write("  Resultado: ")
        file.write(str(Resultado))

    elif (Operacion=='Tangente'):
        file.write("\nOperación: ")
        file.write(str(Operacion))
        file.write("  Resultado: ")
        file.write(str(Resultado))
    else:
        return ''

    #escribir en el archivo de respaldo: la operacion y el resultado de la misma.
    print("La operación esta siendo exportada al datalog....... 74%")#notificacion de progreso en copia de datos al archivo.
    time.sleep(2)#detiene la ejecucion del programa por 2 segundos para ganar atencion en el ultimo comentario impreso.
    
    file.write("\n")
    file.close()
    print("La operación ha sido EXPORTADA EXITOSAMENTE!........ 100%\n")

