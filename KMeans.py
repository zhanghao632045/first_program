import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math
#数据
dat = np.array([[14,22,15,20,30,18,32,13,23,20,21,22,23,24,35,18],
                [15,28,18,30,35,20,30,15,25,23,24,25,26,27,30,16]])
print(dat)
#======聚类中心======#
n = len(dat[0])
N = len(dat)*n
k = 3
#-------随机产生-----#
center = rd.sample(range(n),k)
center = np.array([dat.T[i] for i in center])
print('初始聚类中心为：')
print(center)
print('-----------------------')
#计算聚类中心
def cent(x):
   return(sum(x)/len(x))
#计算各点到聚类中心的距离之和
def dist(x):
   #聚类中心
   m0 = cent(x)
   dis = sum(sum((x-m0)**2))
   return(dis)
#距离
def f(center):
   c0 = []
   c1 = []
   c2 = []
   D = np.arange(k*n).reshape(k,n)
   d0 = center[0]-dat.T
   d1 = center[1]-dat.T
   d2 = center[2]-dat.T
   d = np.array([d0,d1,d2])
   for i in range(k):
      D[i] = sum((d[i]**2).T)
   for i in range(n):
      ind = D.T[i].argmin()
      if(ind == 0):
         c0.append(i)#分配类别
      else:
         if(ind == 1):
            c1.append(i)
         else:
            c2.append(i)
   C0 = np.array([dat.T[i] for i in c0])
   C1 = np.array([dat.T[i] for i in c1])
   C2 = np.array([dat.T[i] for i in c2])
   C = [C0,C1,C2]
   print([c0,c1,c2])
   s = 0
   for i in C:
      s+=dist(i)
   return(s,C)
n_max = 50
#初始距离和
print('第1次计算！')
dd,C = f(center)
print('距离和为'+str(dd))
print('第2次计算！')
center = [cent(i) for i in C]
Dd,C = f(center)
print('距离和为'+str(Dd))
K = 3
while(K<n_max):
   #两次差值很小并且计算了一定次数
   if(math.sqrt(dd-Dd)<1 and K>20):
      break;
   print('第'+str(K)+'次计算！')
   dd = Dd
   print('距离和为'+str(dd))
   #当前聚类中心
   center = [cent(i) for i in C]
   Dd,C = f(center)
   K+=1
#---聚类结果可视化部分---#
j = 0
for i in C:
   if(j == 0):
      plt.plot(i.T[0],i.T[1],'ro')
   if(j == 1):
      plt.plot(i.T[0],i.T[1],'b+')
   if(j == 2):
      plt.plot(i.T[0],i.T[1],'g*')
   j+=1
plt.show()


