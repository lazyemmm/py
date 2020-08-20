"""
    有两种类型的域：类的变量和对象的变量。
        类变量：定义在class中且method外，为类和所有实例共享，包括public和private类型，调用方法: 类名.变量名 或者 实例名.变量名；
        实例变量：调用__init__(参数)方法去实例化对象时创建的变量，为当前实例所独享，调用方法: 实例名.变量名；
    类的变量由一个类的所有对象（实例）共享使用。只有一个类变量的拷贝，所以当某个对象对类的变量做了改动的时候，这个改动会反映到所有其他的实例上。
    对象的变量由类的每个对象/实例拥有。每个对象有自己对这个域的一份拷贝，即他们不是共享的。
"""
class Person:
    '''Represents a person.'''
    population = 3

    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name = name
        print('(Initializing %s)' %self.name)

        # when this person is created,he/she
        # adds to the population
        Person.population += 1
        print(self.population)

    def __del__(self):
        ''' I am dying. '''
        print('%s says bye.' % self.name)

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

print('____________')
print(Person.population)

"""
    说明：上例中population属于Person类，因此是一个类的变量。name变量属于对象（它使用self赋值）因此是对象的变量。
    记住：
    Python中所有的类成员（包括数据成员）都是公共的，所有的方法都是有效的。
    例外：你使用的数据成员名称以双下划线前缀比如__privatevar,Python的名称管理体系会有效地把它作为私有变量。
    这是一个惯例，如果某个变量只想在类或对象中使用，就应该以单下划线前缀。而其他的名称都将作为公共的，可以被其他类/对象使用。
"""