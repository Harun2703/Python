lbs=[]
kgs=[]
x = int(input("Enter the number of students[N] :"))
for i in range(x):
     weights=float(input("Enter input in lbs :"))
     lbs.append(weights)
print("Input in lbs",lbs)
for j in range(x):
    y=0.45*lbs[j]
    kgs.append(y)
print("Output in Kgs",kgs)