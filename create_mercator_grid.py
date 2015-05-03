__author__ = 'wyb'
# -*- coding:utf-8 -*-
# creating 0-12 levels Mercator grid

import arcpy
import os
'''
调用ArcPy接口生成0级墨卡托网格
'''

n = int(raw_input('n = '))         # 输入要生成对应的级别
output_shp = 'F:\\Data\\%s.shp' % n    # 输出路径及对应的文件名
grid_num = 2**n
arcpy.env.overwriteOutput = True
arcpy.CreateFishnet_management(output_shp, '-20037508.3428114 -20077508.342814', '-20037508.3428114 -20037508.3428114',
                               '', '', grid_num, grid_num, '20037508.3428114 20037508.3428114', 'NO_LABELS', '',
                               'POLYGON')

'''
获取dbf文件
'''

name_sub = os.path.split(output_shp)
name_text = os.path.splitext(name_sub[1])
name_dbf = name_text[0] + '.dbf'
path_dbf = os.path.join(name_sub[0], name_dbf)

del output_shp

'''
添加x_code，y_code，code三个字段
'''

arcpy.AddField_management(path_dbf, 'x_code', 'DOUBLE')
arcpy.AddField_management(path_dbf, 'y_code', 'DOUBLE')
arcpy.AddField_management(path_dbf, 'code', 'TEXT')

'''
给三个字段赋值
'''

x_list_sub = []
x_list = []
y_list = []

cursor = arcpy.UpdateCursor(path_dbf)

# 编号规则

for i in xrange(0, 2**n):
    x_list_sub.append(i)
for i1 in x_list_sub*(2**n):
    x_list.append(i1)
for j in xrange(2**n, -1, -1):
    for j1 in xrange(0, 2**n):
        y_list.append(j)

k = 0
v = 0

for row in cursor:
    row.setValue('x_code', x_list[k])
    row.setValue('y_code', y_list[v])
    code = str(n) + '-' + str(x_list[k]) + '-' + str(y_list[v])
    row.setValue('code', code)
    cursor.updateRow(row)
    k += 1
    v += 1

del cursor, row
