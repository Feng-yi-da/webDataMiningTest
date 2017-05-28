# coding=utf-8
# coding=gbk


# 运用朴素贝斯进行新闻分类

import sys
import Txt
import re
import JieBa
import math

# 朴素贝叶斯
def naiveBayesian(A, B, N):
    PAB = math.log(float((float(A) / float(B)) * (1.0 / float(N))),2)
    return PAB


# froPath 根目录
# froPath = "/home/yida/Desktop/webDataMiningTest/"
# clas 分类类型的数组
# clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
# clas = [ "Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]
def classificate(froPath, clas, txt):
    reload(sys)
    sys.setdefaultencoding('gbk')
    # 各类的训练集
    classTrainingSet = [dict() for i in clas]
    # 总训练集
    taltollTrainingSet = dict()
    # 各类训练集的词数
    classWordNumber = [int() for i in clas]
    # 总词数
    taltallWordNumber = 0
    # 读取各类的训练集
    for i in range(len(clas)):
        # 读取文本,一次读取一行,
        classs = clas[i]
        try:
            file = open((froPath + "/TrainingSet/" + classs + "/" + classs + "TrainingSet.txt"), 'r')
            line = file.readline()
            patterm = re.compile("(.+?)\\\(\d+)")
            while line:
                match = patterm.search(line)
                if match:
                    if match.group(1) != "":
                        if classTrainingSet[i].get(match.group(1)):
                            print clas[i] + "读取词频出错 " + match.group(1)
                        else:
                            classTrainingSet[i][match.group(1)] = int(match.group(2))
                            classWordNumber[i] = classWordNumber[i] + int(match.group(2))

                line = file.readline()
        except:
            print "读取 " + classs + " 出错"
            print "1"
            Txt.writeAll('a', froPath + "/ReadError.txt", "classification " + classs + "TrainingSet.txt\n")
            # print classs + "读取成功"

    # 读取总的训练集
    try:
        file = open((froPath + "/TrainingSet/" + "TaltollTrainingSet.txt"), 'r')
        line = file.readline()
        patterm = re.compile("(.+?)\\\(\d+)")
        while line:
            match = patterm.search(line)
            if match:
                if match.group(1) != "":
                    if taltollTrainingSet.get(match.group(1)):
                        print "TaltollTrainingSet" + "读取词频出错" + match.group(1)
                    else:
                        taltollTrainingSet[match.group(1)] = int(match.group(2))
                        taltallWordNumber = taltallWordNumber + int(match.group(2))

            line = file.readline()
    except:
        Txt.writeAll('a', froPath + "/ReadError.txt", "classification " + classs + "TaltollTrainingSet.txt\n")

    #
    #
    #
    #
    # 测试代码
    # clas = ["Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]
    # froPath = "C:/Users/yida/Desktop/webDataMiningTest/"
    fromnum = 1611
    endnum = 1990
    tatollCorrectNum = 0.0
    tatollTxtNum = 0.0

    for classs in clas:
        classCorrectNum = 0.0
        classTxtNum = 0.0
        for n in range(fromnum, endnum + 1):
            try:
                txt = Txt.read(
                    (froPath + "/NewsCorpus/" + classs + "/" + str(n) + ".txt"))
                # print classs + " " + str(n) + " 成功"
            except:
                print "读取 " + classs + str(n) + " 出错"


            # ###################################################################################33
            # 对要分类的文档进行分词
            particple = JieBa.particple(txt)
            # 统计词频
            txtWordFrequency = dict()
            txtWordAll = particple.split('\\')
            for value in txtWordAll:
                if txtWordFrequency.get(value):
                    txtWordFrequency[value] = txtWordFrequency.get(value) + 1
                else:
                    txtWordFrequency[value] = 1

            Num = taltallWordNumber
            tempPAB = -1000000000000
            for i in range(len(clas)):
                PAB = float(1)

                for word, num in txtWordFrequency.items():
                    B = float(classWordNumber[i])

                    if classTrainingSet[i].get(word) != None:
                        A = float(classTrainingSet[i].get(word))
                        if taltollTrainingSet.get(word):
                            AB = float(taltollTrainingSet.get(word))
                            N = len(clas)
                            # print "Num"+str(Num)+" "+"A"+str(A)+" "+"AB"+str(AB)+" "+"B"+str(B)+" "+"N"+str(N)
                            PAB = PAB + float(naiveBayesian(A, B,AB))
                    elif taltollTrainingSet.get(word) != None:
                        # 平滑处理
                        PAB = PAB + float(naiveBayesian(0.01, B+0.01, AB+0.01))

                # print PAB
                if PAB != 1:
                    if tempPAB < PAB:
                        tempPAB = PAB
                        # print tempPAB
                        classspossbile = clas[i]

            classification = classspossbile
            # print classification

            if classification == classs:
                tatollCorrectNum = tatollCorrectNum + 1
                classCorrectNum = classCorrectNum + 1
            tatollTxtNum = tatollTxtNum + 1
            classTxtNum = classTxtNum + 1
        print classs + " " + str(classCorrectNum / classTxtNum)
    print tatollCorrectNum / tatollTxtNum

    return classification

# 测试代码

# clas = ["Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]
# froPath = "/home/yida/Desktop/webDataMiningTest/"
# classificate(froPath, clas, "")

# fromnum = 1611
# endnum = 1990
# tatollCorrectNum = 0.0
# tatollTxtNum = 0.0
#
# for classs in clas:
#     classCorrectNum = 0.0
#     classTxtNum = 0.0
#     for n in range(fromnum, endnum + 1):
#         try:
#             txtall = Txt.read(
#                 (froPath + "/NewsCorpus/" + classs + "/" + str(n) + ".txt"))
#             # print classs + " " + str(n) + " 成功"
#         except:
#             print "读取 " + classs + str(n) + " 出错"
#
#         if classificate(froPath, clas, txtall) == classs:
#             tatollCorrectNum = tatollCorrectNum + 1
#             classCorrectNum = classCorrectNum + 1
#         tatollTxtNum = tatollTxtNum + 1
#         classTxtNum = classTxtNum + 1
#         print classs + " " + classificate(froPath, clas, txtall)
#     print classs + " " + str(classCorrectNum / classTxtNum)
# print tatollCorrectNum / tatollTxtNum
