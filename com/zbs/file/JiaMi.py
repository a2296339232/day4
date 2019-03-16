def jiaMi():
    file1 = input("输入拷贝文件所在路径及文件名")
    file2 = input("输入拷贝至文件夹，以及拷贝后的名称")
    pass1= input("输入加密密码")
    print(file1)
    print(file2)
    with open(file1,"rb") as f:
        with open(file2, "wb") as f2:
            mm=f.read(1)
            mm=int(mm)
            for i in pass1:
                mm=mm^ord(i)

            f2.write(bytes(mm))
            while True:
                tlist = f.read(1024)
                f2.write(tlist)
                if len(tlist) == 0:
                    break
            print("加密\解密完成")







if __name__ == '__main__':
    jiaMi()





