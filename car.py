cars = []

print('Please enter your favourite car ')
for i in range(5):
    favcar = input(f"car {i+1} ")
    cars.append(favcar)


print(cars)

for car in cars:
    print(f"My favourite car is {car} ")

