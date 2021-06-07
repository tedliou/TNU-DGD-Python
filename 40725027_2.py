import re
again = True
while again:
    regexStr = ""
    while True:
        print("請輸入一段字串(長度至少為10)：", end="")
        inputStr = input()

        if len(inputStr) >= 10:
            regex = re.match("^[a-zA-Z0-9. ]+$", inputStr)
            if regex is not None:
                regexStr = regex.group()
                break
        else:
            break

    repeatChar = ""
    repeatCharIndex = -1
    for i in regexStr:
        if not re.match("^[. ]+$", i):
            findArray = re.findall(i, regexStr)
            if len(findArray) == 1:
                repeatChar = i
                repeatCharIndex = regexStr.find(i)
                break
    if repeatChar == "":
        print("沒有不重複的字元")
    else:
        print("您輸入的字串中，第一個沒有重複的字元是 %s，他的索引是 %s" % (repeatChar, repeatCharIndex + 1))

    print("你要再玩一次嗎? (yes or no)")
    againCheck = input().upper()
    again = againCheck[0] == "Y"
