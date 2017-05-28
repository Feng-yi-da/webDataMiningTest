# coding=utf-8
# coding=gbk

# 找出各类有效词频构成训练集，利用idf
# 获得总词频

import sys
import Txt
import re
import math


# froPath 根目录
# froPath = "/home/yida/Desktop/webDataMiningTest/"
# clas 分类类型的数组
# clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
# clas = [ "Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]


def validWords(froPath, clas, idfnumber):
    reload(sys)
    sys.setdefaultencoding('gbk')
    # 各类的词频，非训练集
    classWordFrequency = [dict() for i in clas]
    # 各类的训练集
    classTrainingSet = [dict() for i in clas]
    # 总训练集
    taltollTrainingSet = dict()
    # df是词所属类的个数
    df = dict()
    # validWords 有效的词
    validWords = dict()

    # 读取词频文档
    # 统计df
    for i in range(len(clas)):
        # 读取文本,一次读取一行,
        classs = clas[i]
        try:
            file = open((froPath + "/TrainingSet/" + classs + "/" + classs + "WordFrequency.txt"), 'r')
            line = file.readline()
            patterm = re.compile("(.+?)\\\(\d+)")
            while line:
                match = patterm.search(line)
                if match:
                    if match.group(1) != "":
                        if classWordFrequency[i].get(match.group(1)):
                            print clas[i] + "读取词频出错"
                        else:
                            classWordFrequency[i][match.group(1)] = int(match.group(2))
                            if df.get(match.group(1)):
                                df[match.group(1)] = df.get(match.group(1)) + 1
                            else:
                                df[match.group(1)] = 1
                line = file.readline()
        except:
            print "读取 " + classs + " 出错"
            print "1"
            Txt.writeAll('a', froPath + "/ReadError.txt", "validWords " + classs + "WordFrequency.txt\n")
            # print classs + "读取成功"

    # for word, dfnum in df.items():
    #     print word + " " + str(dfnum)

    # 统计有效词频
    for word, dfnum in df.items():
        idf = float(math.log(float(len(clas)) / float(dfnum),2))
        if idf > idfnumber:
            # 整理各类的有效词
            # 将各类的词数规范，每类拥有相同的词的种类，原来不含该词的自动+1，有词的在原来的词数基础上+1
            patterm = re.compile("(\d+)")
            match = patterm.search(word)
            if match:
                continue
            else:
                for i in range(len(clas)):
                    if classWordFrequency[i].get(word):
                        classTrainingSet[i][word] = classWordFrequency[i].get(word)
                        if taltollTrainingSet.get(word):
                            taltollTrainingSet[word] = taltollTrainingSet.get(word) + classWordFrequency[i].get(word)
                        else:
                            taltollTrainingSet[word] = classWordFrequency[i].get(word)
                            # 统计总词频

    # for word, dfnum in taltollTrainingSet.items():
    #     print word + " " + str(dfnum)

    # tatollnum = taltollTrainingSet.get("兴趣")
    # print taltollTrainingSet.get("兴趣")
    # num = 0
    # for i in range(len(clas)):
    #     # 读取文本,一次读取一行,
    #     classs = clas[i]
    #     num = num + classTrainingSet[i].get("兴趣")
    #     print classTrainingSet[i].get("兴趣")
    # if tatollnum ==num:
    #     print "~"+str(tatollnum)

    # 将各类的有效词频写入文档
    for i in range(len(clas)):
        classs = clas[i]
        try:
            Txt.writeDict('w', froPath + "/TrainingSet/" + classs + "/" + classs + "TrainingSet.txt",
                          classTrainingSet[i])
        except:
            print "写入出错" + classs
            Txt.writeAll('a', froPath + "/ReadError.txt", "validWords " + classs + "TrainingSet.txt\n")

    # 将总的有效词频写入文档
    try:
        Txt.writeDict('w', froPath + "/TrainingSet/" + "TaltollTrainingSet.txt", classTrainingSet[i])
    except:
        print "写入出错" + classs
        Txt.writeAll('a', froPath + "/ReadError.txt", "validWords " + classs + "TaltollTrainingSet.txt\n")

# clas = ["Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]
# froPath = "/home/yida/Desktop/webDataMiningTest/"
# idfnumber = 1.5
# validWords(froPath, clas, idfnumber)
# 2 0 0.6687134
# 2 1 0.7406432
# 2 2 0.706
# 2 0
# 2 0
# 2 0
# 2 0
# 2 0
# 2 0
# 2 0
