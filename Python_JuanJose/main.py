## ---------------------------------------
## ---- Ejercicio 1 ----
## ---------------------------------------
print("hola mundo")

# ---- Datos primitivos ----
#1. String
texto = "campus"
print(texto)
print(type(texto))
#2. Int
numeroEntero = 1
print(numeroEntero)
#3. Float
numeroDecimal = 3.1
print(numeroDecimal)
#4. Double
numeroDesimalLargo = 3.14167582737283
print(numeroDesimalLargo)
#5. Boolean
boolean = True
print(boolean)
# ---- Entradas parte del usuario ----
entradaUsuarioNumero = str(input("Ingresa tu nombre:"))
print("tu nombre es:" ,entradaUsuarioNumero)
# ---- Entradas parte del usuario con definicion de tipo de dato primitivo ----
entradaUsuarioNumero = input("ingresa tu edad:")
numeroFinal =  int(entradaUsuarioNumero)
print("tu edad es: " , numeroFinal)
# ---- ciclos ----

#ciclo for
for i in range(5,10,2): #for contador in range (desde,hasta,pasos):
    print (i)

    #ciclo"while"
    boleanito = True
    while boleanito == True: # while condicion a_cumplir 
        print("sigo vivo")
        boleanito = False

    # ---- Condicionales ----
    texto1 = "campus"
    if texto1 == "campus":
        print("soy campus")
    else:
        print("no soy campus")

        # ------- Funciones -----------


        # ---- Funciones con retorno con parametros ----

        def suma(a,b):   ##def(comando para iniciar una funcion), nombre funcion, (parametros)
            return a + b   ##return es el comando para retornar un valor
        result = suma(1,2)
        print (result)

        # ---- Funcion sin retorno sin parametros ----

        def saludo():
         print("hola invitado")
         saludo()

         # ---- Funcion sin retorno con parametros ----
         

         def saludoNombre(name):
             print("hola usuario/a" + name + "!" )

             name = input ("ingrese su nombre: ")

             saludoNombre(name)

             # ---- Funcion con retorno sin parametros ----

             def resultado():
                 resultadofin = a + b
                 return resultadofin
             
             a = float(input("digite el primer numero: "))
             b = float(input("digite el segundo numero: "))

             print("el resultado de la suma es: ",resultado())


## Desarrollado por JUAN JOSE ROJAS PEÑA - 1096701688