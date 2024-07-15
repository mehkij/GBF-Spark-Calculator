def spark(crystals = 0, tickets = 0):
    spark = 90000
    ticket_value = 300
    total = crystals + (tickets * ticket_value)
    remaining_tickets = round((spark - total) / ticket_value)

    print(f"Total value of your crystals and tickets: {total}")
    print(f"Amount of crystals remaining until spark: {spark - total if total <= spark else 0}")
    print(f"The amount of tickets you would need to spark: {remaining_tickets if total <= spark else 0}")

    if total >= spark:
        print("Your progress: 100%")
    else:
        print(f"Your progress: {float(total / spark * 100):.2f}%")

def main():
    crystals = int(input("How many crystals do you have?\n"))
    tickets = int(input("How many tickets do you have?\n"))

    spark(crystals, tickets)

main()