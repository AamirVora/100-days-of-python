# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))


# This is how you work out whether if a particular year is a leap year.
#
# - on every year that is divisible by 4 with no remainder
#
# - except every year that is evenly divisible by 100 with no remainder
#
# - unless the year is also divisible by 400 with no remainder

# e.g. The year 2000:
#
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
#
#
#
# But the year 2100 is not a leap year because:
#
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)



def is_leap_year(year):
    leap_year = True
    if year % 4 == 0 or year % 400 == 0:
        print("leap year")
        leap_year = True

    if year % 100 == 0 or year % 400 != 0:
        print("not leap year")
        leap_year = False

    if year % 400 == 0:
        print("leap year")
        leap_year = True


is_leap_year(2000)