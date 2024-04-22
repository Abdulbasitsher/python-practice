print("Welcome to printing lists")

heights_of_students = input("Enter the height_of students ").split()

for n in range(0,len(heights_of_students)):
    heights_of_students[n] = int(heights_of_students[n])
aver = 0
i = 0
for n in heights_of_students:
    aver += n
    i += 1
print(aver/i)
