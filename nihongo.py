from random import randrange
from collections import Counter
import time

hiragana = [
    [["a", "あ"],  ["i", "い"],  ["u", "う"],  ["e", "え"],  ["o", "お"]],
    [["ka", "か"], ["ki", "き"], ["ku", "く"], ["ke", "け"], ["ko", "こ"]],
    [["sa", "さ"], ["shi", "し"], ["su", "す"], ["se", "せ"], ["so", "そ"]],
    [["ta", "た"], ["chi", "ち"], ["tsu", "つ"], ["te", "て"], ["to", "と"]],
    [["na", "な"], ["ni", "に"], ["nu", "ぬ"], ["ne", "ね"], ["no", "の"]],
    [["ha", "は"], ["hi", "ひ"], ["fu", "ふ"], ["he", "へ"], ["ho", "ほ"]],
    [["ma", "ま"], ["mi", "み"], ["mu", "む"], ["me", "め"], ["mo", "も"]],
    [["ya", "や"], ["yu", "ゆ"], ["yo", "よ"]],
    [["ra", "ら"], ["ri", "り"], ["ru", "る"], ["re", "れ"], ["ro", "ろ"]],
    [["wa", "わ"], ["wo", "を"]],
    [["n", "ん"]],
]

katakana = [
    [["a", "ア"],  ["i", "イ"],  ["u", "ウ"],  ["e", "エ"],  ["o", "オ"]],
    [["ka", "カ"], ["ki", "キ"], ["ku", "ク"], ["ke", "ケ"], ["ko", "コ"]],
    [["sa", "サ"], ["shi", "シ"], ["su", "ス"], ["se", "セ"], ["so", "ソ"]],
    [["ta", "タ"], ["chi", "チ"], ["tsu", "ツ"], ["te", "テ"], ["to", "ト"]],
    [["na", "ナ"], ["ni", "ニ"], ["nu", "ヌ"], ["ne", "ネ"], ["no", "ノ"]],
    [["ha", "ハ"], ["hi", "ヒ"], ["fu", "フ"], ["he", "ヘ"], ["ho", "ホ"]],
    [["ma", "マ"], ["mi", "ミ"], ["mu", "ム"], ["me", "メ"], ["mo", "モ"]],
    [["ya", "ヤ"], ["yu", "ユ"], ["yo", "ヨ"]],
    [["ra", "ラ"], ["ri", "リ"], ["ru", "ル"], ["re", "レ"], ["ro", "ロ"]],
    [["wa", "ワ"], ["wo", "ヲ"]],
    [["n", "ン"]],
]

testtype = [
    [["hiragana", "hira", "hi", "h"], hiragana],
    [["katakana", "kata", "ka", "k"], katakana]
]

print("  Welcome to Hiragana Trivia! ")
print("  Hiragana / Katakana / Both  ")
print("  Please enter h, k or b  ")
typeinput = input().lower()
print("a/ka/sa/ta/na/ha/ma/ya/ra/wa/n")
startfrom = input("Choose from: ").lower()
stopat    = input("to: ").lower()

startindex = -1
stopindex = -1
for i in range(len(hiragana)):
    if(startfrom==hiragana[i][0][0]):
        startindex = i
    if(stopat==hiragana[i][0][0]):
        stopindex = i

if( startindex == -1 or stopindex == -1 ):
    print("Can't seem to find list.")
    exit()

questionlist = []
for el in testtype:
    if ( typeinput == "both" or typeinput == "b" ):
        for i in range(startindex,stopindex+1):
            for b in hiragana[i]:
                questionlist.append(b)
            for c in katakana[i]:
                questionlist.append(c)
        break
    else:
        for a in el[0]:
            if ( a == typeinput ):
                for i in range(startindex,stopindex+1):
                    for b in el[1][i]:
                        questionlist.append(b)
                break

if(len(questionlist) == 0):
    print("Can't seem to find list.")
    exit()

wrongcount = 0
wronglist = []
wronglistromanji = []
testlist = questionlist
starttime = time.time()
while True:
    if(len(testlist)==0):
        endtime = time.time()
        break
    curquestindex = randrange(len(testlist))
    print("What is this :" + testlist[curquestindex][1] )
    answ = input().lower()
    if( answ == testlist[curquestindex][0] ):
        testlist.remove(testlist[curquestindex])
        print("Correct!!!")
    else:
        print("Wrong, please try again")
        wronglist.append(testlist[curquestindex][1])
        wronglistromanji.append(testlist[curquestindex][0])
        wrongcount += 1

print("Time elapsed : " + str(round(endtime-starttime, 2)) + " seconds")
print("You have finish from {} to {} with {} mistakes".format(startfrom.upper(),stopat.upper(),wrongcount))
if(wrongcount!=0):
    print("Most mistake is :", end='')
    result = [item for items, c in Counter(wronglist).most_common()
        for item in [items] * c]
    resultromanji = [item for items, c in Counter(wronglistromanji).most_common()
        for item in [items] * c]
    result = list(dict.fromkeys(result))[:5]
    resultromanji = list(dict.fromkeys(resultromanji))[:5]
    for i in range(len(result)):
        print(" " + result[i] + "(" + resultromanji[i] + ")", end="")
