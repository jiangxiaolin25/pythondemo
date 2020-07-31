# _*_ coding:utf-8 _*_
import shutil


class filetools(object):




    def copyfiles(self, sou, tar):

        """
        复制一个文件的内容到另一个文件里面
        :param sou: 源文件
        :param tar: 目标文件
        """
        shutil.copyfile(sou, tar)

    def readfile(self, path):
        """
        通过read读取一个文件的内容
        :param path: 文件路径
        """
        f=open(path,"r+")
        data=f.read()
        f.close()
        print("%s 说: 我 %d 岁。"+data)

    def readlinefile(self, path):
        """
        通过readline读取一个文件的内容
        :param path: 文件路径
        """
        f = open(path, "r+")
        data=f.readlines()
        # 只是辅助测试
        for i in  data :
            print (i)
        f.close()

    def writeladdfile(self, path,contont):
        """
        通过readline追加一段内容到文件
        :param path: 文件路径
        :param contont: 写入的内容
        """
        f = open(path, "a")
        f.writelines(contont)
        f.close()

    def writenewfile(self, path,contont):
        """
        通过readline重新写入一段内容到文件，覆盖之前的文件
        :param path: 文件路径
        :param contont: 写入的内容
        """
        f = open(path, "r+")
        f.writelines(contont)
        f.close()

    def speak(self,path):
        try:
            fh = open(path, "r")
            fh.write("这是一个测试文件，用于测试异常!!")
        except IOError:
            print "Error: 没有找到文件或读取文件失败"
        else:
            print "内容写入文件成功"
            fh.close()










