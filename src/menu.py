import driver as driver
import API_endpoints as api
while (True):
    print("Zendesk ticket viewer main menu")
    print("Enter 1 to: View All Tickets of user",api.SUBDOMAIN)
    print("Enter 2 to: View Selected Tickets by ID")
    print("Enter any key to: Quit Ticket Viewer")
    print("==================================================")
    opt = input("Please enter your option: ")

    if opt == '1':
        driver.paginate_results()
        print()
    elif opt == '2':
        ticket_id = input("Please enter ticket id to view details ")
        driver.get_ticket_by_id(ticket_id)   
    else:
        print("Thank you for using Ticket Viewer")
        break