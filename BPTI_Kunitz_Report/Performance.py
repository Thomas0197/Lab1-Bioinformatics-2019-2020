#!/usr/bin/python
import sys, math

def get_blast(filename):
  flist=[]
  d={}
  c =0
  f=open(filename)
  for line in f:
    v=line.rstrip().split()
    d[v[0]]=d.get(v[0],[])
    d[v[0]].append([float(v[1]),int(v[2])])
    c = c + 1
  f.close()
  for v in d.values():
    v.sort()
    flist.append(v[0])
  return flist


def get_cm(data,th):
  # CM=[[TP,FP],[FN,TN]]
  # 0 = Negatives 1=Positives
  cm=[[0.0,0.0],[0.0,0.0]]
  cList = []
  tList = []
  c = 1
  for i in data:
    if i[0]<th and i[1]==1: 
      cm[0][0]=cm[0][0]+1
    if i[0]>=th and i[1]==1:
      cm[1][0]=cm[1][0]+1
      tList.append(c)
    if i[0]<th and i[1]==0:
      cm[0][1]=cm[0][1]+1
      cList.append(c)
    if i[0]>th and i[1]==0:
      cm[1][1]=cm[1][1]+1
    c = c +1
  #print (cList)
  #print (tList)
  return cm
		
def get_id(filename):
	data = []
	f = open(filename)
	for line in f:
		v=line.rstrip().split()
		data.append([v[0], float(v[1]),int(v[2])])
	return data
			

def get_acc(cm):
  return float(cm[0][0]+cm[1][1])/(sum(cm[0])+sum(cm[1]))


def mcc(m):
  d=(m[0][0]+m[1][0])*(m[0][0]+m[0][1])*(m[1][1]+m[1][0])*(m[1][1]+m[0][1])
  return (m[0][0]*m[1][1]-m[0][1]*m[1][0])/math.sqrt(d)



if __name__ == "__main__":
  filename=sys.argv[1]
  data=get_blast(filename) 
  #print(get_id(filename) ) 
  for i in range(20):
    th=10**-i
    cm, clist=get_cm(data,th)
    print ('TH:',th,'ACC:',get_acc(cm),'MCC:',mcc(cm),cm)
