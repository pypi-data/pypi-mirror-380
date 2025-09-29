#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2025/09/26 10:36 
# @Author : JY
"""
默认都不修改原数据
"""


class listHelper:
    def __init__(self):
        pass

    @staticmethod
    def explode(data, n):
        """将列表分割 每一份n的长度"""
        return [data[i:i + n] for i in range(0, len(data), n)]

    @staticmethod
    def del_by_value(data, value):
        """根据值从list中删除数据"""
        if not isinstance(value, list):
            value = [value]
        return [x for x in data if x not in value]

    @staticmethod
    def del_by_index(data, index):
        """根据索引从list中删除数据"""
        if not isinstance(index, list):
            index = [index]
        return [data[i] for i in range(len(data)) if i not in index]

    @staticmethod
    def sort(data, sort_func=None, reverse=False):
        if sort_func is not None:
            return sorted(data, key=sort_func, reverse=reverse)
        else:
            return sorted(data, reverse=reverse)


if __name__ == '__main__':
    dataa = [a for a in '01234567389'][::-1]
    dataa.append('11')
    print('原始数据', dataa)
    res = listHelper.sort(dataa)
    print('原始数据', dataa)
    print('------------------')
    print('修后数据', res)
