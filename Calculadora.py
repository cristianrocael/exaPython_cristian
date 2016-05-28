
import os 
import time

def divi():
	print " "
	print "                 Bienvenido a la seccion de DIVISIONES"
	print "                ///////////////////////////////////////"
	time.sleep(1)
	print " "
	print "Por favor sigua las instrucciones:"
	print " "
	print "/////////////////////////////////"
	K= input("Ingrese el primer Valor: ")
	print " "
	L= input("Ingrese el segundo Valor : ")
	print " ////////////////////////////////"
	print " "
	print "       /////////////////////////////////////"
	print "       ///  El resultado de su retas es: ///"
	print "       ///        " +str(K/L)+"        ///"
	print " "
	time.sleep(1)
	print "Muchas gracias por utlizar la seccion DIVISIONES ahora "
	print "           sera regresado al menu principal "
	print " "
	time.sleep(2)
	print "                   +++++++++++++++++++++++++"
	time.sleep(0.8)
	print "                   +++++  HASTA LUEGO  +++++"
	time.sleep(0.8)
	print "                   +++++++++++++++++++++++++"
	time.sleep(5)
	os.system ("cls")
	inicio()
	inicio()
	inicio()


def multi():
	print " "
	print "          Bienvenido a la seccion de MULTIPLICACIONES"
	print "        ***********************************************"
	print " "
	time.sleep(1)
	print "sigua las instrucciones:"
	print " "
	print " *****************************"
	J= input("Ingrese su primer numero: ")
	print " "
	H= input("Ingrese su segundo numero: ")
	print " ***************************** "
	time.sleep(1)
	print "         *****************************************"
	print "         * El resultado de su multiplicacion es: *"
	print "         **********      "+ str(J*H)+"      *********"
	print "         *****************************************"
	time.sleep(3)
	print "Muchas gracias por utlizar la seccion MULTIPLICACIONES ahora "
	print "                sera regresado al menu principal "
	print " "
	time.sleep(2)
	print "                   +++++++++++++++++++++++++"
	time.sleep(0.8)
	print "                   +++++  HASTA LUEGO  +++++"
	time.sleep(0.8)
	print "                   +++++++++++++++++++++++++"
	time.sleep(5)
	os.system ("cls")
	inicio()
	inicio()
	inicio()

def resta():
	print " "
	print "                   Bienvenido a la seccion RESTA"
	print "                 ----------------------------------"
	print " "
	time.sleep(1)
	print "Por favor sigua las instrucciones:"
	print " "
	time.sleep(1)
	print " ------------------------------"
	D= input("Ingrese el primer Valor: ")
	print " "
	E= input("Ingrese el segundo Valor : ")
	print " ------------------------------"
	print " "
	time.sleep(2)
	print "       ---------------------------------------"
	print "       ---- El resultado de su restas es: ----"
	print "               ----------     " + str(D-E) + "     -------------"
	time.sleep(3)
	print "Muchas gracias por utlizar la seccion RESTAS ahora sera regresado"
	print "                      al menu principal "
	print " "
	time.sleep(2)
	print "                   +++++++++++++++++++++++++"
	time.sleep(0.8)
	print "                   +++++  HASTA LUEGO  +++++"
	time.sleep(0.8)
	print "                   +++++++++++++++++++++++++"
	time.sleep(5)
	os.system ("cls")
	inicio()
	inicio()

def suma():
	print " "
	print " "
	print "                   Bienvenido a la seccion de SUMAS"
	print "                 +++++++++++++++++++++++++++++++++++++"
	print " "
	print "Por favor sigua las instrucciones:"
	print " "
	time.sleep(3)
	print " "
	print " "
	print "++++++++++++++++++++++++++++++++++"
	A=input("ingrese su primer valor: ")
	print " "
	b=input("ingrese su segundo valor: ")
	print "++++++++++++++++++++++++++++++++++"
	print " "
	time.sleep(2)
	print "      El resusltado de su suma es: "
	print " +++++++++++++++++++++++++++++"
	print  "+++++++++  " + str (A+b) +"  +++++++++"
	print " +++++++++++++++++++++++++++++"
	print " "
	time.sleep(3)
	print "Muchas gracias por utlizar la seccion SUMAS ahora sera regresado"
	print "                      al menu principal "
	print " "
	time.sleep(2)
	print "                   +++++++++++++++++++++++++"
	time.sleep(0.8)
	print "                   +++++  HASTA LUEGO  +++++"
	time.sleep(0.8)
	print "                   +++++++++++++++++++++++++"
	time.sleep(5)
	os.system ("cls")
	inicio()



def eleccion():
	time.sleep(2)
	seleccion = raw_input("Escriba su NUMERO: ")
	if seleccion == "1":
		os.system ("cls")
		suma()
	elif seleccion=="2":
		os.system ("cls")
		resta()
	elif seleccion=="3":
		os.system ("cls")
		multi()
	elif seleccion=="4":
		os.system ("cls")
		divi()
	else:
		print " "
		print "Usted solo puede seleccionar numeros del 1-4 por favor"
		print "              Vuelva a intentarlo"
		time.sleep(2)
		os.system ("cls")
		inicio()
		



def inicio():
	os.system ("cls")
	print "*********************************************************************"
	print "********                     CALCULADORA                     ********"
	print "*********************************************************************"
	print   " "
	time.sleep(2)
	print " A continuacion se le presentaran las operaciones que usted puede "
	print "                   realizar en este programa"
	print " "
	print "**************************************"
	time.sleep(3)
	print "*****1       SUMAS               *****"
	time.sleep(1)
	print "*****2       RESTAS              *****"
	time.sleep(1)
	print "*****3       MULTIPLICACIONES    *****"
	time.sleep(1)
	print "*****4       DIVISIONES          *****"
	print "**************************************"
	time.sleep(2)
	print "Usted puede seleccionar la operacion escribiendo el numero que corresponde "
	print "    a cada una de las operacion por favor elija un numero del 1-4"
	print " "
	eleccion() 

inicio()
