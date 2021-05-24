# 40725027 柳俞百

str1 = "請輸入至少4個數字以上的一串整數："
str2 = "您輸入的整數，排序過後的list是："
str3 = "您輸入的偶數個整數字串的二個中間值是："
str4 = "您輸入的奇數個整數字串的中間值是："
str5 = "你要再來一次嗎? (yes or no)"

while True:
    print(str1, end="")
    inputData = input().split()

    # 如果輸入的個數小於4個，則要求重新輸入
    if len(inputData) < 4:
        continue

    # 逐字檢查
    isNotInt = False
    for i in inputData:
        # 如果有非數字的輸入，則要求重新輸入
        # 如果有非整數的輸入，則要求重新輸入
        if not i.isdigit():
            isNotInt = True
            continue
    if isNotInt:
        continue

    # 轉整數陣列並重新排序
    intList = [int(i) for i in inputData]
    intList.sort()

    # 印出排序後陣列
    print("%s%s" % (str2, [i for i in intList]))

    # 陣列奇偶數判斷
    listCount = len(intList)
    if listCount % 2 == 0:
        # 偶數
        print("%s[%s, %s]" % (str3, intList[(listCount - 1) // 2], intList[listCount // 2]))
    else:
        # 奇數
        print("%s[%s]" % (str4, intList[(listCount - 1) // 2]))

    # 問答，如輸入 y 則再來一次，反之結束程式
    print(str5)
    answer = input()
    if answer == "y" or answer == "yes":
        continue
    else:
        break
