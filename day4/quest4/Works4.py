def getHuiWen():
    num=input("请输入一串数列")
    try:
        num=int(num)
    except Exception as e:
        print("转换有误，您输入的数列不正确")
    else:
        if num%2==0:
            print("该数字不是回文数")
        else:
            svm=len(str(num))//2+1
            if str(num)[0:svm]==str(num)[:-svm-1:-1]:
                print("回文数")

if __name__ == '__main__':
    getHuiWen()