class Person:
    '''represents a person'''
    population =0

    def __init__(self,name):
        '''initializes the person's data.'''
        self.name = name
        print('initializing %s' %self.name)

        Person.population +=1

    def __del__(self):
        print('%s says bye' %self.name)
        Person.population-=1
        if Person.population ==0:
            print('last one')
        else:
            print('there are still %d people left' %Person.population)

    def sayhi(self):
        print('hi,%s' %self.name)

    def howmany(self):
        if Person.population == 1:
            print('i am the only person here')
        else:
            print('we have %d persons here' %Person.population)



swaroop = Person('Swaroop')
swaroop.sayhi()
swaroop.howmany()

kalam = Person('Kalam')
kalam.sayhi()
kalam.howmany()