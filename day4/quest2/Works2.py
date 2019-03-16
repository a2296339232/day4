import  random
def getSet():
    aset={random.choice(range(0,1000)) for i in range(0,15)}
    bset={random.choice(range(0,1000)) for i in range(0,10)}
    anset= aset | bset
    print(anset)
    return  anset


if __name__ == '__main__':
    mdict={1:getSet}
    print(mdict[1]())