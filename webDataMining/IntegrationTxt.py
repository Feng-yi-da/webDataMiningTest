# coding=utf-8
# coding=gbk

# 将各类新闻整合在一起

import sys
import Txt

# froPath 根目录
# froPath = "/home/yida/Desktop/webDataMiningTest/"
# clas 分类类型的数组
# clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
# clas = [ "Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]

def integrationTxt(froPath, clas, fromnum, endnum):
    reload(sys)
    sys.setdefaultencoding('gbk')
    for classs in clas:
        txtall = ""
        for n in range(fromnum, endnum + 1):
            try:
                txtall = txtall + Txt.read(
                    (froPath + "/NewsCorpus/" + classs + "/" + str(n) + ".txt"))
                print classs + " " + str(n) + " 成功"
            except:
                print "读取 " + classs + str(n) + " 出错"
                Txt.writeAll('a', froPath + "/ReadError.txt", "integrationTxt " + classs + " " + str(n) + ".txt\n")
            # print txtall
        try:
            Txt.writeAll('w', froPath + "/TrainingSet/" + classs + "/" + classs + "TextIntegration.txt", txtall)
        except:
            print "写入出错" + classs + str(n)
            Txt.writeAll('a', froPath + "/WriteError.txt", "first " + classs + " " + str(n) + ".txt\n")

clas = [ "Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]
froPath = "C:/Users/yida/Desktop/webDataMiningTest/"
# integrationTxt(froPath, clas, 10, 1610)
