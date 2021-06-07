again = True

while again:
    intArray = {}
    Count = 1
    while Count <= 2:
        print("請輸入第%x個整數list(至少5個數字)：" % Count, end="")
        inputStr = input().split()
        isCorrect = True
        if len(inputStr) >= 5:
            for a in inputStr:
                if not a.isdigit():
                    isCorrect = False
                    break
            if isCorrect:
                intArray[Count - 1] = [int(i) for i in inputStr]
                Count += 1

    print("您輸入的整數list分別是：%s與%s" % ([i for i in intArray[0]], [i for i in intArray[1]]))
    mergeArray = intArray[0] + intArray[1]
    print("合併過的整數list是：%s" % [i for i in mergeArray])
    sortArray = sorted(mergeArray)
    reverseSortArray = sorted(mergeArray, reverse=True)
    print("合併並由小到大排序的整數list是：%s" % [i for i in sortArray])
    print("合併並由大到小排序的整數list是：%s" % [i for i in reverseSortArray])

    print("你要再玩一次嗎? (yes or no)")
    againCheck = input().upper()
    again = againCheck[0] == "Y"
