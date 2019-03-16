if __name__ == '__main__':
    with open(r"D:\1.jpg","rb") as f:
        with open(r"D:\3.jpg", "wb") as f2:

         while True:
            tlist=f.read(1024)
            f2.write(tlist)
            if len(tlist)==0:
                break


        print("拷贝完成")