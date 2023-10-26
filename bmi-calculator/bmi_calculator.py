
def getBMI(weight, height):
    try:
        bmi = round(float(weight)/float(height)**2, 1)
        return bmi
    except:
        print('Please input correct informations')

def getCategories(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi <= 24.9:
        return 'Normal'
    elif bmi <= 29.9:
        return 'Overweight'
    else:
        return 'Obese'

if __name__ == '__main__':
    weight = input('Enter your weight (kg):')
    height = input('Enter your height (m):')
    bmi = getBMI(weight, height)
    if bmi:
        category = getCategories(bmi)
        print(
f"""Your BMI is {bmi}
Category: {category}""")