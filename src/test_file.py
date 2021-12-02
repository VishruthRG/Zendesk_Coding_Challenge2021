import unittest
import requests
import API_endpoints as api
import driver as driver
import sys
import os

class TestAPI(unittest.TestCase):
    def test_get_tickets_api(self):
        params = {'page[size]':'25'}
        EMAIL = os.environ.get('EMAIL')
        PSWD = os.environ.get('PSWD')
        response = requests.get(api.GET_ALL_TICKETS, params=params, auth=(EMAIL,PSWD))
        self.assertEqual(response.status_code, 200)
    
    def test_ticket_count_api(self):
        EMAIL = os.environ.get('EMAIL')
        PSWD = os.environ.get('PSWD')
        ticket_count = requests.get(api.TICKET_COUNT_API, auth=(EMAIL, PSWD))
        self.assertEqual(ticket_count.status_code, 200)

    def test_count_ticket_api(self):
        params = {'ids':self.ticketID}
        EMAIL = os.environ.get('EMAIL')
        PSWD = os.environ.get('PSWD')
        response = requests.get(api.GET_TICKET_BY_ID, params=params, auth=(EMAIL,PSWD))
        self.assertEqual(response.status_code, 200)
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        TestAPI.ticketID = sys.argv.pop()
        unittest.main()
    else:
        print("Please enter ticket ID with command")
    