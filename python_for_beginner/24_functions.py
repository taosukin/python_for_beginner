def calculate_BMI(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        category = '偏瘦'
    elif BMI <= 25:
        category = '正常'
    elif BMI <= 30:
        category = '偏胖'
    else:
        category = '肥胖'
    print(f'Your BMI category is: {category}')
    return BMI


calculate_BMI(1.75, 75)
