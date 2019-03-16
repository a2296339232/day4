if __name__ == '__main__':
 try:
    num = 5/0
 except ZeroDivisionError as e:
    pass
    print("ZeroDivisionError")
    print("除数为零")
