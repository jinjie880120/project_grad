#!/usr/bin/python
#-*- coding: utf-8 -*-
import simplekml
import math
import sys
import GPS_Prid
import datetime
import os
#def move out function
def moveout_line(x,y):
  dvnum=10
  #move 10 time and move seat 100 according direction
  if x<300:
    if y>300:
      if abs(x)>abs(600-y):
        afterx=x
        aftery=y+100
        returnx,returny=devideLine(x,y,afterx,aftery,dvnum)
      else:
        afterx=x+100
        aftery=y
        returnx,returny=devideLine(x,y,afterx,aftery,dvnum)
    else:
      if abs(600-x)>abs(600-y):
        afterx=x
        aftery=y+100
        returnx,returny=devideLine(x,y,afterx,aftery,dvnum)
      else:
        afterx=x-100
        aftery=y
        returnx,returny=devideLine(x,y,afterx,aftery,dvnum)
  else:
    if y>300:
      if abs(x)>abs(y):
        afterx=x
        aftery=y-100
        returnx,returny=devideLine(x,y,afterx,aftery,dvnum)
      else:
        afterx=x+100
        aftery=y
        returnx,returny=devideLine(x,y,afterx,aftery,dvnum)
    else:
      if abs(600-x)>abs(y):
        afterx=x
        aftery=y-100
        returnx,returny=devideLine(x,y,afterx,aftery,dvnum)
      else:
        afterx=x-100
        aftery=y
        returnx,returny=devideLine(x,y,afterx,aftery,dvnum)
  return returnx,returny
#def dot&dot&devide return array of line
def devideLine(x1,y1,x2,y2,devidenum):
  minusx=x2-x1
  minusy=y2-y1
  returnx=[]
  returny=[]
  for i in range(1,devidenum):
    disx=minusx/devidenum
    disy=minusy/devidenum
    nx=x1+i*disx
    ny=y1+i*disy
    returnx.append(nx)
    returny.append(ny)
  return returnx,returny
#def(x,y)return 3DPoint func
def convert3D(x,y):
  #pic size and angle
  SizeX=600
  SizeY=600
  CentX=SizeX/2
  Ang=45
  #pic dis and height
  R=200
  Heading=90
  BottomAtti=20
  theta=Heading+90
  #caculate
  Dis=(CentX)*(math.cos(math.radians(Ang))/math.sin(math.radians(Ang)))
  AddDegree=math.degrees(math.atan(float(BottomAtti)/R))
  DiffAng=math.degrees(math.atan((x-CentX)/Dis))
  R_forx=R*(1/math.cos(math.radians(DiffAng)))
  DiffUpAng=math.degrees(math.atan(float(SizeY-y)/Dis))+AddDegree
  UPDis=R*math.tan(math.radians(DiffUpAng))
  #return 3DPoint
  restring=("%s,%f" % (GPS_Prid.GPSP((120.288289,22.733552),theta+DiffAng,R_forx),UPDis))
  return restring
#for return time span string
def timespan_return(d,h,m,s):
  timeforreturn=("2020-01-%sT%s:%s:%sZ" % (str(d).zfill(2),str(h).zfill(2),str(m).zfill(2),str(s).zfill(2)))
  return timeforreturn
#calculate time
def time_add(d,h,m,s,addminute):
  m+=addminute
  if m>=60:
    correcttime=False
    while(not correcttime):
      h+=1
      m-=60
      if m<60:
        correcttime=True
  if h>=24:
    correcttime=False
    while(not correcttime):
      d+=1
      h-=24
      if m<60:
        correcttime=True
  return d,h,m,s
#-----------------------------main process--------------------------------------------
#set simplekml
kml=simplekml.Kml()
#open allpoint 2D file
allnum=len(os.listdir("./str_2D"))
#initiial time span 
nowday=1
nowhour=0
nowminute=0
nowsecond=0
endday=1
endhour=0
endminute=0
endsecond=0
STATIC_TIME=20
DYNAMIC_TIME=10
nowtimestring=""
endtimestring=""
#for all word write in kml
for i in range((allnum-1)):
  rightnum=i+1
  secondnum=rightnum+1
  #catch two 2D point
  firstfile="./str_2D/"+str(rightnum)+".txt"
  secondfile="./str_2D/"+str(secondnum)+".txt"
  firstx=[]
  firsty=[]
  secondx=[]
  secondy=[]
  ff=open(firstfile,"r")
  for line in ff:
    line=line.strip('\n')
    x=int(line.split(", ")[0])
    y=int(line.split(", ")[1])
    firstx.append(x)
    firsty.append(y)
  ff.close()
  sf=open(secondfile,"r")
  for line in sf:
    line=line.strip('\n')
    x=int(line.split(", ")[0])
    y=int(line.split(", ")[1])
    secondx.append(x)
    secondy.append(y)
  sf.close()
  #first dot for 20 minute
  #set time
  endday,endhour,endminute,endsecond=time_add(nowday,nowhour,nowminute,nowsecond,STATIC_TIME)
  nowtimestring=timespan_return(nowday,nowhour,nowminute,nowsecond)
  endtimestring=timespan_return(endday,endhour,endminute,endsecond)
  nowday,nowhour,nowminute,nowsecond=endday,endhour,endminute,endsecond
  #first word convert 3D
  for i in range(len(firstx)):
    string3D=convert3D(firstx[i],firsty[i])
    G1=string3D.split(",")[0]
    G2=string3D.split(",")[1]
    H=string3D.split(",")[2]
    p=kml.newpoint( coords=[(G2,G1,H)])
    p.altitudemode=simplekml.AltitudeMode.relativetoground
    p.timespan.begin=nowtimestring
    p.timespan.end=endtimestring
  #load move out file first line 1 means move out 2 means join in 
  mvoutx=[]
  mvouty=[]
  moveoutfile="./moveout_in/"+str(rightnum)+str(secondnum)+"movedot.txt"
  mjf=open(moveoutfile,"r")
  moveoutsign=mjf.readline()
  moveoutsign=int(moveoutsign)
  if moveoutsign==1:
    for line in mjf:
      line=line.strip('\n')
      line=line.strip('(')
      line=line.strip(')')
      mvoutx.append(int(line.split(",")[0]))
      mvouty.append(int(line.split(",")[0]))
  mjf.close()
  #set move time
  mnday=nowday
  mnhour=nowhour
  mnminute=nowminute
  mnsecond=nowsecond
  meday=nowday
  mehour=nowhour
  meminute=nowminute
  mesecond=nowsecond
  #get array and convert 3D for every 10 minute
  movedotx=[]
  movedoty=[]
  movedividenum=10
  MOVE_TIME=10
  for i in range(len(mvoutx)):
    mvx_array,mvy_array=moveout_line(mvoutx[i],mvouty[i])
    movedotx.append(mvx_array)
    movedoty.append(mvy_array)
  for i in range(0,movedividenum-1):
    #set time
    meday,mehour,meminute,mesecond=time_add(mnday,mnhour,mnminute,mnsecond,MOVE_TIME)
    mntimestring=timespan_return(mnday,mnhour,mnminute,mnsecond)
    metimestring=timespan_return(meday,mehour,meminute,mesecond)
    mnday,mnhour,mnminute,mnsecond=meday,mehour,meminute,mesecond
    for j in range(len(movedotx)):
      string3D=convert3D(movedotx[j][i],movedoty[j][i])
      G1=string3D.split(",")[0]
      G2=string3D.split(",")[1]
      H=string3D.split(",")[2]
      p=kml.newpoint( coords=[(G2,G1,H)])
      p.altitudemode=simplekml.AltitudeMode.relativetoground
      p.timespan.begin=mntimestring
      p.timespan.end=metimestring
  #load d2d file
  beforex=[]
  beforey=[]
  afterx=[]
  aftery=[]
  d2dfile="./dot2dot/"+str(rightnum)+str(secondnum)+"d2d.txt"
  fd=open(d2dfile,"r")
  for line in fd:
    line=line.strip('\n')
    beforex.append(int(line.split("&")[0].split(",")[0]))
    beforey.append(int(line.split("&")[0].split(",")[1]))
    afterx.append(int(line.split("&")[1].split(",")[0]))
    aftery.append(int(line.split("&")[1].split(",")[1]))
  #get devide array and store in a list
  linedotx=[]
  linedoty=[]
  devide_num=40
  for i in range(0,len(beforex)):
    x_array,y_array=devideLine(beforex[i],beforey[i],afterx[i],aftery[i],devide_num)
    linedotx.append(x_array)
    linedoty.append(y_array)
  #get 3Ddot and write in kml every dot seperate 10min
  for i in range(0,devide_num-1):
    #set time
    endday,endhour,endminute,endsecond=time_add(nowday,nowhour,nowminute,nowsecond,DYNAMIC_TIME)
    nowtimestring=timespan_return(nowday,nowhour,nowminute,nowsecond)
    endtimestring=timespan_return(endday,endhour,endminute,endsecond)
    nowday,nowhour,nowminute,nowsecond=endday,endhour,endminute,endsecond
    #get 3DP
    for j in range(0,len(linedotx)):
      string3D=convert3D(linedotx[j][i],linedoty[j][i])
      G1=string3D.split(",")[0]
      G2=string3D.split(",")[1]
      H=string3D.split(",")[2]
      p=kml.newpoint( coords=[(G2,G1,H)])
      p.altitudemode=simplekml.AltitudeMode.relativetoground
      p.timespan.begin=nowtimestring
      p.timespan.end=endtimestring
  #second word for 20 minutes
  #set time
  endday,endhour,endminute,endsecond=time_add(nowday,nowhour,nowminute,nowsecond,STATIC_TIME)
  nowtimestring=timespan_return(nowday,nowhour,nowminute,nowsecond)
  endtimestring=timespan_return(endday,endhour,endminute,endsecond)
  nowday,nowhour,nowminute,nowsecond=endday,endhour,endminute,endsecond
  for i in range(0,len(secondx)):
    string3D=convert3D(secondx[i],secondy[i])
    G1=string3D.split(",")[0]
    G2=string3D.split(",")[1]
    H=string3D.split(",")[2]
    ##print(string3D)
    p=kml.newpoint( coords=[(G2,G1,H)])
    p.altitudemode=simplekml.AltitudeMode.relativetoground
    p.timespan.begin=nowtimestring
    p.timespan.end=endtimestring

kml.save("perform_allpoint.kml")
