import re
import csv
from tabulate import tabulate

def main():

    gender = input("What's your gender? ")
    if not re.search(r"^\b(?:male|female|m|f)\b", gender, re.IGNORECASE):
        print('Please retry. (i.e male/female)')
        main()

    while True:
        try:
            age = int(input("How old are you? "))
            break
        except ValueError:
            print('Please retry. (i.e 18)')
            continue
    
    while True:
            weight = input("What's your weight? ")
            if weight_data := re.search(r"^([0-9]+\.?[0-9]+) ?(lbs|pounds|kilograms|kg)$", weight, re.IGNORECASE):
                if weight_data.group(2) == 'lbs' or weight_data.group(2) == 'pounds':
                    formatted_weight = float(weight_data.group(1)) * 0.453592
                    break
                else:
                    formatted_weight = float(weight_data.group(1))
                    break
            else:
                print('Please retry. (i.e 60kg)')
                continue

    while True:
            height = input("Whats's your height? ")
            #cm and m
            if height_data := re.search(r"^([0-9]+(?:\.[0-9]+)?) ?(cm|centimeters|meters|m)$", height, re.IGNORECASE):
                if height_data.group(2) == 'centimeters' or height_data.group(2) == 'cm':
                    formatted_height = float(height_data.group(1)) / 100
                    break
                else:
                    formatted_height = float(height_data.group(1))
                    break

            #ft and in
            elif height_data := re.search(r"^([0-9]{1}) ?(ft|feet|foot|'{1}) ?([0-9]{1}) ?(in|inches|'')$", height, re.IGNORECASE):
                n1 = float(height_data.group(1)) * 0.3048
                n2 = float(height_data.group(3)) * 0.0254
                formatted_height = n1 + n2
                break

            else:
                print('Please retry. (i.e 1.8m / 6ft 1in)')
                continue
    
    print('''What's your activity level?
Sedentary (little or no exercise)
Lightly active (light exercise/sports 1-3 days/week)
Moderately active (moderate exercise/sports 3-5 days/week)
Very active (hard exercise/sports 6-7 days a week)
          ''')
    
    while True:
        act_lvl = input("Activity level: ")

        if lvl := re.search(r"^(sedentary|lightly active| moderately active|very active)$", act_lvl, re.IGNORECASE):
            act_lvl = lvl.group(1).lower()
            break
        else:
            print('Please retry. (i.e Sedentary)')
            continue

    bmi = bmi_calc(formatted_weight, formatted_height)
    print(f"BMI: {bmi}")

    if 0 < bmi <= 18.5:
        print('You are underweight and have to gain weight')
    elif 18.5 < bmi <= 24.9:
        print('You have a normal weight and have to maintain weight')
    elif bmi >= 25.0:
        print('You are overweight and have to lose weight')

    dci = round(calorie_intake(bmi, gender, age, formatted_weight, formatted_height, act_lvl),2)
    print(f"Daily calorie intake: {dci}calories")
    
    list_of_lists_of_meals = meal_plan()
    final_list = regulator(list_of_lists_of_meals, dci)
    meal_types = ['Breakfast','Shake','Lunch','Snack','Dinner']
    for finallist, mealtype in zip(final_list, meal_types):
        print(mealtype)
        print(tabulate(finallist, headers='keys', tablefmt="grid"))

def bmi_calc(weight, height):

    return round(weight / (height ** 2),2)

def calorie_intake(bmi, gender, age, weight, height, act_lvl):

    #DCI=BMR×Activity Level Factor

    if gender == 'male' or gender == 'm':
        bmr = round(88.362+(13.397 * weight) + (4.799 * height * 100) - (5.677 * age))
    else:
        bmr = round(447.593+ (9.247 * weight)+ (3.098 * height * 100) - (4.330 * age))

#determine basic daily calorie intake(without considering surplus/deficit)
    if act_lvl == 'sedentary':
        dci = bmr * 1.2
    elif act_lvl == 'lightly active':
        dci = bmr * 1.375
    elif act_lvl == 'moderately active':
        dci = bmr * 1.55
    else:
        dci = bmr * 1.725

#determine actual calorie intake adhering to goals
    #surplus
    if 0 < bmi <= 18.5:
        dci += 400
    #maintenance
    elif 18.5 < bmi <= 24.9:
        pass
    #deficit
    elif bmi >= 25.0:
        dci -= 700
    
    return round(dci,2)

def meal_plan():
    all_meals = []
    #breakfast, shake, lunch, snack, dinner
    csv_files = ['breakfast.csv','shake.csv','lunch.csv','snack.csv','dinner.csv']
    for file_csv in csv_files:
        meal_dict = []
        with open(file_csv) as file:
            reader = csv.DictReader(file)
            for row in reader:
                meal_dict.append({'Food':row['Food'], 'Amount':row['Amount'], 'Calories':row['Calories'], 'Protein(g)':row['Protein(g)'], 'Carbs(g)':row['Carbs(g)'], 'Fat(g)':row['Fat(g)']})
            all_meals.append(meal_dict)
    return all_meals

def regulator(list_of_lists_of_meals, dci):
    #cal for each meal
    cal_per_meal = dci / 5
    changes = ['Blueberries','Cooked white or brown rice','Natural peanut butter','Mixed nuts','Cooked lean beef']
    for meal in list_of_lists_of_meals:
        base_cal = 0
    #meal is breakfast/shake/lunch/snack/dinner
        for dicts in meal:
        #dict is dict of food item
            if dicts.get('Food') != 'TOTAL' and dicts.get('Food') not in changes:
                base_cal += float(dicts['Calories'])
            if dicts.get('Food') in changes:
                food_cal = float(dicts['Calories'])
                coefficient = (cal_per_meal-base_cal) / food_cal
                original_amt, _ = dicts['Amount'].split(' ')
                dicts['Amount'] = f"{round(float(original_amt) * coefficient)} g"

                dicts['Calories'] = round(float(dicts['Calories']) * coefficient)
                new_cal = float(dicts['Calories'])
                if dicts['Food'] == 'Cooked white or brown rice':
                    new_cal -= 40

                dicts['Protein(g)'] = round(float(dicts['Protein(g)']) * coefficient)
                new_protein = float(dicts['Protein(g)'])

                dicts['Carbs(g)'] = round(float(dicts['Carbs(g)']) * coefficient)
                new_carbs = float(dicts['Carbs(g)'])
                dicts['Fat(g)'] = round(float(dicts['Fat(g)']) * coefficient)
                new_fat = float(dicts['Fat(g)'])

            if dicts.get('Food') == 'TOTAL':
                dicts['Calories'] = int(dicts['Calories']) + new_cal
                dicts['Protein(g)'] = int(dicts['Protein(g)']) + new_protein
                dicts['Carbs(g)'] = int(dicts['Carbs(g)']) + new_carbs
                dicts['Fat(g)'] = int(dicts['Fat(g)']) + new_fat
    return list_of_lists_of_meals
if __name__ == "__main__":
    main()