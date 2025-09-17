op,x,y=map(float,input("What operation?\n0.mult\n1.div\n2.add\n3.sub\n4.exp\n5.mod\nGive operation and 2 vars: ").split())
ops={'0':lambda x,y:x*y,'1':lambda x,y:x/y,'2':lambda x,y:x+y,'3':lambda x,y:x-y,'4':lambda x,y:x**y,'5':lambda x,y:x%y}
print("\nans:",ops[str(int(op))](x,y))
