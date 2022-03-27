apple = []


def apple_program() :
    value = input()
    flag = value.isnumeric()



    if not flag :
        print("잘못 입력하셨습니다.")
        apple_program()

    value = int(value)

    if value == 0 :
        print("바구니 개수는 0개 입니다")
    elif value % ? == 0:
        print(value // 10)
    else :
        print(value // 10 + 1)
        apple_program()

apple_program()
