# Ask the user for weight and height
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Print BMI
print("Your BMI is:", bmi)

# Health recommendation based on BMI
if bmi > 25:
    print("You are overweight. You need to work out more and watch your diet.")
elif bmi >= 18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")
