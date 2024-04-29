#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import math
def choosedot(x,y,area,des):
  chosex=x[0]
  chosey=y[0]
  chosenum=0
  if area==1:
    for i in range(0,len(x)):
      if x[i]>chosex:
        chosex=x[i]
        chosey=y[i]
        chosenum=i
  elif area==2:
    for i in range(0,len(x)):
      if y[i]<chosey:
        chosex=x[i]
        chosey=y[i]
        chosenum=i
  elif area==3:
    for i in range(0,len(x)):
      if x[i]<chosex:
        chosex=x[i]
        chosey=y[i]
        chosenum=i
  else:
    if des==1:
      for i in range(0,len(x)):
        if y[i]>chosey:
          chosex=x[i]
          chosey=y[i]
          chosenum=i
    elif des==2:
      for i in range(0,len(x)):
        if x[i]>chosex and y[i]>chosey:
          chosex=x[i]
          chosey=y[i]
          chosenum=i
    else:
      for i in range(0,len(x)):
        if x[i]>chosex:
          chosex=x[i]
          chosey=y[i]
          chosenum=i
  return chosex,chosey,chosenum

def getdistance(x1,y1,x2,y2):
  xc=abs(x1-x2)
  yc=abs(y1-y2)
  dis=math.sqrt((xc**2)+(yc**2))
  return dis

def dot2dot(bx,by,ax,ay):
  dis=getdistance(bx[0],by[0],ax[0],ay[0])
  cbx=bx[0]
  cby=by[0]
  cax=ax[0]
  cay=ay[0]
  bnum=0
  anum=0
  for i in range(0,len(bx)):
    for j in range(0,len(ax)):
      newdis=getdistance(bx[i],by[i],ax[j],ay[j])
      if dis>newdis:
        #print("get new dot b:(%s,%s) a:(%s,%s) dis:%s" % (bx[i],by[i],ax[j],ay[j],newdis))
        cbx=bx[i]
        cby=by[i]
        cax=ax[j]
        cay=ay[j]
        dis=newdis
        bnum=i
        anum=j
  return cbx,cby,cax,cay,bnum,anum

def calculate_yidong(fp1,fp2,fac1,fac2,fac3,fac4,fdotsum,sp1,sp2,sac1,sac2,sac3,sac4,sdotsum,minusnum,rightnum):
  if minusnum>0:
    jian=minusnum
    print("目標移動區域數量:( %s , %s , %s , %s ),待移開: %s 個點" % (sac1,sac2,sac3,sac4,minusnum))
    yiwan=True
    yi1=0
    yi2=0
    yi3=0
    yi4=0
    yikaistr=""
    while(yiwan):
      if fac1>sac1:
        fac1-=1
        jian-=1
        yi1+=1
        yikaix=fp1[0]
        yikaiy=fp1[0]
        yikainum=0
        for i in range(len(fp1)):
          if fp1[i]<300 and fp2[i]>300:
            if fp1[i]<yikaix or fp2[i]>yikaiy:
              yikaix=fp1[i]
              yikaiy=fp2[i]
              yikainum=i
        print("第一個區域移開一個點,要被移開的座標x: %s ,y: %s" % (yikaix,yikaiy))
        yikaistr+="("+str(yikaix)+","+str(yikaiy)+")\n"
        del fp1[yikainum]
        del fp2[yikainum]
      else:
        if fac2>sac2:
          fac2-=1
          jian-=1
          yi2+=1
          yikaix=fp1[0]
          yikaiy=fp2[0]
          yikainum=0
          for i in range(len(fp1)):
            if fp1[i]>300 and fp2[i]>300:
              if fp1[i]>yikaix or fp2[i]>yikaiy:
                yikaix=fp1[i]
                yikaiy=fp2[i]
                yikainum=i
          print("第二個區域移開一個點,要被移開的座標x: %s ,y: %s" % (yikaix,yikaiy))
          yikaistr+="("+str(yikaix)+","+str(yikaiy)+")\n"
          del fp1[yikainum]
          del fp2[yikainum]
        else:
          if fac3>sac3:
            fac3-=1
            jian-=1
            yi3+=1
            yikaix=fp1[0]
            yikaiy=fp2[0]
            yikainum=0
            for i in range(len(fp1)):
              if fp1[i]>300 and fp2[i]<300:
                if fp1[i]>yikaix or fp2[i]<yikaiy:
                  yikaix=fp1[i]
                  yikaiy=fp2[i]
                  yikainum=i
            print("第三個區域移開一個點,要被移開的座標x: %s ,y: %s" % (yikaix,yikaiy))
            yikaistr+="("+str(yikaix)+","+str(yikaiy)+")\n"
            del fp1[yikainum]
            del fp2[yikainum]
          else:
            if fac4>sac4:
              fac4-=1
              jian-=1
              yi4+=1
              yikaix=fp1[0]
              yikaiy=fp2[0]
              yikainum=0
              for i in range(len(fp1)):
                if fp1[i]<300 and fp2[i]<300:
                  if fp1[i]<yikaix or fp2[i]<yikaiy:
                    yikaix=fp1[i]
                    yikaiy=fp2[i]
                    yikainum=i
              print("第四個區域移開一個點,要被移開的座標x: %s ,y: %s" % (yikaix,yikaiy))
              yikaistr+="("+str(yikaix)+","+str(yikaiy)+")\n"
              del fp1[yikainum]
              del fp2[yikainum]
            else:
              print("Error~!")
              sys.exit()
      if jian==0:
        print("移開完成")
        print("所有移開座標:\n %s" % yikaistr)
        yikaifilename="./moveout_in/"+str(rightnum)+str((rightnum+1))+"movedot.txt"
        kaif=open(yikaifilename,"w")
        kaif.write("1\n")
        kaif.write(yikaistr)
        kaif.close()
        print("=============================")
        yiwan=False
    print("所有區域移開( %s, %s, %s, %s)個點" % (yi1,yi2,yi3,yi4))
    print("所有區域剩下( %s, %s, %s, %s)個點" % (fac1,fac2,fac3,fac4))
    print("=============================")
    area1x=[]
    area1y=[]
    area2x=[]
    area2y=[]
    area3x=[]
    area3y=[]
    area4x=[]
    area4y=[]
    for i in range(0,len(fp1)):
      if fp1[i]>300:
        if fp2[i]>300:
          area2x.append(fp1[i])
          area2y.append(fp2[i])
        else:
          area3x.append(fp1[i])
          area3y.append(fp2[i])
      else:
        if fp2[i]>300:
          area1x.append(fp1[i])
          area1y.append(fp2[i])
        else:
          area4x.append(fp1[i])
          area4y.append(fp2[i])
    #print("第一區域內座標:"),
    #for i in range(0,len(area1x)):
    #  print("(%s,%s)" % (area1x[i],area1y[i])),
    #print("\n第二區域內座標:"),
    #for i in range(0,len(area2x)):
    #  print("(%s,%s)" % (area2x[i],area2y[i])),
    #print("\n第三區域內座標:"),
    #for i in range(0,len(area3x)):
    #  print("(%s,%s)" % (area3x[i],area3y[i])),
    #print("\n第四區域內座標:"),
    #for i in range(0,len(area4x)):
    #  print("(%s,%s)" % (area4x[i],area4y[i])),
    #print("\n=============================")
    huanwei1=True
    while huanwei1:
      if fac1>sac1:
        fac1-=1
        fac2+=1
        cx,cy,cnum=choosedot(area1x,area1y,1,0)
        print("第一區域移到第二區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area1x[cnum]
        del area1y[cnum]
        area2x.append(cx)
        area2y.append(cy)
      if fac1<sac1:
        fac1+=1
        fac4-=1
        cx,cy,cnum=choosedot(area4x,area4y,4,1)
        print("第四區域移到第一區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area4x[cnum]
        del area4y[cnum]
        area1x.append(cx)
        area1y.append(cy)
      if fac1==sac1:
        print("第一區域完成")
        huanwei1=False
    huanwei2=True
    while huanwei2:
      if fac2>sac2:
        fac2-=1
        fac3+=1
        cx,cy,cnum=choosedot(area2x,area2y,2,0)
        print("第二區域移到第三區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area2x[cnum]
        del area2y[cnum]
        area3x.append(cx)
        area3y.append(cy)
      if fac2<sac2:
        fac2+=1
        fac4-=1
        cx,cy,cnum=choosedot(area4x,area4y,4,2)
        print("第四區域移到第二區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area4x[cnum]
        del area4y[cnum]
        area2x.append(cx)
        area2y.append(cy)
      if fac2==sac2:
        print("第二區域完成")
        huanwei2=False
    huanwei3=True
    while huanwei3:
      if fac3>sac3:
        fac3-=1
        fac4+=1
        cx,cy,cnum=choosedot(area3x,area3y,3,0)
        print("第三區域移到第四區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area3x[cnum]
        del area3y[cnum]
        area4x.append(cx)
        area4y.append(cy)
      if fac3<sac3:
        fac3+=1
        fac4-=1
        cx,cy,cnum=choosedot(area4x,area4y,4,3)
        print("第四區域移到第三區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area4x[cnum]
        del area4y[cnum]
        area3x.append(cx)
        area3y.append(cy)
      if fac3==sac3:
        print("第三區域完成")
        huanwei3=False
    if fac4==sac4:
        print("全部區域整理完成")
        print("====================================")
    else:
        print("尚有錯誤")
    print("劃分變更後座標...")
    afarea1x=[]
    afarea2x=[]
    afarea3x=[]
    afarea4x=[]
    afarea1y=[]
    afarea2y=[]
    afarea3y=[]
    afarea4y=[]
    for i in range(0,len(sp1)):
        if sp1[i]>300:
            if sp2[i]>300:
                afarea2x.append(sp1[i])
                afarea2y.append(sp2[i])
            else:
                afarea3x.append(sp1[i])
                afarea3y.append(sp2[i])
        else:
            if sp2[i]>300:
                afarea1x.append(sp1[i])
                afarea1y.append(sp2[i])
            else:
                afarea4x.append(sp1[i])
                afarea4y.append(sp2[i])
    #print("第一區域內座標:"),
    #for i in range(0,len(afarea1x)):
    #    print("(%s,%s)" % (afarea1x[i],afarea1y[i])),
    #print("\n第二區域內座標:"),
    #for i in range(0,len(afarea2x)):
    #    print("(%s,%s)" % (afarea2x[i],afarea2y[i])),
    #print("\n第三區域內座標:"),
    #for i in range(0,len(afarea3x)):
    #    print("(%s,%s)" % (afarea3x[i],afarea3y[i])),
    #print("\n第四區域內座標:"),
    #for i in range(0,len(afarea4x)):
    #    print("(%s,%s)" % (afarea4x[i],afarea4y[i])),
    print("\n劃分完成")
    print("====================================")
    print("設定點對點")
    fdot2dot=""
    print("設定第一區域")
    dtd1=True
    bx=area1x
    by=area1y
    ax=afarea1x
    ay=afarea1y
    while dtd1:
      if len(bx)>0:
        cbx,cby,cax,cay,bnum,anum=dot2dot(bx,by,ax,ay)
        del bx[bnum]
        del by[bnum]
        del ax[anum]
        del ay[anum]
        print("(%s,%s)移動到(%s,%s)" % (cbx,cby,cax,cay))
        fdot2dot+=("%s,%s&%s,%s\n" % (cbx,cby,cax,cay))
      if len(bx)==0:
        dtd1=False
    print("第一區域完成")
    print("====================================")
    print("設定第二區域")
    dtd2=True
    bx=area2x
    by=area2y
    ax=afarea2x
    ay=afarea2y
    while dtd2:
      if len(bx)>0:
        cbx,cby,cax,cay,bnum,anum=dot2dot(bx,by,ax,ay)
        del bx[bnum]
        del by[bnum]
        del ax[anum]
        del ay[anum]
        print("(%s,%s)移動到(%s,%s)" % (cbx,cby,cax,cay))
        fdot2dot+=("%s,%s&%s,%s\n" % (cbx,cby,cax,cay))
      if len(bx)==0:
        dtd2=False
    print("第二區域完成")
    print("====================================")
    print("設定第三區域")
    dtd3=True
    bx=area3x
    by=area3y
    ax=afarea3x
    ay=afarea3y
    while dtd3:
      if len(bx)>0:
        cbx,cby,cax,cay,bnum,anum=dot2dot(bx,by,ax,ay)
        del bx[bnum]
        del by[bnum]
        del ax[anum]
        del ay[anum]
        print("(%s,%s)移動到(%s,%s)" % (cbx,cby,cax,cay))
        fdot2dot+=("%s,%s&%s,%s\n" % (cbx,cby,cax,cay))
      if len(bx)==0:
        dtd3=False
    print("第三區域完成")
    print("====================================")
    print("設定第四區域")
    dtd4=True
    bx=area4x
    by=area4y
    ax=afarea4x
    ay=afarea4y
    while dtd4:
      if len(bx)>0:
        cbx,cby,cax,cay,bnum,anum=dot2dot(bx,by,ax,ay)
        del bx[bnum]
        del by[bnum]
        del ax[anum]
        del ay[anum]
        print("(%s,%s)移動到(%s,%s)" % (cbx,cby,cax,cay))
        fdot2dot+=("%s,%s&%s,%s\n" % (cbx,cby,cax,cay))
      if len(bx)==0:
        dtd4=False
    print("第四區域完成")
    print("====================================")
    print("座標寫入檔案")
    fdotname="./dot2dot/"+str(rightnum)+str((rightnum+1))+"d2d.txt"
    fdot=open(fdotname,"w")
    fdot.write(fdot2dot)
    fdot.close()
    print("寫入完成")
    print("====================================")
  #join dot
  else:
    jialu=abs(minusnum)
    print("目標移動區域數量:( %s , %s , %s , %s ),待加入: %s 個點" % (sac1,sac2,sac3,sac4,abs(minusnum)))
    yiwan=True
    yi1=0
    yi2=0
    yi3=0
    yi4=0
    jialustr=""
    while(yiwan):
      if fac1<sac1:
        fac1+=1
        jialu-=1
        yi1+=1
        jialux=0
        jialuy=600
        if yi1%2==0:
          jialux+=(yi1/2)*10
          jialux=int(jialux)
        else:
          jialuy-=(yi1/2)*10
          jialuy=int(jialuy)
        jialustr+="("+str(jialux)+","+str(jialuy)+")\n"
        fp1.append(jialux)
        fp2.append(jialuy)
        print("第一個區域加入一個點,要被加入的座標x: %s ,y: %s" % (jialux,jialuy))
      else:
        if fac2<sac2:
          fac2+=1
          jialu-=1
          yi2+=1
          jialux=600
          jialuy=600
          if yi2%2==0:
            jialux-=(yi2/2)*10
            jialux=int(jialux)
          else:
            jialuy-=(yi2/2)*10
            jialuy=int(jialuy)
          jialustr+="("+str(jialux)+","+str(jialuy)+")\n"
          fp1.append(jialux)
          fp2.append(jialuy)
          print("第二個區域加入一個點,要被加入的座標x: %s ,y: %s" % (jialux,jialuy))
        else:
          if fac3<sac3:
            fac3+=1
            jialu-=1
            yi3+=1
            jialux=600
            jialuy=0
            if yi3%2==0:
              jialux-=(yi3/2)*10
              jialux=int(jialux)
            else:
              jialuy+=(yi3/2)*10
              jialuy=int(jialuy)
            jialustr+="("+str(jialux)+","+str(jialuy)+")\n"
            fp1.append(jialux)
            fp2.append(jialuy)
            print("第三個區域加入一個點,要被加入的座標x: %s ,y: %s" % (jialux,jialuy))
          else:
            if fac4<sac4:
              fac4+=1
              jialu-=1
              yi4+=1
              jialux=0
              jialuy=0
              if yi4%2==0:
                jialux+=(yi4/2)*10
                jialux=int(jialux)
              else:
                jialuy+=(yi4/2)*10
                jialuy=int(jialuy)
              jialustr+="("+str(jialux)+","+str(jialuy)+")\n"
              fp1.append(jialux)
              fp2.append(jialuy)
              print("第四個區域加入一個點,要被加入的座標x: %s ,y: %s" % (jialux,jialuy))
      if jialu==0:
        print("加入完成")
        print("所有加入座標:\n %s" % jialustr)
        jialufilename="./moveout_in/"+str(rightnum)+str((rightnum+1))+"movedot.txt"
        jiaf=open(jialufilename,"w")
        jiaf.write("2\n")
        jiaf.write(jialustr)
        jiaf.close()
        print("=============================")
        yiwan=False
    print("所有區域加入( %s, %s, %s, %s)個點" % (yi1,yi2,yi3,yi4))
    print("所有區域剩下( %s, %s, %s, %s)個點" % (fac1,fac2,fac3,fac4))
    print("=============================")
    area1x=[]
    area1y=[]
    area2x=[]
    area2y=[]
    area3x=[]
    area3y=[]
    area4x=[]
    area4y=[]
    for i in range(0,len(fp1)):
      if fp1[i]>300:
        if fp2[i]>300:
          area2x.append(fp1[i])
          area2y.append(fp2[i])
        else:
          area3x.append(fp1[i])
          area3y.append(fp2[i])
      else:
        if fp2[i]>300:
          area1x.append(fp1[i])
          area1y.append(fp2[i])
        else:
          area4x.append(fp1[i])
          area4y.append(fp2[i])
    #print("第一區域內座標:"),
    #for i in range(0,len(area1x)):
    #  print("(%s,%s)" % (area1x[i],area1y[i])),
    #print("\n第二區域內座標:"),
    #for i in range(0,len(area2x)):
    #  print("(%s,%s)" % (area2x[i],area2y[i])),
    #print("\n第三區域內座標:"),
    #for i in range(0,len(area3x)):
    #  print("(%s,%s)" % (area3x[i],area3y[i])),
    #print("\n第四區域內座標:"),
    #for i in range(0,len(area4x)):
    #  print("(%s,%s)" % (area4x[i],area4y[i])),
    print("\n=============================")
    huanwei1=True
    while huanwei1:
      if fac1>sac1:
        fac1-=1
        fac2+=1
        cx,cy,cnum=choosedot(area1x,area1y,1,0)
        print("第一區域移到第二區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area1x[cnum]
        del area1y[cnum]
        area2x.append(cx)
        area2y.append(cy)
      if fac1<sac1:
        fac1+=1
        fac4-=1
        cx,cy,cnum=choosedot(area4x,area4y,4,1)
        print("第四區域移到第一區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area4x[cnum]
        del area4y[cnum]
        area1x.append(cx)
        area1y.append(cy)
      if fac1==sac1:
        print("第一區域完成")
        huanwei1=False
    huanwei2=True
    while huanwei2:
      if fac2>sac2:
        fac2-=1
        fac3+=1
        cx,cy,cnum=choosedot(area2x,area2y,2,0)
        print("第二區域移到第三區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area2x[cnum]
        del area2y[cnum]
        area3x.append(cx)
        area3y.append(cy)
      if fac2<sac2:
        fac2+=1
        fac4-=1
        cx,cy,cnum=choosedot(area4x,area4y,4,2)
        print("第四區域移到第二區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area4x[cnum]
        del area4y[cnum]
        area2x.append(cx)
        area2y.append(cy)
      if fac2==sac2:
        print("第二區域完成")
        huanwei2=False
    huanwei3=True
    while huanwei3:
      if fac3>sac3:
        fac3-=1
        fac4+=1
        cx,cy,cnum=choosedot(area3x,area3y,3,0)
        print("第三區域移到第四區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area3x[cnum]
        del area3y[cnum]
        area4x.append(cx)
        area4y.append(cy)
      if fac3<sac3:
        fac3+=1
        fac4-=1
        cx,cy,cnum=choosedot(area4x,area4y,4,3)
        print("第四區域移到第三區域一個點,被移動的點(%s,%s)" % (cx,cy))
        del area4x[cnum]
        del area4y[cnum]
        area3x.append(cx)
        area3y.append(cy)
      if fac3==sac3:
        print("第三區域完成")
        huanwei3=False
    if fac4==sac4:
        print("全部區域整理完成")
        print("====================================")
    else:
        print("尚有錯誤")
    print("劃分變更後座標...")
    afarea1x=[]
    afarea2x=[]
    afarea3x=[]
    afarea4x=[]
    afarea1y=[]
    afarea2y=[]
    afarea3y=[]
    afarea4y=[]
    for i in range(0,len(sp1)):
        if sp1[i]>300:
            if sp2[i]>300:
                afarea2x.append(sp1[i])
                afarea2y.append(sp2[i])
            else:
                afarea3x.append(sp1[i])
                afarea3y.append(sp2[i])
        else:
            if sp2[i]>300:
                afarea1x.append(sp1[i])
                afarea1y.append(sp2[i])
            else:
                afarea4x.append(sp1[i])
                afarea4y.append(sp2[i])
    #print("第一區域內座標:"),
    #for i in range(0,len(afarea1x)):
    #    print("(%s,%s)" % (afarea1x[i],afarea1y[i])),
    #print("\n第二區域內座標:"),
    #for i in range(0,len(afarea2x)):
    #    print("(%s,%s)" % (afarea2x[i],afarea2y[i])),
    #print("\n第三區域內座標:"),
    #for i in range(0,len(afarea3x)):
    #    print("(%s,%s)" % (afarea3x[i],afarea3y[i])),
    #print("\n第四區域內座標:"),
    #for i in range(0,len(afarea4x)):
    #    print("(%s,%s)" % (afarea4x[i],afarea4y[i])),
    print("\n劃分完成")
    print("====================================")
    print("設定點對點")
    fdot2dot=""
    print("設定第一區域")
    dtd1=True
    bx=area1x
    by=area1y
    ax=afarea1x
    ay=afarea1y
    while dtd1:
      if len(bx)>0:
        cbx,cby,cax,cay,bnum,anum=dot2dot(bx,by,ax,ay)
        del bx[bnum]
        del by[bnum]
        del ax[anum]
        del ay[anum]
        print("(%s,%s)移動到(%s,%s)" % (cbx,cby,cax,cay))
        fdot2dot+=("%s,%s&%s,%s\n" % (cbx,cby,cax,cay))
      if len(bx)==0:
        dtd1=False
    print("第一區域完成")
    print("====================================")
    print("設定第二區域")
    dtd2=True
    bx=area2x
    by=area2y
    ax=afarea2x
    ay=afarea2y
    while dtd2:
      if len(bx)>0:
        cbx,cby,cax,cay,bnum,anum=dot2dot(bx,by,ax,ay)
        del bx[bnum]
        del by[bnum]
        del ax[anum]
        del ay[anum]
        print("(%s,%s)移動到(%s,%s)" % (cbx,cby,cax,cay))
        fdot2dot+=("%s,%s&%s,%s\n" % (cbx,cby,cax,cay))
      if len(bx)==0:
        dtd2=False
    print("第二區域完成")
    print("====================================")
    print("設定第三區域")
    dtd3=True
    bx=area3x
    by=area3y
    ax=afarea3x
    ay=afarea3y
    while dtd3:
      if len(bx)>0:
        cbx,cby,cax,cay,bnum,anum=dot2dot(bx,by,ax,ay)
        del bx[bnum]
        del by[bnum]
        del ax[anum]
        del ay[anum]
        print("(%s,%s)移動到(%s,%s)" % (cbx,cby,cax,cay))
        fdot2dot+=("%s,%s&%s,%s\n" % (cbx,cby,cax,cay))
      if len(bx)==0:
        dtd3=False
      
    print("第三區域完成")
    print("====================================")
    print("設定第四區域")
    dtd4=True
    bx=area4x
    by=area4y
    ax=afarea4x
    ay=afarea4y
    while dtd4:
      if len(bx)>0:
        cbx,cby,cax,cay,bnum,anum=dot2dot(bx,by,ax,ay)
        del bx[bnum]
        del by[bnum]
        del ax[anum]
        del ay[anum]
        print("(%s,%s)移動到(%s,%s)" % (cbx,cby,cax,cay))
        fdot2dot+=("%s,%s&%s,%s\n" % (cbx,cby,cax,cay))
      if len(bx)==0:
        dtd4=False
    print("第四區域完成")
    print("====================================")
    print("座標寫入檔案")
    fdotname="./dot2dot/"+str(rightnum)+str((rightnum+1))+"d2d.txt"
    fdot=open(fdotname,"w")
    fdot.write(fdot2dot)
    fdot.close()
    print("寫入完成")
    print("====================================")

#------------------main process----------------------------------------------  
DIR="./str_2D"
dirnum=len(os.listdir(DIR))
for i in range((dirnum-1)):
  rightnum=i+1
  firstfile="./str_2D/"+str(rightnum)+".txt"
  secondfile="./str_2D/"+str((rightnum+1))+".txt"
  f1=open(firstfile,"r")
  f2=open(secondfile,"r")
  fp1=[]
  fp2=[]
  fdotsum=0
  fac1=0
  fac2=0
  fac3=0
  fac4=0
  sp1=[]
  sp2=[]
  sdotsum=0
  sac1=0
  sac2=0
  sac3=0
  sac4=0
  for line in f1:
    line=line.strip('\n')
    fdotsum+=1
    x=int(line.split(", ")[0])
    y=int(line.split(", ")[1])
    fp1.append(x)
    fp2.append(y)
    if x>=300:
        if y>=300:
            fac2+=1
        else:
            fac3+=1
    else:
        if y>=300:
            fac1+=1
        else:
            fac4+=1
  for line in f2:
    line=line.strip('\n')
    sdotsum+=1
    x=int(line.split(", ")[0])
    y=int(line.split(", ")[1])
    sp1.append(x)
    sp2.append(y)
    if x>=300:
        if y>=300:
            sac2+=1
        else:
            sac3+=1
    else:
        if y>=300:
            sac1+=1
        else:
            sac4+=1
  print("第%s個字有 %s 個點,所有區域分別是 (%s,%s,%s,%s)個" % (rightnum,fdotsum,fac1,fac2,fac3,fac4))
  print("第%s個字有 %s 個點,所有區域分別是 (%s,%s,%s,%s)個" % ((rightnum+1),sdotsum,sac1,sac2,sac3,sac4))
  minusnum=fdotsum-sdotsum
  print("兩字相差 %s 個點" % abs(minusnum))
  print("=========================")
  calculate_yidong(fp1,fp2,fac1,fac2,fac3,fac4,fdotsum,sp1,sp2,sac1,sac2,sac3,sac4,sdotsum,minusnum,rightnum)

