# A(B) -> C
# A = Decorador
# B = Función a decorar
# C = Función Base decorada + nueva funcionalidad
# wraper significa envoltorio

def decorador(funcion): # A
    # funcion = B
    """Permite generar un decorador que añade funcionalidad a una función.

        args:
            funcion: La función que se va a decorar.
        returns:
            wrapper: La función decorada que añade funcionalidad antes y después de la llamada a la función original.
    """


    def wrapper(*args, **kwargs): # C
        print("Antes de llamar a la función")
        result =funcion(*args, **kwargs) # Llamada a la función original
        print("Después de llamar a la función")
        return result

    return wrapper 

@decorador # B
def hello_word():
    print("¡Hola, mundo!")

@decorador # B
def suma(a, b):
    return a + b

print(suma(5, 10))
print(
    decorador.__doc__  # Imprime la documentación del decorador
)

def palindromo(sentence):
        """
        Verifica si una frase es un palíndromo.

        Args:
            sentence (str): La frase a verificar.
        Returns:
            bool: True si la frase es un palíndromo, False en caso contrario.

        Examples:
        >>> palindromo("Anita lava la tina")
        True
        >>> palindromo("Hola mundo")
        False
        """
        sentence = sentence.lower().replace(" ", "")
        return sentence == sentence[::-1]

