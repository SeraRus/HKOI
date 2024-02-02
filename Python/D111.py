s=input()
BMI=format(float(s.split(' ')[0])/(float(s.split(' ')[1])*float(s.split(' ')[1])),'.3f')
print(BMI)
BMI=float(BMI)
if BMI < 18.5:
  print("Underweight")
elif BMI < 23.0:
  print("Normal")
elif BMI < 25.0:
  print("Overweight")
else:
  print("Obese")
