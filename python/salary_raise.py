def calculate_salary(value, perc):
    growth = value * (perc/100)
    new_sal = growth + value
    print(new_sal)


calculate_salary(100, 10)