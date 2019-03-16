if __name__ == '__main__':
    #实现按照字符串的长度
    myList = ['青海省', '内蒙古自治区', '西藏自治区', '新疆维吾尔自治区', '广西壮族自治区','1',\
              '3']
    myList1 = sorted(myList, key=lambda i: len(i))
    print(myList1)