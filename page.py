# ERROR code
# CODE001 : 압력한 테이터가 정수형이 아닙니다
# CODE002 : 압력한 데이터가 정수형 이지만 , 1보다 작은 0 또ㅡㄴㄴ 읍수입니다

basket = 10

def program() :
    value = input("사과는 몇개이나요")
    int_flag = value.isnumeric()

    if not int_flag :
        print("[CODE001]올바른 숫자를 입력해주세여")
        program()

    value = int(value)
    if value < 1 :
        print("[CODE002]올바른 숫자를 입력해주새요")
        program()

    need_basket = value / basket + 1 if value % basket > 0 else value / basket
    need_basket = int(need_basket)

    print(f"필요한 바구나는 {need_basket}개 입니다")

program()