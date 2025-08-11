import matplotlib.pyplot as plt

print("\n----------------------------------------------------------------\n")
print("This program will demonstrate to you the Collatz Conjecture.")
print("The conjecture goes as follows:\n")
print("Take a positive integer 'N'.\nIf 'N' is even, divide 'N' by 2.\nIf 'N' is odd, multiple 'N' by 3 and add 1.")
print("After the appropriate operation, continue to repeat this with the answer you just found.")
print("No matter the positive integer you choose, the sequence always reaches 1\n")

while True:
    seed = int(input("Please enter a positive integer: "))
    if seed % 1 != 0:
        print("Invalid, please try again.\n")

    else:
        valid = 0
        break

altitude = seed
maxAltitude = seed
count = 0

y_altitudes = []
x_count = []

print("\nSequence:")
print(altitude)
while altitude != 1:
    if altitude % 2 == 0: #Even Numbers
        altitude  = altitude / 2
        count += 1
        print(int(altitude))

    else: #Odd Numbers
        altitude = (altitude * 3) + 1
        if altitude > maxAltitude:
            maxAltitude = altitude
        count += 1
        print(int(altitude))
    
    y_altitudes.append(altitude)
    x_count.append(count)

print("\n----------------------------------------------------------------\n")
print("Seed: N =", seed)
print("Max Altitude:", int(maxAltitude))
print("Count:", count)
print("\n----------------------------------------------------------------\n")

plt.plot(x_count, y_altitudes, color='green', marker='o', markerfacecolor='blue')

plt.title("Altitudes Visualized")
  
plt.xlabel('Count')
plt.ylabel('Altitude')

plt.ylim(1, max(y_altitudes))
plt.xlim(1, max(x_count))

plt.show()

