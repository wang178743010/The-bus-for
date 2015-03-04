#coding:utf-8
r1 = "aa bb cc dd  ff gg hh"
r2 = "pp qq vv tt uu cc ee"
bn = "aa"
en = "ee"
rd1=r1.split()
rd2=r2.split()
print rd1,"\n",rd2
if bn in rd1:
    bs = rd1.index(bn)
    print 'find begin station',bs
print "-----is.-----<--->---start--------"
if en in rd2:
    es = rd2.index(en)
    print 'find end station',es
print "-----is-----<--->----end----------"
i = 0
for x1 in rd1:    
    if x1 in rd2:
        ex1 = rd1.index(x1)
        ex2 = rd2.index(x1)
        print x1,rd1.index(x1),"\n",x1,rd2.index(x1)
    i = i + 1
for x in rd1[bs:ex1]:
    print x,'->',
print rd1[ex1]
if ex2<es:
    for x in rd2[ex2:es]:
        print x,'->',
    print rd2[es]
else:
    for x in rd2[ex2:es:-1]:
        print x,'<-',

def findExchange(r1,r2):
    li = []
    for x in r1:
        if x in r2:
            temp = x.r1.index(x),r2.index(x)
