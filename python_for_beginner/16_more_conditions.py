# BMI = Weight / (Height ** 2)
user_weight = float(input("Please input your weight(kg):"))
user_height = float(input("Please input your height(meter):"))
user_BMI = user_weight / (user_height ** 2)
print("Your BMI is ", user_BMI)

if user_BMI <= 18.5:
    print("偏瘦")
elif 18.5 < user_BMI <= 25:
    print("正常")
elif 25 < user_BMI <= 30:
    print("偏胖")
else:
    print("肥胖")
