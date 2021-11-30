import unittest
import requests
import API_endpoints as api
import driver as driver
import sys

class TestAPI(unittest.TestCase):
    def test_get_tickets_api(self):
        params = {'page[size]':'25'}
        keys = driver.get_keys("../.secret/secrets.json")
        EMAIL = keys['EMAIL_ID']
        PWD = keys['PWD']
        response = requests.get(api.GET_TICKETS_PAGE, params=params, auth=(EMAIL,PWD))
        self.assertEqual(response.status_code, 200)
    
    def test_ticket_count_api(self):
        keys = driver.get_keys("../.secret/secrets.json")
        EMAIL = keys['EMAIL_ID']
        PWD = keys['PWD']
        ticket_count = requests.get(api.TICKET_COUNT_API, auth=(EMAIL, PWD))
        self.assertEqual(ticket_count.status_code, 200)

    def test_get_ticket_by_id_api(self):
        #print(self.ticketID)
        if self.ticketID not in driver.get_ids():
            self.assertEqual(driver.get_ticket_by_id(self.ticketID), False)
        else:
            self.assertEqual(driver.get_ticket_by_id(self.ticketID), True)
        
        

if __name__ == "__main__":
    if len(sys.argv) > 1:
        TestAPI.ticketID = sys.argv.pop()
    unittest.main()