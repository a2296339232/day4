if __name__ == '__main__':
    num=input("输入一个字符")
    strr="123456789abcdefg"
    try:
     print(strr.index(num))
    except TypeError as e:
        print(strr)
        print("该字符不在字符串中")
    except ValueError as e:
        print(strr)
        print("该字符不在字符串中")
    else:
        print("该字符存在")