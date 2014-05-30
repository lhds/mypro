# coding=utf-8

#process the text files by using jieba,a Python Chinese word segmentation module

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
sys.path.append('../')
import jieba
jieba.initialize()
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg
import jieba.analyse
import re


f = open('output.txt','wb')
f_ex = open('words.txt','rb')
words = [line.strip() for line in f_ex.readlines()]


for eachline in open('input.txt','rb'):
    i = 0
    line = eachline.strip().decode('gbk')      #str
    
    f.write(line.encode('utf-8')+'\t')

#    seg_list = jieba.cut_for_search(line)      #搜索引擎模式分词
#    for w in seg_list:
#        f.write(w.encode('utf-8')+'|')
#    f.seek(-1,1)
#    f.write('\t')

    cut_result = list(pseg.cut(line))                 #词性标注兼分词
    for w in cut_result:
        f.write(w.word.encode('utf-8')+w.flag+'|')
    f.seek(-1,1)
    f.write('\t')

    tags = jieba.analyse.extract_tags(line, topK=10)    #TOPK排序
    for w in tags:
        f.write(w.encode('utf-8')+'|')
    f.seek(-1,1)
    f.write('\t')
    
    for w in cut_result:                          #显示指定去除词性
        if w.flag in ['u','r','p','c'] :          #更改要去除的词性 
            f.write(w.word.encode('utf-8')+'|')
            cut_result.remove(w)
            i = 1
    f.seek(-1,1)
    if i == 0:
        f.write('\t')
    f.write('\t')

    for w in cut_result:                          #去除指定词性 
        f.write(w.word.encode('utf-8')+'|')
    f.seek(-1,1)
    f.write('\t')

    for cut_w in cut_result:
        for w in words:                           #去除指定关键词
            #cut_w.word = re.sub(w.decode('gbk'),'',cut_w.word)
            if w.decode('gbk') == cut_w.word :
                cut_w.word = ''
        if cut_w.word != '':
            f.write(cut_w.word.encode('utf-8')+'|')
    f.seek(-1,1)
    f.write('\t')


    f.write('\r\n')


f.close()
f_ex.close()

