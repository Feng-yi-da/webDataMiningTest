# coding=utf-8
# coding=gbk

import ValidWords
import Classification
import IntegrationTxt
import WordFrequency
clas = ["Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Recruitment"]
froPath = "C:/Users/yida/Desktop/webDataMiningTest/"
idfnumber = 0.1

# # 整合文本
# IntegrationTxt.integrationTxt(froPath, clas, 10, 1999)
# # 文本分词
# WordFrequency.wordFrequency(froPath, clas)
# # 训练集
# ValidWords.validWords(froPath, clas, idfnumber)

Classification.classificate(froPath, clas, " ")


# 0.0 0.754
# 0.1 0.7
# 0.2 0.75