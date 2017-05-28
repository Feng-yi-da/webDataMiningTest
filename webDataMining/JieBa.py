# encoding=utf-8
# coding=gbk
# 利用JieBa经性分词
# 返回所有分词结果
# 结果形式 词1\词2\词3
def particple(string):
    # print "JieBa分词"
    import jieba
    seg_list = jieba.cut(string)
    wordAll = "\\".join(seg_list).encode("utf8")
    # print wordAll
    return wordAll


