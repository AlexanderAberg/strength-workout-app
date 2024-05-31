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

"""
The start menu below, the spreadsheet and creds.json above.
"""


def start():
    strength = []
    while True:
        workout = []
        print('Welcome to the Strength Workout App')
        print('1. Workout Manager\n2. Exit')
        """
        The choices related to the manager above,
        while the choices for the exercises below
        """
        choice = input('Choose an option in the menu! \n')
        if choice == '1':
            try:
                exercise = input('Enter exercise ')

            except ValueError:
                print('You have to add a value')

            try:

                """
                Separate to give error message and
                have loop repeat after wrong answer.
                """
                sets = abs(int(input('Enter amount of sets ')))
                reps = abs(int(input('Enter amount of reps ')))
                weight = abs(int(input('Enter the weight in Kilogram ')))
                """
                Have int for whole numbers and numbers only allowed,
                included abs instead of make negative forbidden
                to make it more user friendly.
                """
                workout.extend([exercise, sets, reps, weight])
                strength.append(workout)
                print(workout)
                print(strength)
                continue

            except ValueError:
                print('You have to add a number')

            print('Exercise added')

            """
            Choice 1 for exercise above and for exit below including
            information that only option 1 and 2 is possible
            """

        elif choice == '2':
            print('Thanks for today, see you another time, have a nice day!')
            break

        else:
            print('Option not possible, please press number 1 or 2')
    return strength


def update_strength_worksheet(data):
    """
    Add information to the worksheet, add new row with information"
    """
    print('Adding exercises to worksheet')
    print(data)
    strength_worksheet = SHEET.worksheet('strength')
    strength_worksheet.append_rows(data)
    print('Strength worksheet updated\n')


if __name__ == '__main__':
    workout_data = start()
    update_strength_worksheet(workout_data)
