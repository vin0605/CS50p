from datetime import date
import inflect
import sys
import operator

p = inflect.engine()

def main():
    try:
        birth_date = input("Date of birth: ")
        formatted_dob = date.fromisoformat(birth_date)
        current_date = date.today()
        subtracted_date = operator.sub(current_date, formatted_dob)
        print(min_calculator(subtracted_date.days))

    except ValueError:
        sys.exit('Invalid date')

def min_calculator(n):
    mins = round(n * 24 * 60)
    word_form = p.number_to_words(mins, andword = '')
    return f"{word_form.capitalize()} minutes"

if __name__ == "__main__":
    main()