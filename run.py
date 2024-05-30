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

    while True:
        print('Welcome to the Strength Workout App')
        print('1. Workout Manager\n2. Exit')
        """
        The choices related to the manager above,
        while the choices for the exercises below
        """
        choice = input('Choose an option in the menu!')
        data = SHEET.worksheet("strength").get_all_values()
        print(data)
        strength = []
        if choice == '1':
            exercise = input('Enter exercise ')
            sets = int(input('Enter amount of sets '))
            reps = int(input('Enter amount of reps '))
            weight = int(input('Enter the weight in Kilogram '))
            strength.extend([exercise, sets, reps, weight])
            data.append(strength)
            print(data)
            print(f'Exercise added')

            """
            Choice 1 for exercise above and for exit below including
            information that only option 1 and 2 is possible
            """

        elif choice == '2':
            print('Thanks for today, see you another time, have a nice day!')

        else:
            print('Option not possible, please press number 1 or 2')


if __name__ == '__main__':
    start()
