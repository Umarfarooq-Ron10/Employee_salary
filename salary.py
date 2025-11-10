import sys
if len(sys.argv)==2:
  script_salary=sys.argv[0]
  salary=sys.argv[1]
else:
  scrip_salary=sya.argv[0]
  salary=float(sys.argv[1])
  bonus=0.10*salary
  total_salary=salary*bonus
print("Bonus Amount:",bonus)
print("Total Salary:",total_salary)
