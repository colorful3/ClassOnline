# -*- coding: utf8 -*-
__author__ = 'Colorful'
__date__ = '2018/2/1 下午6:00'

"""
这个模块下主要封装字符串处理的相关函数
"""


def cc_split(string="", seps=None):
    """
    拆分含有多种分隔符的字符串
    s:字符串
    seps:分隔符
    对于实际问题，推荐使用正则表达式的方法： re.split('[,;\t|]+', s)
    """
    if s is None:
        return False
    result = [string]
    for sep in seps:
        tmp_list = []
        # 使用map函数和lambda表达式处理列表
        list(map(lambda x: tmp_list.extend(x.split(sep)), result))
        result = tmp_list
    return [x for x in result if x]


if __name__ == '__main__':
    s = 'ab,cdef;ghijk|l\t\tmn|op,q|rstu|vwx|yz'
    res = cc_split(s, '\t,;|')
    print(res)
