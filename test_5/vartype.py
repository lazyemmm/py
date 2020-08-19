"""
    有两种类型的域：类的变量和对象的变量。
    类的变量由一个类的所有对象（实例）共享使用。只有一个类变量的拷贝，所以当某个对象对类的变量做了改动的时候，这个改动会反映到所有其他的实例上。
    对象的变量由类的每个对象/实例拥有。每个对象有自己对这个域的一份拷贝，即他们不是共享的。
"""
class Person:
    '''Represents a person.'''
    population=0

    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name = name
        print('(Initializing %s)' %self.name)

        #when this person is created,he/she
        #adds to the population
        Person.population+=1

    def __del__(self):
        '''I am dying.'''
        print('%s says bye.' %self.name)

        Person.population -= 1

        if Person.population == 0:
            print('I am the last one.')
        else:
            print('There are still %d people left.'%Person.population)

    def sayHi(self):
        '''Greeting by the person.

         Really,that's all it does.'''
        print('Hi,my name is %s.'%self.name)

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.'% Person.population)

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()