
# Pass in the required parameters
def calculate_temperature(val, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in ['c', 'f', 'k']:
        raise ValueError("Invalid from_unit. Use 'c', 'f', or 'k'.")
    if to_unit not in ['c', 'f', 'k']:
        raise ValueError("Invalid to_unit. Use 'c', 'f', or 'k'.")
    # Convert the temperature
    if from_unit == 'c':
        if to_unit == 'f':
            return round((val * 9 / 5),2) + 32
        elif to_unit == 'k':
            return val + 273.15
        else:
            return val
    elif from_unit == 'f':
        if to_unit == 'c':
            return round((val - 32) * 5 / 9,2)
        elif to_unit == 'k':
            return round((val - 32) * 5 / 9,2) + 273.15
        else:
            return val
    elif from_unit == 'k':
        if to_unit == 'c':
            return val - 273.15
        elif to_unit == 'f':
            return round((val - 273.15) * 9,2) / 5 + 32
        else:
            return val
    

if __name__ == '__main__':
    source = input("Enter the temperature you want to convert(unit: C, F, or K): ")
    source = source.split()
    val = float(source[0])
    from_unit = source[1]
    to_unit = input("Enter the unit you want to convert to(unit: C, F, or K): ")
    print(f"The temperature {val} {from_unit} is {calculate_temperature(val, from_unit, to_unit)} {to_unit}")