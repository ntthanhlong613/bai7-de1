n=int(input())
tien=0
if n<101:
    tien=n*2000
if n>100 and n<201:
    tien=100*2000+(n-100)*3000
if n>200 and n<301:
    tien=100*2000+100*3000+(n-200)*5000
if n>300:
    tien=100*2000+100*3000+100*5000(n-300)*10000
print(tien)