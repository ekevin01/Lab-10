#the authors names are Isa Grace Guthrie and Ellen Kevin and Camryn Hurley
d={'a':1,'b':2,'c':3}
h={1:'a',2:'b',3:'c'}
def my_get_method(x,y,z):
    for char in z:
        if char==x:
            print(z[x])
            break
        else:
            print(y)
            break

my_get_method('a',5,d)
my_get_method('i',14,d)
my_get_method(3,'seven',d)
