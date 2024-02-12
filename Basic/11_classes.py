### Classes ###

class MyEmptyPerson:  #La primera letra de cada palabra en MAYUS 
    pass

print(MyEmptyPerson())
print(MyEmptyPerson)



class Person:
    def __init__(self, name, surname): #siempre debe haber un self. Se refiere a si mismo
        self.name = name
        self.surname = surname 

my_person = Person("Unai", "Munoz")
print(my_person.name, my_person.surname)

class People:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" #propiedad pública
        self.__name = name  #propiedad privada
    def get_name():
        return self.__name

    def walk (self):
        print(f"{self.full_name} Es tá caminando")

myy_person = People("Unai", "Munoz")
print(myy_person.full_name)
myy_person.walk()

my_other_person = People("Unai", "Munoz", "Mongolardo")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Tyson Rodriges el manolardo"
print(my_other_person.full_name)


my_other_person.full_name = 123
print(my_other_person.full_name)

