count = 0
def hanoi(num, a, b, c):
    global count
    if num > 0:
        hanoi(num - 1, a, c, b)
        count = count + 1
        print('第', count, '次移動:')
        print(str(num) + "號盤：" + a + " --> " + c)
        print()
        hanoi(num - 1, b, a, c)

def main():
    num = eval(input("請輸入盤子數："))
    hanoi(num, 'A', 'B', 'C')
    print("搬運次數為",2 ** num - 1)

main()
