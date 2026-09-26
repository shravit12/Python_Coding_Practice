# Electricity Bill Calculator
def calculate_bill(Unit):
    if Unit <= 100:
        return Unit*5
    elif Unit <=200:
        return 100*5 + (Unit - 100)*8
    else:
       return 100*5+100*8+(Unit-200)*10



    
# Customer Name
C_name = input("Enter Your Name:")
# Consumed Unit aswell Check Unit is in integer or Not
while True:
       try:
            Unit = int(input("Enter Consumed Unit:"))
            break
       except ValueError:
          print("Invalid Unit Please Enter Again")
   
Bill = calculate_bill(Unit)

if Bill < 500:
   cat = "Low Bill"
elif Bill <= 1500:
   cat = "Medium Bill"
else:
   cat = "High Bill"


print(f"\n\nCustomer Name :{C_name}\n Units : {Unit} \n Total Bill: {Bill} \n Bill Category: {cat}")

    
