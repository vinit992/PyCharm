#Global variable
calculation_to_units = 24
name_of_unit = "hours"

#In the days_to_units we are doing calculation only. Doing this we are practing the clean coding

def days_to_units(num_of_days):
    # it will help in debugging to check the value is +ve or -ve
    #print(num_of_days>0)

    #if num_of_days > 0:
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    #elif num_of_days == 0:
     #   return f"you mistakenly enter the day value is zero! Pls Enter a valid value!"

    '''
    else:
        return f"Wrong Input you entered or may be you entered the -ve value!."
'''

#We are validating everthing in the validate_and_execute function

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            number_of_hours = days_to_units(user_input_number)
            print(number_of_hours)
        elif user_input_number == 0:
            print(f"you mistakenly enter the number of day value is 0! That's wrong!!! Pls enter the correct value!")
        else:
            print(f"Wrong Input you entered or may be you entered the -ve value!!!")
    except ValueError:
        print("What input you were enter that's wrong!!! Pls correct Your input!!!!")

#Global variable
user_input = input("Hi user, Enter no. of days and It convert it to hours!\n")

validate_and_execute()

'''
if user_input.isdigit():
    user_input_number = int(user_input)
    number_of_hours = days_to_units(user_input_number)
    print(number_of_hours)

else:
    print("What input you entered that's wrong!!! Pls correct Your input!")
'''


'''
#By default it takes the input as a string so to typecaste string to integer use below function
user_input_number_of_days = int(user_input)

number_of_hours = days_to_units(user_input_number_of_days)

print(number_of_hours)
'''