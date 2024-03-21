###############################

def plus(a, b):  # a si b sunt parametrii (numele folosite pt argumentele unei functii)
    return a + b


plus(1, 2)  # 1 si 2 sunt argumentele ( argumentele sunt val parametrilor)


##################################################
# default arguments (parametrii cu val implicite)

def plus(a, b=2):
    return a + b


plus(1)  # daca nu specificam o valoare explicita pt b, atunci va lua val implicita 2
plus(1, 3)


################################################

# keyword arguments
def plus(a, b):
    return a + b


plus(a=1, b=2)
plus(b=2, a=1)  # specificand argumntele prin numele lor nu mai este necesar sa pastram ordinea


###################################################
# nr variabil de parametri
def plus(*args):  # *args convectie in python dar se poate numi orcum atat timp cat are steluta
    print(args)
    return sum(args)


plus(1, 2, 3)
plus(1)
plus(*[1, 2, 3])  # * se mai numeste unpacking


def plus(**kmargs):
    print(kmargs)
    return sum(kmargs.values())


plus(a=1, b=2)
plus(**{'a': 1, 'b': 2})


def plus(*args, **kwargs):
    print(args, kwargs)
    return sum(args) + sum(kwargs.values())


plus(1, 2, a=7, b=9)
plus(3)
plus(x=7, y=8)
plus()
