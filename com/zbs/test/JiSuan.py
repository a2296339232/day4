if __name__ == '__main__':
    print("输入两个数字，计算除法")
    print("输入q退出程序")
    while True:
        print("\t")
        fnum=input("第一个数字")
        if fnum=="q":
            break
        snum=input('输入第二个数字')
        if snum=='q':
            break
        try:
            res=int(fnum)/int(snum)

        except Exception as e:
            print("输入有误,除数不能为0")
        else:
            print("结果为：{snum}".format(snum=snum))



