from data_storage import create_chart
from data_storage import read_column
filename_prompt = "Enter your desired file name: "
user_menu = """Please choose from the following options:

- Enter 'c' to chart a new graph.
- Enter 'q' to quit.

Your selection: """

charting_menu = "Enter the column you'd like to chart: "


def handel_chart():
    try:
        column = int(input(charting_menu))
        x = read_column(-1)
        y = [float(n) for n in read_column(column)]
        file_name = input(filename_prompt)
        create_chart(x, y, file_name.strip())
    except ValueError:
        print("Your column have to integer")


while True:
    user_selection = input(user_menu)
    if user_selection == "q":
        break
    elif user_selection == "c":
        handel_chart()
    else:
        print(f"Sorry,{user_selection} is not a valid option")
