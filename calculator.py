def cal() :
   while True:
      a,b=[int(x) for x in input("Enter 2 values: ").split()]
      c=str(input('Choose operator(+,-,/,*,**,//): '))
      if c=="+":
         res=a+b
         print('a+b=',res)
      elif c=="-":
         res=a-b
         print('a-b=',res)
      elif c=="*":
         res=a*b
         print('a*b=',res)
      elif c=="/":
         res=a/b
         print('a/b=',res)
      elif c=="**":
         res=a**b
         print('a**b=',res)
      elif c=="//":
         res=a//b
         print('a//b=',res)
      d=input('COntinue?(y/n):')
      if d=='n':
         break
cal()    
