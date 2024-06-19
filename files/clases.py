
class Dog():
    num_dog_objects = 0
    def __init__(self, name, age) :
        self. name = name
        self.age = age
        Dog.num_dog_objects += 1

    @classmethod # Este es un método de clase
    def increase_num_dog_objects(cls) :
        cls.num_dog_objects += 1


dogl = Dog("rocky", 4)
dog2 = Dog("fifi", 5)
dog3 = Dog("baaron", 6)

print(dogl.name + ' ' +str(dogl.age))
print(dog2.name + ' ' + str(dog2.age))
print(dog3.name + ' ' + str(dog3.age))

print(dog2.num_dog_objects) #3 Imprime error
Dog.increase_num_dog_objects()
print(Dog.num_dog_objects) # 4 # calling our class method Este funciond