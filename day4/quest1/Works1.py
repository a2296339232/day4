def checkSex(strr="贝奥兰迪",sex="男"):
    mdict={"男":False,"Man":False,"man":False,"1":False}

    if mdict[sex]:
        print("欢迎您:", strr, "女士")
    else:
        print("欢迎您:", strr, "先生")

