# coding=utf-8
# coding=gbk

# 新闻分词并统计词频

import sys
import Txt
import JieBa

# froPath 根目录
# froPath = "/home/yida/Desktop/webDataMiningTest/"
# clas 分类类型的数组
# clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
# clas = [ "Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]
def wordFrequency(froPath, clas):
    reload(sys)
    sys.setdefaultencoding('gbk')

    for classs in clas:
        # 读取文本
        try:
            txtall = Txt.read(
                (froPath + "/TrainingSet/" + classs + "/" + classs + "TextIntegration.txt"))
        except:
            print "读取 " + classs + " 出错"
            Txt.writeAll('a', froPath + "/ReadError.txt", "WordFrequency " + classs + "TextIntegration.txt\n")

        # 分词
        particple = JieBa.particple(txtall)

        # 统计词频
        wordFrequency = dict()
        wordAll = particple.split('\\')
        for value in wordAll:
            if wordFrequency.get(value):
                wordFrequency[value] = wordFrequency.get(value) + 1
            else:
                wordFrequency[value] = 1

        # 写入
        try:
            Txt.writeDict('w', froPath + "/TrainingSet/" + classs + "/" +classs + "WordFrequency.txt", wordFrequency)
        except:
            print "写入出错" + classs
            Txt.writeAll('a',  froPath + "/ReadError.txt", "WordFrequency " + classs + "WordFrequency.txt\n")

clas = [ "Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]
froPath = "C:/Users/yida/Desktop/webDataMiningTest/"
# wordFrequency(froPath,clas)