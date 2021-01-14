### Packaging
# Ref https://www.geeksforgeeks.org/convert-python-script-to-exe-file/
# pip install pyinstaller
# 
###

### 
# Ideally would like to restrict during input stage itself to not allow any invalid value using below commented Logic
# But since the use case suggest to have Invalid as response modifying the logic

#measurment_units = {"1": "Kelvin", "2": "Celsius", "3": "Fahrenheit", "4": "Rankine"}
# print ("""Temperature Measurement Unit Type's and mapped option Number,
#     option 1 - Kelvin
#     option 2 - Celsius
#     option 3 - Fahrenheit
#     option 4 - Rankine""")

# while iterations < 3:
#     input_option = input("\nChoose option number based on Input Unit Type:\t\t")
#     target_option = input("Choose option number based on Target Unit Type:\t\t")
#     if input_option not in measurment_units or target_option not in measurment_units:
#         iterations += 1
#         print("Invalid option selected. Please enter number between 1 to 4 based on Unit Type. ** Attempts Left: ", 3-iterations)
#         continue
#     elif input_option == target_option:
#         iterations += 1
#         print("Invalid option selected. Both Input and Target Unit Type is Same. ** Attempts Left: ", 3-iterations)
#         continue
#     break
# print ("Temperature Conversion is from", measurment_units[input_option], "to", measurment_units[target_option])
###

def temperature_conversion(target_unit, input_unit, input_temperature):
    ### Conversion Logic
    ## To Kelvin Conversion
    if target_unit.casefold() == "kelvin":
        if input_unit.casefold() == "celsius":
            expected_response = input_temperature+273.15
        elif input_unit.casefold() == "fahrenheit":
            expected_response = ((input_temperature-32)/1.8)+273.15
        else:
            expected_response = ((input_temperature-491.67)/1.8)+273.15
    ## To Celsius Conversion
    elif target_unit.casefold() == "celsius":
        if input_unit.casefold() == "kelvin":
            expected_response = input_temperature-273.15
        elif input_unit.casefold() == "fahrenheit":
            expected_response = (input_temperature-32)/1.8
        else:
            expected_response = ((input_temperature-491.67)/1.8)
    ## To Fahrenheit Conversion
    elif target_unit.casefold() == "fahrenheit":
        if input_unit.casefold() == "kelvin":
            expected_response = 1.8*(input_temperature-273.15)+32
        elif input_unit.casefold() == "celsius":
            expected_response = 1.8*(input_temperature)+32
        else:
            expected_response = (input_temperature-491.67)+32
    ## To Rankine Conversion
    else:
        if input_unit.casefold() == "kelvin":
            expected_response = ((input_temperature-273.15)*1.8)+491.67
        elif input_unit.casefold() == "celsius":
            expected_response = 1.8*(input_temperature)+491.67
        else:
            expected_response = (input_temperature-32)+491.67
    return expected_response

print ("\nInfo: Valid Temperature Units - Kelvin, Celsius, Fahrenheit and Rankine")
print ("\nInputs")

iterations = 0
valid_flag = True

## Allowing Teacher to feed in the values
input_temperature = input("Enter the Input Value of Temperature:\t\t")

### Ensuring Input and Target Unit Of Measure is not Identical
while iterations < 3:
    input_unit = input("Enter Input Unit Of Measure:\t\t\t")
    target_unit = input("Enter Target Unit Of Measure:\t\t\t")
    if input_unit.casefold() == target_unit.casefold():
        iterations += 1
        print("Info: Both Input and Target Unit Type can not be Same. ** Attempts Left: ", 3-iterations)
        continue
    break
if iterations == 3:
    print ("\nInfo: Exiting Program as allowed attempts exceeded. Please seek assistance from Support")
    exit()

student_response = input("Enter the Student Response of Temperature:\t")

## Checking for Validity of Input
try:
    input_temperature = float(input_temperature)
except ValueError:
    print("Info: Input Temperature is non-numeric/Invalid")
    valid_flag = False
if input_unit.casefold() not in ["kelvin", "celsius", "fahrenheit", "rankine"]:
    print ("Info: Input Unit of Measure -", input_unit.casefold() , "is Invalid")
    valid_flag = False
if target_unit.casefold() not in ["kelvin", "celsius", "fahrenheit", "rankine"]:
    print ("Info: Target Unit of Measure -", target_unit.casefold() , "is Invalid")
    valid_flag = False

if valid_flag == True:
    ## Feeding Student Response and checking if it is valid value
    try:
        student_response =  float(student_response)
    except ValueError:
        print ("\nOutput - Incorrect")
        exit()
    expected_response = temperature_conversion(target_unit, input_unit, input_temperature)
else:
    print ("\nOutput - Invalid")
    exit()

if round(expected_response, 1) == round(student_response, 1):
    print ("\nOutput - Correct")
else:
    print ("\nOutput - Incorrect")
