# ## Syntax von Dekoratoren
# @dekorator
# def my_function():
#     ...
#     # Inhalt der Funktion

# # Umgeschrieben:
# def my_function():
#     ...

# my_function = dekorator(my_function)

# def my_function(a,b):
#     print(a + b)

# my_function = greeting(my_function)
# my_function(1,2)

## Beispiel
def greeting(function):
    def wrapper_function():
        print("Eins")
        function()
        print("Zwei")
    return wrapper_function


## Umschreiben ohne Dekorator
def say_something():
    print("Hey ich sag was")

say_something = greeting(say_something)
say_something()

## Umschreiben mit Dekorator
@greeting
def say_something_else():
    print("Sag iwas anderes")

say_something_else()
