#!/usr/bin/python
#-*- coding=utf-8 -*-
f=open("perform.txt","w")
word=input("請輸入所有你想呈現的文字:")
#print word
#word = word.decode('utf-8')
f.write(word)
f.close()
