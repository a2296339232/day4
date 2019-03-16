class MyExcept (ZeroDivisionError):
    pass
    def show(self):
        print("当前错误为Exception")

if __name__ == '__main__':
    try:
        num=5/0
    except Exception as e:
        print("错误")

    except MyExcept as e:
        print("MyExcept")
