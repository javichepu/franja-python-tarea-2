# Funcion para contar el caracter contenido en la frase.
def  contar_caracteres ( letra , frase ):
    # Se inicia el contador en 0
    contador  =  0

    para  char  en  frase :
        si  letra  ==  char :
            contador  += 1
    
    volver  contador

def  principal ():

    print ( "EJERCICIO 1 \n " )

    # Se lee la frase por teclado y se comprueba que tenga contenido.
    mientras que  es cierto :
        frase  =  entrada ( 'Escriba una frase: ' )
        
        si  len ( frase ) >  0 :
            descanso

        print ( 'Por favor, escribe una frase válida...' )
    
    # Se lee la letra por teclado y se comprueba que tenga largo 1, es decir, sólo sea 1 carácter.
    mientras que  es cierto :
        letra  =  input ( 'Escriba una letra: ' )

        si  len ( letra ) ==  1 :
            descanso

        print ( 'Ingrese sólo una letra!!!' )

    print ( 'La cantidad de letras "' +  letra  + '" es: ' , contar_caracteres ( letra , frase ))

si  __nombre__  ==  "__principal__" :
    principal ()
