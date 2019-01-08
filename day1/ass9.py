num = float(input("Enter Salary: "))
if num<=2000:
    print("DA is %fand HRA is %f"%(0.1*num,0.2*num))
elif num>2000 and num<=5000:
    print("DA is %f and HRA is %f "%(0.2*num,0.3*num))
elif num>5000 and num<=10000:
    print("DA is %f and HRA is %f "%(0.3*num,0.4*num))
elif num>10000:
    print("DA is %f and HRA is %f "%(0.5*num,0.5*num))