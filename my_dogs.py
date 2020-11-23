import dog # we need to specify exactly what we want

my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()


my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)

my_other_dogs = dog.Dog("Bear", "Cat")
my_dog.bark()

my_other_doggie = dog.Dog("MArk", "poodle")
my_other_doggie.sit()

my_other_doggies = dog.Dog("MAx", "Wolf")
my_other_doggies.rollover()