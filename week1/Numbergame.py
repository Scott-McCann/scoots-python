import random
def guess(int1=1,int2=1000):
    """return a random integer from between two integers
    default values:(int1 = 1, int2 = 2)
    """
    return random.randint(int1,int2)


def secretmaker(int1=1, int2=1001):
    """creates a list of numbers, returns random
    """
    numbers = list(range(int1,int2))
    secret = random.choice(numbers)

    return secret

f=secretmaker(1,1001)
g=guess(1,1000)


print(f)
print(g)
