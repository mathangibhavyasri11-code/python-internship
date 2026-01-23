# TASK 6: Lists, Tuples & Sets
# collections_demo.py

print("---- LISTS, TUPLES & SETS DEMO ----\n")

# 1 & 2. Store student names in a list
students = ["Anu", "Ravi", "Sita", "Anu", "Kiran"]
print("Original student list:", students)

# 3. Add, remove, sort elements
students.append("Meena")
print("\nAfter adding Meena:", students)

students.remove("Ravi")
print("After removing Ravi:", students)

students.sort()
print("After sorting:", students)

# 4. Use tuple for fixed data
college_info = ("ABC College", "CSE", 2025)
print("\nTuple (fixed data):", college_info)

# 5. Convert list to set to remove duplicates
student_set = set(students)
print("\nAfter removing duplicates using set:", student_set)

# 6. Perform set operations
set1 = {"Anu", "Sita", "Kiran"}
set2 = {"Kiran", "Meena", "Raju"}

print("\nSet 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (Set1 - Set2):", set1 - set2)

# 7. Iterate over collections
print("\nIterating over student set:")
for name in student_set:
    print(name)

# 8. Compare mutable vs immutable
print("\nMutable vs Immutable:")
print("List is mutable (can change):", students)
print("Tuple is immutable (cannot change):", college_info)

# 9. Print formatted output
print("\n---- FORMATTED OUTPUT ----")
print(f"Total students (unique): {len(student_set)}")
print(f"College: {college_info[0]}, Branch: {college_info[1]}")
