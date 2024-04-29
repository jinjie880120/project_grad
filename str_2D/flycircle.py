import simplekml
import math
import sys
import GPS_Prid
import datetime
from geopy.geocoders import Nominatim


def convert3D(x,y,angle,word_la,word_long):
  
  #pic size and angle
  SizeX=600
  SizeY=600
  CentX=SizeX/2
  Ang=45
  #pic dis and height
  R=200
  Heading=180
  BottomAtti=20
  theta=Heading-angle
  #caculate
  Dis=(CentX)*(math.cos(math.radians(Ang))/math.sin(math.radians(Ang)))
  AddDegree=math.degrees(math.atan(float(BottomAtti)/R))
  DiffAng=math.degrees(math.atan((x-CentX)/Dis))
  R_forx=R*(1/math.cos(math.radians(DiffAng)))
  DiffUpAng=math.degrees(math.atan(float(SizeY-y)/Dis))+AddDegree
  UPDis=R*math.tan(math.radians(DiffUpAng))
  #return 3DPoint
  restring=("%s,%f" % (GPS_Prid.GPSP((word_long,word_la),theta+DiffAng,R_forx),UPDis))
  return restring
def timespan_return(d,h,m,s):
  timeforreturn=("2020-01-%sT%s:%s:%sZ" % (str(d).zfill(2),str(h).zfill(2),str(m).zfill(2),str(s).zfill(2)))
  return timeforreturn
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
#-------------------main process----------------------------
kml=simplekml.Kml()
f=open("2DPoint.txt","r")
p1=[]
p2=[]
for line in f:
  line=line.strip('\n')
  x=int(line.split(", ")[0])
  y=int(line.split(", ")[1])
  p1.append(x)
  p2.append(y)

word=input("請輸入地點:")
#geopy des
geolocator=Nominatim(user_agent="ll563tw@yahoo.com.tw")
location=geolocator.geocode(word)
print(location.address)
print((location.latitude, location.longitude))
word_la=round(location.latitude,6)
word_long=round(location.longitude,6)

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

#set time
endday,endhour,endminute,endsecond=time_add(nowday,nowhour,nowminute,nowsecond,STATIC_TIME)
nowtimestring=timespan_return(nowday,nowhour,nowminute,nowsecond)
endtimestring=timespan_return(endday,endhour,endminute,endsecond)
nowday,nowhour,nowminute,nowsecond=endday,endhour,endminute,endsecond

for i in range(len(p1)):
  string3D=convert3D(p1[i],p2[i],0,word_la,word_long)
  G1=string3D.split(",")[0]
  G2=string3D.split(",")[1]
  H=string3D.split(",")[2]
  p=kml.newpoint( coords=[(G2,G1,H)])
  p.altitudemode=simplekml.AltitudeMode.relativetoground
  p.timespan.begin=nowtimestring
  p.timespan.end=endtimestring

for i in range(72):
  #set time
  endday,endhour,endminute,endsecond=time_add(nowday,nowhour,nowminute,nowsecond,DYNAMIC_TIME)
  nowtimestring=timespan_return(nowday,nowhour,nowminute,nowsecond)
  endtimestring=timespan_return(endday,endhour,endminute,endsecond)
  nowday,nowhour,nowminute,nowsecond=endday,endhour,endminute,endsecond


  angle=i*5
  for j in range(len(p1)):
    string3D=convert3D(p1[j],p2[j],angle,word_la,word_long)
    G1=string3D.split(",")[0]
    G2=string3D.split(",")[1]
    H=string3D.split(",")[2]
    p=kml.newpoint( coords=[(G2,G1,H)])
    p.altitudemode=simplekml.AltitudeMode.relativetoground
    p.timespan.begin=nowtimestring
    p.timespan.end=endtimestring

kml.save("circlefly.kml")