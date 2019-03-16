import random
if __name__ == '__main__':
    mlist=[i for i in range(0,random.choice(range(0,100)))]
    num=random.choice(range(0,100))
    if str(mlist).find(str(num))!=-1:
        print("该数字在列表中")
    else:
        print("该数字不在列表中")
   
    print(mlist)
    print(num)
