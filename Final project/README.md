# Health and nutrition
#### Video Demo:  <URL HERE>
#### Description:
This program serves as a comprehensive health and nutrition tool. It begins by gathering user data such as gender, age, weight, height, and activity level to calculate the user's Body Mass Index (BMI) and required Daily Calorie Intake (DCI) using established formulas. Based on the calculated BMI, the program then advises the user on whether they need to gain, maintain, or lose weight.

Moreover, the program then offers personalized meal planning to align with the user's DCI and weight goals. It reads from CSV files containing nutritional information for various meals categorized into breakfast, shakes, lunch, snacks, and dinner. The meal_plan() function compiles these meals into a list of dictionaries.

The regulator() function adjusts the quantities of food items in each meal to customize the meal plan according to the user's caloric needs. It modifies the amounts of specific foods to ensure that each meal contributes appropriately to the user's daily caloric intake. Additionally, it considers adjustments for specific foods, such as reducing calories from rice by 40 units.

Overall, this script provides a tailored approach to health management by incorporating user-specific data to offer dietary guidance and meal planning that aligns with individual goals and needs. With its modular design and use of regular expressions for input validation, the script offers flexibility and accuracy in its recommendations.






