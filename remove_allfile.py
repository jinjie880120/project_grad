#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
strDIR="/home/orange/orange_project/str_2D/"
files=os.listdir(strDIR)
for f in files:
  fullpath=os.path.join(strDIR,f)
  print("刪除: %s " % fullpath)
  os.remove(fullpath)
moveDIR="/home/orange/orange_project/moveout_in/"
files=os.listdir(moveDIR)
for f in files:
  fullpath=os.path.join(moveDIR,f)
  print("刪除: %s " % fullpath)
  os.remove(fullpath)
d2dDIR="/home/orange/orange_project/dot2dot/"
files=os.listdir(d2dDIR)
for f in files:
  fullpath=os.path.join(d2dDIR,f)
  print("刪除: %s " % fullpath)
  os.remove(fullpath)
