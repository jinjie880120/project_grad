#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
performfile="./perform_allpoint.kml"
if os.path.isfile(performfile):
  print("======================================")
  print("kml檔案已經創建,請在GoogleEarth上打開")
  print("======================================")
