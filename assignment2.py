print("Hello there! What's your name?")
name = input("Please enter your name: ")
upper_name = name.upper()
print("Hello "+upper_name+", how tall are you?")
height_cm = float(input("Please enter your height in centimeters: "))

#conversions:
#1 foot = 30.48cm
#1 inch = 2.54cm

#Divide height by 30.48
#Need to deal with the remainder. (Use modulo)

height_ft = height_cm / 30.48
height_ft_int = int(height_ft)
height_ft_remainder = height_ft - height_ft_int
height_ft_remainder = round(height_ft_remainder, 2) #Returns feet as decimal

height_in = height_ft_remainder * 12 #Converts feet to inches
height_in_int = int(height_in)

height_in_remainder = height_in - height_in_int #Returns a decimal of the number of inches remaining. Usually goes to fractions of 64.
height_in_remainder = height_in_remainder * 4 #Increase to fraction of 4
height_in_remainder = round(height_in_remainder, 0) #Remainder to 0 decimal places
height_in_remainder = int(height_in_remainder)
#height_in_remainder = Fraction(height_in_remainder, 4).limit_denominator()

height_ft_str = str(height_ft_int)
height_in_str = str(height_in_int)
height_remainder_str = str(height_in_remainder) + "/4"

#height_ft_str = str(height_ft_int)
#height_in_str = str(height_in_int)
#height_remainder_str = str(height_in_remainder)

print("Dear "+upper_name+", you are "+height_ft_str+" foot, "+height_in_str+" "+height_remainder_str+" in tall")

input("\nPress enter to finish")