calculation_to_units = 24
name_of_unit = 'hours'
#number_of_days = 40

def days_to_units(number_of_days,custom_message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

#days_to_units() ==> Give an error
days_to_units(20, "sounds Great")
days_to_units(30,"Awesome")
days_to_units(40,"All Good")
days_to_units(50, "okay, Cool, i got it")


