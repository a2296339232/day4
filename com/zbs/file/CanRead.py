if __name__ == '__main__':
    f = open(r"d:/test.txt","w")

    len=f.write("吼吼吼吼全给党")
    print(len)

    f.close()

    ff=open(r"d:/test.txt","r")