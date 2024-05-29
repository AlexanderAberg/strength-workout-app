import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('strength_workout_app')



def get_strength_data():
    """
    Get strength workout data from user
    """
    print('You can enter your workout information here.')
    print('Sets, reps and weight needs to be written as numbers, and weight is counted in Kilograms.')

    data_str = input('Enter your information here')
    print(f'The information you provided is {data_str}')

get_strength_data()
print(get_strength_data)

"""
def start():
    strength_workout_app = StrengthWorkoutApp()

    while True:
        print_separator()
        print('Welcome to the Strength Workout App')
        print_separator()
        print('1. Workout Manager\n2. Exit')

        choice = input('Choose an option in the menu!')

        if choice == '1':
            exercise = input('Enter exercise'):
            sets = input('Enter amount of sets'):
            reps = input('Enter amount of reps'):
            weight = input('Enter the weight in Kilogram'):
            strength_workout_app.log_workout(SHEET.worksheet('strength'))
            print_separator()
            print(f'Exercise added')

        elif choice == '2':
            print_separator()
                print('Thanks for today, see you another time, goodbye and have a nice day!')

        else:
            print_separator(
                print('Option not possible, please press number 1 or 2')
            )
            
if __name__ = '__start__':
    main()

print(start)
"""