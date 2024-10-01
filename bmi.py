# first code to push
def calculate_bmi_with_meaning():
    # Ask user for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    return (bmi)

# Example usage:
bmi = calculate_bmi_with_meaning()
print(f"BMI: {bmi:.2f}")
     
