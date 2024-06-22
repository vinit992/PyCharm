calculation_to_units = 24
name_of_unit = 'hours'
#number_of_days = 40

def days_to_units(number_of_days,custom_message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)
def scope_check():
    print(name_of_unit) # Global Variable run without any hustle
    print(number_of_days) # here Number of days act as a Local Variable so it will give an error e.g. "number of days is not defined"

#days_to_units() ==> Give an error

days_to_units(20, "sounds Great")
days_to_units(30,"Awesome")
days_to_units(40,"Looks Cool")
days_to_units(50, "okay, Cool, i got it")
scope_check()


