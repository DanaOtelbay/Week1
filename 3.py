stu = int(input())
app = int(input())

app_ev = app//stu
app_os = app - (app_ev*stu)
if stu==app:
   print("0")
elif app_os==0:
   print(app_os)
else:
   print(stu-app_os)