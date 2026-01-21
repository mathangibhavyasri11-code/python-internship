# loop_tasks.py
# Demonstration of loops and conditions in Python
print("1. Print numbers from 1 to 100 using for loop")
for i in range(1, 101):
    print(i, end=" ")
print("\n")
# --------------------------------------------------
print("2. Countdown timer using while loop")
count = 10
while count > 0:
    print(count)
    count -= 1
print("Countdown finished!\n")
# --------------------------------------------------
print("3. Using break and continue")
for i in range(1, 11):
    if i == 4:
        print("Skipping 4")
        continue
    if i == 8:
        print("Stopping at 8")
        break
    print(i)
print()
# --------------------------------------------------
print("4. Iterate over string characters")
text = "Python"
for ch in text:
    print(ch)
print()
# --------------------------------------------------
print("5. Multiplication table of a number")
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
print()
# --------------------------------------------------
print("6. Using range with steps (even numbers)")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")
# --------------------------------------------------
print("7. Combine loops with conditions")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
print()
# --------------------------------------------------
print("8. Real-world example: Shopping cart budget check")
prices = [120, 250, 300, 180, 90]
budget = 600
total = 0
for price in prices:
    if total + price > budget:
        print("Budget exceeded! Cannot add item worth", price)
        break
    total += price
    print("Added item worth", price)
print("Total bill:", total)
print()
# --------------------------------------------------
print("9. Real-world example: Attendance system")
students = ["Ravi", "Anu", "Kiran", "Sita"]
for student in students:
    if student == "Anu":
        continue
    print(student, "is present")
