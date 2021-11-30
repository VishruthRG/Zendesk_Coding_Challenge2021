# Zendesk_Coding_Challenge2021
This is my submission to the Zendesk Intern Coding Challenge for 2021

## Packages
This projects makes use of the json, requests and pandas packages. To install the packages required for this project run

```
pip install -r requirements.txt
```

## Running the code
To run the code, clone the repository and navigate to the ```src``` folder. Once in the folder, run 
```
python menu.py
```

## Unit tests
Unit tests for this project are written using the unittest in-built python library. To run the sample test cases run
```
python -m test_file
```

## Testing on other accounts
To test the project code for other accounts, i.e, view ticket data for other accounts, the following steps have to be done
1. Navigate to the `.secret/secrets.json` file
2. Change the `EMAIL`, `PWD` and the `API_KEY` fields with the updated values
3. Change the `SUBDOMAIN` value in the `API_endpoints` file

Now it should be possible to run the code on the required account.

### Note
For this project, I have not created a browser interface. It uses a CLI for the operations. The operations allowed are
1. Viewing all tickets
2. Viewing ticket details for selected tickets

Other features are:
1. Ticket data displayed are: ID, Status, Subject, Description, Requestor and Assignee ID's
2. Pages through when number of results greater than 25
3. Although I have not added functionality to choose page numbers, pages can be scrolled by hitting Y to access subsequent pages until there are no further pages, at which point the user is redirected back to the main menu
4. Menu looks like this
![Menu View](img/menu.png)

5. Image showing the second page of the ticket pages
![Option 1: Displaying all available tickets (page 2)](img/opt1.png)

6. Image showing ticket data for select tickets
![Option 2: Displaying ticket data for select tickets](img/opt2.png)

7. Image showing exit
![Option 3: Exit menu](img/exit.png)