import start

while (True):
    print("Zendesk ticket viewer main menu")
    print("Enter 1 to: View All Tickets of user zccvishruth")
    print("Enter 2 to: View Selected Tickets by ID")
    print("Enter any key to: Quit Ticket Viewer")
    print("==================================================")
    opt = input("Please enter your option: ")

    if opt == '1':
        start.paginate_results()
        print()
    elif opt == '2':
        ticket_id = input("Please enter ticket id to view details")
        print()
        start.get_ticket_by_id(ticket_id)
    else:
        print("Thank you for using Vishruth's Ticket Viewer")
        break


