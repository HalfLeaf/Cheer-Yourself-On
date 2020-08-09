#!/usr/bin/python
#-*-coding：utf-8 -*-

'''
# -------------------------------------------------------------------------------
# Purpose:     根据提供的文本生成json格式化数据
#
# Author:      青衫少年春归也
#
# Created:     2020-05-20
#
# Copyright:
# -------------------------------------------------------------------------------
'''

import json


class GenerateData():
    def __init__(self):
        self.data = {}
        self.index = 1

    def read(self):
        """
        读取json文件中持久化保存的数据
        """
        with open("lovaTalk.json", "r", encoding='utf-8') as fread:
            self.data = json.load(fread)
        self.index = len(self.data)

    def write(self):
        """
        数据写入json文件中持久化保存
        """
        with open("lovaTalk.json", "w", encoding='utf-8') as fwrite:
             json.dump(self.data, fwrite, ensure_ascii=False)

    def split_context(self, line_split='\n\n', content_split="\n"):
        """
        按照分割文本
            :param line_split: 每一行的分割
            :param content_split: 每行内容的分割
        :return:
        """
        with open("story2.txt", "r", encoding='utf-8') as fr:
            context = fr.read()

        content = context.split(line_split)
        for _index, text in enumerate(content):
            if len(text) > 1:
                story = text.split(content_split)
                key = self.index+_index+1
                self.data.update({
                    key:story
                })




if __name__ == '__main__':
    g = GenerateData()
    g.read()
    g.split_context()
    g.write()