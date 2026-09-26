# Employees Name and Salery 
name = input("Enter Your Name :")
while True:
       try:
             basic = int(input("Enter Your Salery:"))
             break
       except ValueError:
             print("Salery Not Corrected Re-Enter")


def HRA(basic):
    return basic*0.20

def DA(basic):
    return basic*0.15

hra = HRA(basic)
da = DA(basic)

total = basic+hra+da

def TAX(total):
    if basic>50000:
        return basic*0.10 
    else:
        return basic*0.05

tax = TAX(total)
salery = total - tax

print(f"\n\n Employee Name = {name}\n Basic Salery = {basic}\n HRA = {hra}\n DA = {da}\n TAX = {tax}\n Total Salery = {salery}")




    