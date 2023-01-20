import random
def simulate(p, limit):
    head = [0, 0]
    n = [0,0]
    thiscoin = 0
    for i in range(limit):
        result = random.random()
        if (result < p[thiscoin]):
            head[thiscoin]+=1
        n[thiscoin] +=1
        if (head[0] + 1)/ (n[0]+2) > (head[1]+1)/(n[1]+2):
            thiscoin = 0
        else:
            thiscoin = 1
    return result < p[thiscoin]

def printf():
    count = 0
    for i in range(1000):
        p = [random.random(), random.random()]
        if simulate(p, 100000):
            count += 1
    return count
print(printf())
