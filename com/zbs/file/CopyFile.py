def copyFile():
    file1 = input("输入拷贝文件所在路径及文件名")
    file2 = input("输入拷贝至文件夹，以及拷贝后的名称")
    print(file1)
    print(file2)
    with open(file1,"rb") as f:
        with open(file2, "wb") as f2:
         while True:
            tlist=f.read(1024)
            f2.write(tlist)
            if len(tlist)==0:
                break
        print("拷贝完成")

if __name__ == '__main__':
    copyFile()