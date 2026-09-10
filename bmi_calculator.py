print("BMI Calculator")

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Please enter positive values.")
            continue

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("BMI:", round(bmi, 2))
        print("Category:", category)

        choice = input("Do you want to calculate again? (yes/no): ")

        if choice.lower() != "yes":
            break

    except ValueError:
        print("Please enter numbers only.")