import os
SUBDOMAIN = os.environ.get('SUBDOMAIN')
#SUBDOMAIN = "zccvishruth" # This is my subdomain name that I used. Uncomment to use this subdomain for testing
TICKET_COUNT_API = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets/count.json"
GET_ALL_TICKETS_API = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets.json"
GET_TICKET_BY_ID = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets/show_many.json"
GET_TICKETS_PAGE = "https://"+SUBDOMAIN+".zendesk.com/api/v2/tickets.json"