while True:
    a = int(input("나이를 입력하세요:"))
    if a in range(0,4):
        print("귀하는 유아등급이며 요금은 무료 입니다.")
        print("즐거운 시간 되십시오.")
    if a in range(4, 14):
        print("귀하는 어린이등급이며 요금은 2000원 입니다.")
        i=int(input("요금 유형을 선택하세요(1:현금,2:공원 전용 신용 카드):"))
        if i == 1:
            b = int(input("요금을 입력하세요:"))
            if b == 2000:
                print("감사합니다. 티켓을 발행합니다.")
            elif b < 2000:
                print("%s원이 모자랍니다." % (2000 - b))
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (b - 2000))
        if i == 2:
            print("%s원이 결제되었습니다. 감사합니다."%(2000*(9/10)))
    if a in range(14, 19):
        print("귀하는 청소년등급이며 요금은 3000원 입니다.")
        i=int(input("요금 유형을 선택하세요(1:현금,2:공원 전용 신용 카드):"))
        if i == 1:
            b = int(input("요금을 입력하세요:"))
            if b == 3000:
                    print("감사합니다. 티켓을 발행합니다.")
            elif b < 3000:
                print("%s원이 모자랍니다." % (3000 - b))
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (b - 3000))
        if i == 2:
            print("%s원이 결제되었습니다. 감사합니다."%(3000*(9/10)))
    if a in range(19, 60):
        print("귀하는 성인등급이며 요금은 5000원 입니다.")
        i=int(input("요금 유형을 선택하세요(1:현금,2:공원 전용 신용 카드):"))
        if i == 1:
            b = int(input("요금을 입력하세요:"))
            if b == 5000:
                    print("감사합니다 티켓을 발행합니다.")
            elif b < 5000:
                print("%s원이 모자랍니다." % (5000 - b))
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (b - 5000))
        if i == 2:
            print("%s원이 결제되었습니다. 감사합니다."%(5000*(9/10)))
    if a in range(60,66):
        print("귀하는 성인등급이며 요금은 5000원 입니다.")
        i = int(input("요금 유형을 선택하세요(1:현금,2:공원 전용 신용 카드):"))
        if i == 1:
            b = int(input("요금을 입력하세요:"))
            if b == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            elif b < 5000:
                print("%s원이 모자랍니다." % (5000 - b))
            else:
                print("감사합니다. 티켓을 발행하고 거스름돈 %s원을 반환합니다." % (b - 5000))
        if i == 2:
            print("%s원이 결제되었습니다. 감사합니다." %(5000*(85/100)))
    if a > 65 :
        print("귀하는 노인등급이며 요금은 무료 입니다")
        print("즐거운 시간 되십시오")