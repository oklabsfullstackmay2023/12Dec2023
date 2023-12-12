teachers = []

print(f'Please enter your favourate teacher ')
for i in range(4):
    favteacher = input(f"teacher {i+1} ")
    teachers.append(favteacher)

print(teachers)
for teacher in teachers:
    print(f'My fav teacher is {teacher} ')