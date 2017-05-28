# coding=utf-8
# coding=gbk


# 读取txt文件
# txt有不同的文件格式
def read(path):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    try:
        file = open(path, 'r')
        txtAll = file.read().decode("gb2312")
        file.closed
        return txtAll
    except:
        try:
            file = open(path, 'r')
            txtAll = file.read().decode("gb18030")
            file.closed
            return txtAll
        except:
            try:
                file = open(path, 'r')
                txtAll = file.read()
                file.closed
                return txtAll
            except:
                print "读取失败"



# 写入文件
# style 写入文件的形式
def writeAll(style, path, txt):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    file = open(path, style)
    file.write(txt)
    file.closed


# 将字典写入文件
def writeDict(style, path, dict):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    file = open(path, style)
    for key, value in dict.items():
        file.write(key + "\\" + str(value) + "\n")
    file.closed


# clas = ["Culture"]
# for classs in clas:
#     for i in range(10, 1900):
#         print read("/home/yida/Desktop/webDataMiningTest/NewsCorpus/" + classs + "/" + str(1150) + ".txt")


# path ="/home/yida/Desktop/webDataMiningTest/a.txt"
# read(path)



# clas = [ "Finance", "Internet", "Health", "Education", "Military", "Travel", "Sports", "Culture", "Recruitment"]
# for classs in clas:
#     read("/home/yida/Desktop/webDataMiningTest/TrainingSet/" +  classs + "/" +classs + "TextIntegration.txt")
