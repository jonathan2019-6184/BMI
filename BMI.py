#Determining Body Mass Index (BMI) 

#Following is a chart for determining one’s body mass index (BMI). BMI is a general  indication of the amount of body fat that a person has. The formula for computing BMI  is,  
#BMI = mass / height2 
#Implement a Python program that prompts a user for their height and weight. Height  should be entered as inches and weight should be entered in pounds. Perform the  calculation in units of kilograms and meters as shown in the chart. Compare the result to  the information in the chart. Use class(es) in your program design. 


def main():
    bmi()
    

#define variables
get_height = 0.0
get_weight = 0.0
body_mass_index = 0.0


#We will start with the introduction to our BMI (Body Mass Index)
def bmi():
    print("Welcome to my BMI calculator!")
    print("If you can tell me your weight and height")
    print("I can tell you your Body Mass Index")
    print("Thank You!\n")

#From this point I will ask the user for his/her information.

get_height = float(input("Please enter your height in inches. "))
get_weight = float(input("Please enter your weight in pounds. "))

#user will enter there information above and we will then calcualte.
body_mass_index = (get_weight * 703) / (get_height ** 2)




if body_mass_index < 18.5:
    print("A person with a BMI of " + str(body_mass_index ) + " is underwieght ")
elif body_mass_index < 24.9:
    print("A person with a BMI of " + str(body_mass_index ) + " is normal weight ")
elif body_mass_index < 30:
    print("A person with a BMI of " + str(body_mass_index ) + " is overweight ")
elif body_mass_index >30:
    print("A person with a BMI of" + str(body_mass_index) + "is obese" )

main()