## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. Login Page: A secure and user-friendly login interface with fields for username and password, a login button, and links for account recovery and new user registration.

2. Sidebar for Notes: An organized and collapsible sidebar categorizes notes into main folders and subfolders, with a search function for easy navigation.

3. Create/Delete Notes: Features to create new notes with a rich-text editor, tag and categorize them, and options to delete with a safeguard against accidental loss.

4. Autosave Functionality: An autosave feature with customizable intervals set by the user to ensure that all changes in the notes are saved automatically and frequently.

5. Editing Notes: A feature that allows the user to add text in notes and edit the text in ways like highlighting, striking, or bolding the text.

6. Create Account Page: A page for the user to create a new account and confirms with the system for verification and security purposes before the system creates the account.

7. requirement
8. requirement
9. requirement
10. requirement
11. requirement
12. requirement
13. requirement
14. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. Custom light/dark mode: An option for the user to set the page to have a light background and dark text (light mode) or a dark background and light text (dark mode)

2. non-functional

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description>
- **Trigger:** <can be a list or short description>
- **Primary Sequence:**
1. Ut enim ad minim veniam, quis nostrum e
2. Et sequi incidunt
3. Quis aute iure reprehenderit
4. ...
5. ...
6. ...
7. ...
8. ...
9. ...
10. <Try to stick to a max of 12 steps>
- **Primary Postconditions:** <can be a list or short description>
- **Alternate Sequence:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>

1. Ut enim ad minim veniam, quis nostrum e
2. Ut enim ad minim veniam, quis nostrum e
3. ...


## list of real use cases start here (will delete above example once all 14 use cases are finished)
1. Login Page (Hannah Ta)
- **Pre-condition:** User is not currently logged in
- **Trigger:** User goes to the login page through a hyperlink called "login"
- **Primary Sequence:**
1. User selects the "login" link on the home page
2. System takes user to a page that prompts the user to input their account information (username/email and password)
3. User inputs the information and presses "login" to attempt a login
4. System will verify account matches with an existing account in a database containing all created accounts
- **Primary Postconditions:** User will be logged in given the system matches the informaiton with an existing account
- **Alternate Sequence:** User information does not match or doesn't exist
1. System will tell user "Information does not match with an existing account/does not exist"
2. User can select the "Forgot password?" option or "Create a new account"
3. If "Forgot password?" is selected, system will take user to a different page that will prompt user to enter email then a new password and re-enter said password
4. Once confirmed by user, system will send an email to the inputted email account that contains a link to verify the user before the change
5. After user clicks the link in the email, the system will apply the changes and take the user to a page that says "Password has been changed. You may return to the home page" and has a link back to the home page


1. Sidebar for Notes (insert name)
- **Pre-condition:** 
- **Trigger:** 
- **Primary Sequence:**
1. 
- **Primary Postconditions:** 
- **Alternate Sequence:** 
1. 


1. Create/Delete Notes (Hannah Ta)
- **Pre-condition:** User must be a verified and logged in account
- **Trigger:** Selection of note options in the form of a create/delete button or a list of note settings
- **Primary Sequence:**
1. User selects a "create note" or selects a note(s) to delete
2. If "create note" is selected, system will bring up a page that lists parts of the note to add before creating such as name, tag, note location, etc.
3. User will fill out the information page and click "create note"
4. System will check if required fields (name and location) are filled and confirm decision with user
5. User selects "yes" to create note or "no" to cancel
6. If a note/notes are selected/highlighted by user, a "delete note(s)" option will be available
7. User clicks on "delete note(s)"
8. System will show the note(s) that will be deleted and prompt the user to confirm deletion
9. User can either cancel or confirm "yes" to delete note(s)
10. If "yes" is selected, system will delete the note(s) 
- **Primary Postconditions:** User's desired note is created or desired note(s) is deleted
- **Alternate Sequence:** If the note being deleted has other collaborators on it
1. System will only delete the user's copy of the note and not the other collaborators' copies
2. System will remove user from the list of editors/readers on the note


1. Autosave Functionality (Hannah Ta)
- **Pre-condition:** User must be logged in
- **Trigger:** User goes to the settings list
- **Primary Sequence:**
1. User selects/goes to the "autosave" section of the settings
2. User can bring down a list provided by the system to select the time interval for autosaves in minutes (1, 5, 10, etc. or custom)
3. User selects or inputs the time interval for the autosaves
4. System will set the internal timer for autosaves to the new set time interval
- **Primary Postconditions:** The system will change the timer to the newly selected/inputted time interval by the user and autosave at every increment of the new time interval
- **Alternate Sequence:** User wants to revert back to previous time interval
1. System will have saved the previous time interval before the most recent change
2. User has the option to select "revert to previous time interval"
3. Selecting the option will prompt system to change the time interval back to the previous one using the saved time interval.


1. Editing Notes (insert name)
- **Pre-condition:** 
- **Trigger:** 
- **Primary Sequence:**
1. 
- **Primary Postconditions:** 
- **Alternate Sequence:** 
1. 


1. Create Account Page (Hannah Ta)
- **Pre-condition:** User can either be logged in or not logged in
- **Trigger:** User selects the "create account" option either from the home page or the login page
- **Primary Sequence:**
1. User selects "create account" and is taken to the "create account" page
2. System will have empty boxes for user to fill out information such as email, username, password (along with re-entering password), etc.
3. User fills out the boxes with their information and selects "create account"
4. System will check if username is not taken
5. System will send an email to verify the user and prompt them to click the link in the email before creating the account
6. User gets email and clicking the link will take them to a page that says "Congrats! Your new account has been created. You may return to the home page" and the system will save the new account information to a database containing all existing and newly created accounts on the site
- **Primary Postconditions:** A new account is created for the user to use to login and use the features of the site
- **Alternate Sequence:** User inputs a username that already exists in the database
1. System will check if the inputted username matches with any existing username in the accounts database
2. If username matches with an already existing username in the databse, system will tell user "username has already been taken" and prompt user to enter a new username


1. <requirement> (insert name)
- **Pre-condition:** 
- **Trigger:** 
- **Primary Sequence:**
1. 
- **Primary Postconditions:** 
- **Alternate Sequence:** 
1. 


