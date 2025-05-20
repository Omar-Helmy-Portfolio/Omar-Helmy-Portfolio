def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    without_d_sign = d.strip("$")
    return float(without_d_sign)


def percent_to_float(p):
    without_p_sign = p.strip("%")
    fraction = float(without_p_sign)/100
    return fraction

main()
