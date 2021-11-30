import requests
import json
import pandas as pd
from requests.api import request

EMAIL = "vishruth@tamu.edu"
PWD = "aBwQE4"
SUBDOMAIN = "zccvishruth"
API_TOKEN = "nDoxGpD2brnxeAO1gfM8fxX5ppvN0EF6KTIMgcku"
TICKET_COUNT_API = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets/count.json"

def print_all_ticket_data(no_of_tickets, resp):

    data = []
    try:
        for i in range(1, no_of_tickets):  
            #url = json.dumps(resp["tickets"][int(i) - 1]["url"])
            id = json.dumps(resp["tickets"][int(i) - 1]["id"])
            status = json.dumps(resp["tickets"][int(i) - 1]["status"])
            subject = json.dumps(resp["tickets"][int(i) - 1]["subject"])
            desc = json.dumps(resp["tickets"][int(i) - 1]["description"])
            requested_by = json.dumps(resp["tickets"][int(i) - 1]["requester_id"])
            assigned_to = json.dumps(resp["tickets"][int(i) - 1]["assignee_id"])
            dataset = [id, status, subject, desc, requested_by, assigned_to]
            data.append(dataset)
    except IndexError:
        pass
    cols = ['ID', 'STATUS', 'SUBJECT', 'DESC', 'REQUESTED BY', 'ASSIGNED TO']
    df = pd.DataFrame(data, columns = cols)
    print(df)

def print_ticket_by_id(id_list, resp):
    data = []
    for i in range(len(id_list)):  
        #url = json.dumps(resp["tickets"][int(i) - 1]["url"])
        id = json.dumps(resp["tickets"][int(i) - 1]["id"])
        status = json.dumps(resp["tickets"][int(i) - 1]["status"])
        subject = json.dumps(resp["tickets"][int(i) - 1]["subject"])
        desc = json.dumps(resp["tickets"][int(i) - 1]["description"])
        requested_by = json.dumps(resp["tickets"][int(i) - 1]["requester_id"])
        assigned_to = json.dumps(resp["tickets"][int(i) - 1]["assignee_id"])
        dataset = [id, status, subject, desc, requested_by, assigned_to]
        data.append(dataset)

    #print(len(data))
    cols = ['ID', 'STATUS', 'SUBJECT', 'DESC', 'REQUESTED BY', 'ASSIGNED TO']
    df = pd.DataFrame(data, columns = cols)
    print(df)
    print()

def count_tickets():
    TICKET_COUNT_API = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets/count.json"
    ticket_count = requests.get(TICKET_COUNT_API, auth=("vishruth@tamu.edu", "aBwQE4"))
    ticket_count_resp = ticket_count.json()
    no_of_tickets = json.dumps(ticket_count_resp["count"]["value"])
    no_of_tickets = int(no_of_tickets)
    return no_of_tickets



# Get all tickets of account
def get_all_tickets():
    GET_ALL_TICKETS_API = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets.json"
    response = requests.get(GET_ALL_TICKETS_API, auth=("vishruth@tamu.edu", "aBwQE4"))
    resp = response.json()
    no_of_tickets = count_tickets(TICKET_COUNT_API)
    print_all_ticket_data(no_of_tickets, resp)




def get_ticket_by_id(ticket_id):
    params = {'ids':ticket_id}
    GET_TICKET_BY_ID = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets/show_many.json"
    response = requests.get(GET_TICKET_BY_ID, params=params, auth=("vishruth@tamu.edu", "aBwQE4"))
    resp = response.json()
    ids = params["ids"].split(',')
    int_ids = [int(i) for i in ids]
    print_ticket_by_id(int_ids, resp)


def paginate_results():
    GET_TICKETS_PAGE = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets.json"
    params = {'page[size]':'25'}
    response = requests.get(GET_TICKETS_PAGE, params=params, auth=(EMAIL,PWD))
    resp = response.json()
    print_all_ticket_data(25, resp)

    np = 'Y'
    while(np != 'N'):
        np = input("View next page? Y = yes, N = no ")
        if resp["meta"]["has_more"] == False:
            break
        if (np == "y" or np == "Y"):
            next_page = json.dumps(resp["meta"]["after_cursor"])
            prev_page = json.dumps(resp["meta"]["before_cursor"])
            next_page = next_page[1:len(next_page) - 1]
            prev_page = prev_page[1:len(prev_page) - 1]
            params = {'page[size]':'25', 'page[after]':next_page}
            response = requests.get(GET_TICKETS_PAGE, params=params, auth=('vishruth@tamu.edu', "aBwQE4"))
            resp = response.json()
            print_all_ticket_data(25, resp)
        else:
            print()
            break



