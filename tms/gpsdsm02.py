import datetime
import math
import numpy as np
import the_pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


BFBK = 10
ZCX = 80  #边际分数
JGX = 60  #全上限 分数， 达标分数

CMB = 0.1  #超温比例达标线，
CWJJ = 0.00 # 超温卷积系数
JWD = 40
JWL = 0.3
CYO = ['D002300116283T1-A','D002300118061T1','D002300118241T1']

def getTemp(pot):
    gpstemp1 =  1000 if pot[7] < -100 else pot[7]
    gpstemp2 =  1000 if pot[8] < -100 else  pot[8]
    gpstemp3 =  1000 if pot[9] < -100 else  pot[9]
    gpstemp4 =  1000 if pot[10] < -100 else  pot[10]
    return  min(gpstemp1,gpstemp2,gpstemp3,gpstemp4)

def fandPot(n,gpsdatas,ss):
    gpst = datetime.datetime.strptime(gpsdatas[n][4], '%Y/%m/%d %H:%M:%S')
    t = getTemp(gpsdatas[n])
    if n < 1:
        return ss
    gpst0 = datetime.datetime.strptime(gpsdatas[n - 1][4], '%Y/%m/%d %H:%M:%S')
    t0 = getTemp(gpsdatas[n-1])
    if t <= gpsdatas[n][1] and t0 <= gpsdatas[n][1] or  ss[2] > JWD :
        ss[1] = 1
        return ss
    lt = (gpst - gpst0).total_seconds() / 60
    if (t0 - t) / lt > JWL:
        ss[0] += (t0 - t)
        ss[2] += lt
    else:
        ss[0] = 0
        ss[2] = 0
    return  ss

def culS(n,gpsdatas, olt, ott):
    stt = datetime.datetime.strptime(gpsdatas[n][2], '%Y/%m/%d %H:%M:%S') # + datetime.timedelta(minutes=0)
    gpst = datetime.datetime.strptime(gpsdatas[n][4], '%Y/%m/%d %H:%M:%S')
    ss =  np.array([0.,0.,0.,0.,0.,0.,0.])
    if gpst < stt:
        return ss
    gpst0 = datetime.datetime.strptime(gpsdatas[n-1][4], '%Y/%m/%d %H:%M:%S') if n > 0 else  gpst + datetime.timedelta(minutes=-2.5)
    gpst1 = datetime.datetime.strptime(gpsdatas[n+1][4], '%Y/%m/%d %H:%M:%S') if n+1 < len(gpsdatas) else  gpst + datetime.timedelta(minutes=2.5)
    blt =  (gpst - gpst0).total_seconds() / 120
    alt =  (gpst1 - gpst).total_seconds() / 120
    ltime =blt +alt
    ht = float(gpsdatas[n][1])
    lt = ht - BFBK if math.isnan(gpsdatas[n][11]) else  float(gpsdatas[n][11])
    stemp0 = (ht + lt) / 2
    ss[0] = (ht - lt)
    tp = getTemp(gpsdatas[n])
    if tp > ht:
        olt = olt + (CWJJ * ltime) if olt > 0 else 1
        ott = ott + ltime if ott > 0 else ltime
        ss[1] = tp - ht
        ss[2] = ht - stemp0
        ss[5] = ss[1] * olt
    elif tp > stemp0:
        ss[2] = tp - stemp0
        olt = 0
        ott = 0
    elif tp > lt:
        ss[3] = stemp0 - tp
        olt = 0
        ott = 0
    else:
        olt = olt - (CWJJ * ltime) if olt < 0 else -1
        ott = ott - ltime if ott < 0 else  -ltime
        ss[4] = lt - tp
        ss[3] = stemp0 - lt
        ss[6] = -ss[4] * olt
    return  ss * ltime,olt, ott

s = pd.read_csv('./order.out')
crrdata = s.values

print(crrdata)
dl= []
otlist= []
for m in np.arange(10, 11, 1):
    dl.append(pd.read_csv('./py'+ str(m) +'.out'))
df =pd.concat(dl)

print('开始分析%d', len(crrdata))
jsq = len(crrdata)
for dn in crrdata:
    jsq -= 1
    if dn[6] == 0 :  #  or  dn[12] > 500  or not math.isnan(gpsdata[0][11])
        continue
    print(jsq)
    gpsdata = df[df['transport_no'].isin([dn[0]])].values
    if gpsdata is None or len(gpsdata) == 0:
        continue
    S = np.array([0.,0.,0.,0.,0.,0.,0.])
    P = np.array([0., 0., 0.])
    olt = 0
    ott = 0
    for j in np.arange(0, len(gpsdata),1) :
        dn[1] = 1
        P = fandPot(j, gpsdata,P)
        if P[1] > 0:
            break
    for i in np.arange(j, len(gpsdata),1) :
        dn[2] = str(gpsdata[i][5]) + '@' + str(gpsdata[i][6])
        tt = ott
        s,olt,ott = culS(i, gpsdata,olt, ott)
        S += s
        if tt != 0 and ott == 0:
            if not math.isnan(gpsdata[0][11]) or tt > 0:
                otlist.append(abs(tt))
    if ott!=0 and (not math.isnan(gpsdata[0][11]) or tt > 0):
        otlist.append(abs(ott))
    if S[0] > 0:
        dn[5] = 1
        if math.isnan(gpsdata[0][11]):
            dn[7] = S[0]/2 - S[2]
            dn[8] = S[1]
            dn[9] = S[2]
            dn[13] = S[5]
        else:
            dn[7] = S[0]/2 - S[2] - S[3]
            dn[8] = (S[1] + S[4])
            dn[9] = (S[2] + S[3])
            dn[13] = (S[5] + S[6])
        dn[4] = 0 if math.isnan(gpsdata[0][11]) else 1 #是否冷藏
sp = pd.DataFrame(crrdata)
needgps =  sp[sp[6] >0]
hgpsO= needgps[(needgps[7] >0) ] #  & (needgps[4] ==1)
hgpsc = len(hgpsO)
mf = hgpsO[(hgpsO[8] ==0) & (hgpsO[9] ==0) & (hgpsO[4] ==0) ]
mk = hgpsO[hgpsO[13] == 0 ]
print(mf)
print(mk)
print('冷运单据：%d, 需跟踪单据：%d ' %(len(crrdata) ,len(needgps)))
print('跟踪单数：%d，跟踪率%.1f%%' %(hgpsc, hgpsc/len(needgps)*100))

xn = np.arange(1, 0.0, -0.01)
y = []
z = []
M = []
S =[]
for x in xn:
    md = np.mat(hgpsO[[7, 8, 9,13]].values)
    m = (100/(JGX * x))
    M.append(m)
    mv = md * np.mat([1, 0, 100/ZCX, m]).T
    mm = md * np.mat([1, 0, 1, 1]).T
    ms = 100 * mm / mv
    mp = pd.DataFrame(ms)

    S.append(mp[0].mean())
    l = 100 * round(len(mp[mp[0] >= JGX]) / len(mp), 3)
    y.append(l)
    print('达标率',ms,'达标率',l,'M值',m)
plt.suptitle('边际分数为%d，及格分数为%d，降温段时间%d分钟, 降温识别速率%.2f度/分钟, 冷冻区温度范围%d度,'
             ' 连续超温卷积系数%.2f' % (ZCX,JGX, JWD, JWL, BFBK, CWJJ))
plt.subplot(2, 3, 1)
plt.title('按不同超温比例作为及格线对应的M值、达标占比、平均分')
plt.plot(M, y, 'b')
# plt.plot(xn, M, 'r')
plt.plot(M, S, 'g')
plt.xlabel('超温区面积比: 红线-M值，蓝线-及格率，绿线-平均分')

md = np.mat(hgpsO[[7, 8, 9,13]].values)
mc = md * np.mat([1,0, 100/ZCX, 7.6]).T #  & (needgps[4] ==1)
mm = md * np.mat([1,0, 1, 1]).T
msc = 100 * mm /mc
mscp = pd.DataFrame(msc)
print(mscp[mscp[0] == 100])
plt.subplot(2, 3, 2)
plt.subplots_adjust(wspace=0.2, hspace=0)
plt.title('如果超温区占比低于%d%%为及格其分数分布'% (CMB*100))
plt.xlabel('分数')
plt.ylabel('单数')
plt.text(50,hgpsc/20,'及格率%0.1f%%' % round(100*len(mscp[mscp[0] >= JGX]) / len(mscp), 3))
plt.hist(msc, bins=20, facecolor='b', alpha=0.3)

mv = md * np.mat([0, 0, 0, 1]).T
ms = mv / mm
plt.subplot(2, 3, 3)
plt.subplots_adjust(wspace=0, hspace=0.3)
plt.title('卷积超温比例的单据分布')
plt.xlabel('卷积超温区面积比')
plt.ylabel('单数')
plt.text(0.5,hgpsc/20,'无超温单率%0.1f%%' % round((100 *len(hgpsO[hgpsO[13] == 0])/hgpsc ), 3))
plt.hist(ms, bins=20, facecolor='r', alpha=0.3)

mm = md * np.mat([1,1,1,0]).T
mvs = md * np.mat([0,0,1,0]).T
mss = mvs / mm
plt.subplot(2, 3, 4)
plt.subplots_adjust(wspace=0.2, hspace=0.3)
plt.title('标准波动区比例的单据分布')
plt.xlabel('波动区面积比')
plt.ylabel('单数')
plt.hist(mss,bins=20 ,facecolor='g', alpha=0.3)

plt.subplot(2, 3, 5)
otlp = pd.DataFrame(otlist)
plt.subplots_adjust(wspace=0.2, hspace=0.3)
plt.title('单次超温时长分布情况')
plt.xlabel('单次超温时长-分钟')
plt.ylabel('单数')
plt.xlim(0,300)
weights = np.ones_like(otlist)/float(len(otlist))
plt.text(70,0.3,'平均：%d，最大值：%d，最小值：%d' % (otlp[0].mean(),otlp[0].max(),otlp[0].min() ))
plt.hist(otlist, weights=weights, bins=1200 ,facecolor='g', alpha=0.3)

mv = md * np.mat([0,1,0,0]).T
ms = mv / mm
plt.subplot(2, 3, 6)
plt.subplots_adjust(wspace=0.2, hspace=0.3)
plt.title('标准超温比例的单据分布')
plt.xlabel('超温区面积比')
plt.ylabel('单数')
plt.hist(ms, bins=20 ,facecolor='r', alpha=0.3)


plt.show()


