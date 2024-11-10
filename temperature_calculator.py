def tempconversion():
    print("[1] Celsius to Fahrenheit")
    print("[2] Fahrenheit to Celsius")
    print("[3] Celsius to Kelvin")
    print("[4] Kelvin to Fahrenheit")
    print("[5] Fahrenheit to Kelvin")
    print("[6] Kelvin to Celsius")
    print("[0] Exit the program")


tempconversion()
selectedOption = int(input("Enter an option  :"))

while selectedOption != 0:
    if selectedOption == 1:
        userEntry = input("Enter temperature Celsius you want to convert :")
        calcFigure = int(userEntry)
        celsiusToFahrenheit = (calcFigure * 9) /5 + 32
        print(f"{userEntry} degrees Celsius is equal to {celsiusToFahrenheit} degrees Fahrenheit.")
        break

    if selectedOption == 2:
        userEntry = input("Enter temperature Fahrenheit you want to convert :")
        calcFigure = int(userEntry)
        fahrenheitToCelsius = ((calcFigure - 32) * 5) / 9
        print(f"{userEntry} degrees Fahrenheit is equal to {fahrenheitToCelsius} degrees Celsius")
        break

    if selectedOption == 3:
        userEntry = input("Enter temperature Celsius you want to convert :")
        calcFigure = int(userEntry)
        celsiusToKelvin = (calcFigure + 273.15)
        print(f"{userEntry} degrees Celsius is equal to {celsiusToKelvin} degrees Kelvin")
        break

    if selectedOption == 4:
        userEntry = input("Enter temperature Kelvin you want to convert : ")
        calcFigure = float(userEntry)
        kelvinToFahrenheit = ((calcFigure - 273.15) * (9 / 5)) + 32
        print(f"{userEntry} degrees Kelvin is equal to {kelvinToFahrenheit} degrees Fahrenheit")
        break

    if selectedOption == 5:
        userEntry = input("Enter temperature Fahrenheit you want to convert : ")
        calcFigure = int(userEntry)
        fahrenheitToKelvin = ((calcFigure - 32) * 5) / 9 + 273.15
        print(f"{userEntry} degrees Fahrenheit is equal to {fahrenheitToKelvin} degrees Kelvin ")
        break

    if selectedOption == 6:
        userEntry = input("Enter temperature Kelvin you want to convert :")
        calcFigure = float(userEntry)
        kelvinToCelsius = calcFigure - 273.15
        print(f"{userEntry} degrees Kelvin is equal to {kelvinToCelsius} degrees Celsius")
        break

    else:
        print("You entered an invalid option!")
        break

print("Thanks for using the program.")








