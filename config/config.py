import configparser
import os

def read_ini():
	#实例化一个configparser对象
    config = configparser.ConfigParser()
    log_path = os.path.dirname(os.path.realpath(__file__))+'/config.ini'
    #path为ini文件的存放路径，最好为绝对路径，获取文件绝对路径的方法，另有文详细描述
    config.read(log_path, encoding='utf8')
    return config
