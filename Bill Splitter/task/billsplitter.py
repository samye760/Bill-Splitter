import random

number_of_guests = int(
    input("Enter the number of friends joining (including you):\n"))

if number_of_guests < 1:
    print("No one is joining for the party")
else:
    print(
        "\nEnter the name of every friend (including you), each on a new line:")
    guests = {}

    for _ in range(number_of_guests):
        guest = input()
        guests[guest] = 0

    final_bill = int(input("\nEnter the total bill value:\n"))

    split_bill = round(final_bill / len(guests), 2)

    lucky = input(
        '\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky == 'Yes':
        pick = random.choice(list(guests.keys()))
        print(f"\n{pick} is the lucky one!")

        split_bill = round(final_bill / (len(guests) - 1), 2)

        guests = {key: split_bill if key != pick else 0 for key in guests}

        print(f"\n{guests}")
    else:
        print("\nNo one is going to be lucky")

        guests = {key: split_bill for key in guests}

        print(guests)
