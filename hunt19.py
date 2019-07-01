num=int(input())
for i in range(2,num+1):
  if(num%i==0):
    t=0
    for s in range(2,i+1):
      if(i%s==0) and (s!=i):
          t=1
          break
    if(t==0):
          print(i,end="")
