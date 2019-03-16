import day4.quest1.Works1 as works1
import day4.quest2.Works2 as works2
import day4.quest3.Works3 as works3
import day4.quest4.Works4 as works4
if __name__ == '__main__':
    mdict = {
        1:"输入用户姓名及性别，然后给出下列的提示",
        2:"随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
        4:"从键盘输入一行字符串，判断是否是回文数",
        0:"退出"
    }
    mfdict = {
        1: works1.checkSex,
        2: works2.getSet,

        4: works4.getHuiWen
    }
    while True:

        for i in mdict.keys():
            print(i,":",mdict[i])

        switch=int(input("请选择你要执行的函数"))
        if switch==0:
            break

        mfdict[switch]()
        print()
