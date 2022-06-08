# Función encargada de calcular el total de la entrada con respecto a la edad.
def  calcular_total ( edad ):
    si  edad  <  4 :
        totales  =  0

    elif  edad  >= 4  y  edad  <  18 :
        totales  =  3500

    elif  edad  >=  18 :
        totales  =  8000
    
    # Se devuelve el total
    devolución  total

def  principal ():
    
    print ( 'EJERCICIO tres: \n ' )
    
    mientras que  es cierto :

        # Menú que se muestra al usuario para calcular la edad del cliente y calcular el total.
        print ( 'Bienvenidos a la sala de juegos: \n \n ' )
        print ( '1 -> Ingreso del cliente. \n ' )
        print ( '2 -> Salir. \n ' )

        # Se verifica que la opción sea válida.
        prueba :
            opcion  =  int ( input ( 'Ingrese el número correspondiente a la opción: ' ))
            imprimir ( ' \n ' )
        excepto :
            print ( 'Ingrese una opcion valida!! \n ' )
            Seguir

        si  opcion  ==  1 :
            
            # Se verifica que la edad sea válida.
            prueba :
                edad  =  int ( input ( 'Ingrese la edad del cliente: ' ))
            excepto :
                print ( 'Ingrese una edad válida!!' )

            # Se muestra por pantalla el total a pagar por el cliente.
            print ( 'El total a pagar por la entrada es: $' + str ( calcular_total ( edad )) + ' \n ' )

        # Se verifica la opción que permite salir del programa.
        elif  opcion  ==  2 :
            salir ()

si  __nombre__  ==  "__principal__" :
    principal ()