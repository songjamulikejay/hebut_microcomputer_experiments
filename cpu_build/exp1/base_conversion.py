# 计224 汤太阳
def two_to_ten(x):
    length = len(x)
    y = 0
    for i in x:
        length=length-1
        y= y+ int(i)*2**length
    return y

def eight_to_ten(x):
    length = len(x)
    y = 0
    for i in x:
        length=length-1
        y= y+ int(i)*8**length
    return y

def sixteen_to_ten(x):
    length = len(x)
    y = 0
    for i in x:
        length=length-1
        if i == "a" or "A":
            y = y + 10 * 16 ** length
        if i == "b" or "B":
            y = y + 11 * 16 ** length
        if i == "c" or "C":
            y = y + 12 * 16 ** length
        if i == "d" or "D":
            y = y + 13* 16 ** length
        if i == "e" or "E":
            y = y + 14 * 16 ** length
        if i == "f" or "F":
            y = y + 15 * 16 ** length
        else:
            y= y+ int(i)*2**length
    return y

def ten_to_two(x):
    c = ""
    while x >= 1 :
        y = x % 2
        x = x // 2
        c = str(y) + c
    return c
def ten_to_eight(x):
    c = ""
    while x>=1 :
        y = x % 8
        x = x // 8
        c = str(y) + c
    return c
def ten_to_sixteen(x):
    c = ""
    while x >= 1:
        y = x % 16
        x = x // 16
        # print(x)
        if y == 10:
            c = 'A' + c
        if y == 10:
            c = 'B' + c
        if y == 10:
            c = 'C' + c
        if y == 10:
            c = 'D' + c
        if y == 10:
            c = 'E' + c
        if y == 10:
            c = 'F' + c
        else:
            c = str(y) + c

    return c

def switch(value,v):
    switcher = {
        '2':two_to_ten(v),
        '8':eight_to_ten(v),
        '10':v,
        '16':sixteen_to_ten(v)
    }
    return switcher.get(value,"输入错误")
def switch2(value,v):
    switcher = {
        '2' :ten_to_two(v),
        '8':ten_to_eight(v),
        '10':v,
        '16':ten_to_sixteen(v),
    }
    return switcher.get(value,"输入错误")

def main():
    while(1):
        print("请输入一个数字")
        a = input()
        print("请输入数字的格式（2，8，10，16）")
        b = input()
        print("请输入要转换的格式（2，8，10，16）")
        c = input()
        p = int(switch(b,a))
        result = switch2(c,p)
        print(result)
if __name__ == '__main__':
    main()


