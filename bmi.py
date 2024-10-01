# create a pull request with that changes
def calculate_bmi_with_meaning():
    # Ask user for weight and height
    weight = float(input("Enter your weight in kilograms: 57"))
    height = float(input("Enter your height in meters: 154"))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine BMI category
    if bmi < 18.5:
        meaning = "Underweight"
    elif 18.5 <= bmi < 24.9:
        meaning = "Normal weight"
    elif 25 <= bmi < 29.9:
        meaning = "Overweight"
    else:
        meaning = "Obesity"

    # Return both BMI value and its meaning
    return (bmi, meaning)

# Example usage:
bmi, meaning = calculate_bmi_with_meaning()
print(f"BMI: {bmi:.2f}, Meaning: {meaning}")
