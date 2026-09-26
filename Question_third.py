# inout student Name and Roll No. and Marks

name = input("Student Name :")

while True:
    try:
        roll_no = int(input("Roll No. :"))
        break  # if Integer is founded then loops break
    except ValueError:
        print("Roll No must be an integer! Please try again.")
marks = []
for i in range(5):
    while True:
        try:
            m = int(input(f"Subject {i+1} marks: "))
            
            # Range check (0 se 100 ke beech hone chahiye)
            if 0 <= m <= 100:
                marks.append(m)
                break  # Sahi marks milne par loop tod kar agle subject par jayega
            else:
                print("Marks must be between 0 and 100 Please try again.")
                
        except ValueError:
            print("Invalid input Marks! Please enter a valid Marks.")

# create Function to total marks
def total(m): return sum(m)
t = total(marks)
# Create Function for Percentage

def percentage(t): return t/5
p = percentage(t)

# Create Function For grade
def grade(p):
    if p>=90 : return "A+"
    elif p>=80: return "A"
    elif p>=70: return "B"
    elif p>=60: return "C"
    else:
        return "Fail"

g = grade(p)

# Print The Values

print(f"Total : {t}, Percentage: {p}% ,Grade:{g}")
print("Schoolership Eligibile" if p>=85 else "Not Eligible")
    