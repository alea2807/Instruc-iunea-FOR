#problema 6
num=eval(input("Introduceti num: "))
s1=0
s2=0
s3=1
s4=0
s5=0
s6=0
c=1
for i in range (1, num+1):
    s1+=i
    s2+=(i-1)*i
    c*=i
    s3+=c
    s4+=i**2
    s5+=i/(i+1)
    s6+=i*2
print(s1,s2,s3-1,s4,s5,s6)