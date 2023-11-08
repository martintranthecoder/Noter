## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. Login Page: A secure and user-friendly login interface with fields for username and password, a login button, and links for account recovery and new user registration.

2. Sidebar for Notes: An organized and collapsible sidebar categorizes notes into main folders and subfolders, with a search function for easy navigation.

3. Create/Delete Notes: Features to create new notes with a rich-text editor, tag and categorize them, and options to delete with a safeguard against accidental loss.

4. Autosave Functionality: An autosave feature with customizable intervals set by the user to ensure that all changes in the notes are saved automatically and frequently.

5. Editing Notes: A feature that allows the user to add text in notes and edit the text in ways like highlighting, striking, or bolding the text.

6. Create Account Page: A page for the user to create a new account and confirm with the system for verification and security purposes before the system creates the account.

7. Advanced Search Using Regular Expressions: A functionality that helps users to search for words and allows users to perform complex pattern matching.

8. Storing Notes in the Database: Notes and associated metadata (e.g., tags, folders, timestamps) should be stored securely in a database. This ensures persistent storage and retrieval of user-generated content.

9.

10. Adding Others as Editors/Viewers: Users can add other people to collaborate or view their notes.

11. Connect with Notion API: Integrates the note-taking app with Notion's API, allowing for seamless interaction with Notion's features and functionalities.


<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>


## Non-functional Requirements
1. Custom light/dark mode: An option for the user to set the page to have a light background and dark text (light mode) or a dark background and light text (dark mode)

2. Passwords of users will be stored in the Database integrating the MD5 hashing algorithm

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
### 1. Login Page (Hannah Ta)
- **Pre-condition:** User is not currently logged in
- **Trigger:** User goes to the login page through a hyperlink called "login"
- **Primary Sequence:**
1. User selects the "login" link on the home page
2. The system takes the user to a page that prompts the user to input their account information (username/email and password)
3. The user inputs the information and presses "login" to attempt a login
4. The system will verify that the account matches an existing account in a database containing all created accounts
- **Primary Postconditions:** User will be logged in given the system matches the information with an existing account
- **Alternate Sequence:** User information does not match or doesn't exist
1. The system will tell the user "Information does not match with an existing account/does not exist"
2. The user can select the "Forgot password?" option or "Create a new account"
3. If "Forgot password?" is selected, the system will take the user to a different page that will prompt the user to enter their email then a new password, and re-enter said password
4. Once confirmed by the user, the system will send an email to the inputted email account that contains a link to verify the user before the change
5. After the user clicks the link in the email, the system will apply the changes and take the user to a page that says "Password has been changed. You may return to the home page" and has a link back to the home page


### 2. Sidebar for Notes (KHAI TRUONG)
- **Pre-condition:**
  The user is logged into their account.
   There are existing notes and folders within the user's account.
- **Trigger:** The user wants to locate a specific note or view the contents of a folder.
- **Primary Sequence:**
1. The user clicks on the sidebar icon to expand it if it's not already visible.
2. The sidebar displays a list of main folders, each potentially containing subfolders and individual notes.
3. The user clicks on a folder to expand it, revealing any subfolders or notes.
4. The user browses through the list and selects a specific note, which opens for viewing or editing.
5. The user uses the search bar at the top of the sidebar to type in keywords or note titles.
6. The system dynamically filters and displays matching results as the user types.
7. From the search results, the user selects a note to open.
8. After navigating to the desired location, the user clicks the sidebar icon again to collapse it and maximize the workspace.
- **Primary Postconditions:** The user has successfully located and accessed the desired note or folder.
                              The sidebar has either remained expanded or collapsed according to the user's preference.
- **Alternate Sequence:** 
1. If no matching results are found during a search, the system displays a message such as "No matches found" and suggests checking for typos or trying different keywords.
2. If a user tries to access a folder or note that has been deleted or moved, the system shows an error or notification and refreshes the sidebar to reflect the current structure.
3. If the sidebar fails to load due to a system error, the application displays an error message and provides the option to reload the sidebar.


### 3. Create/Delete Notes (Hannah Ta)
- **Pre-condition:** User must be a verified and logged-in account
- **Trigger:** Selection of note options in the form of a create/delete button or a list of note settings
- **Primary Sequence:**
1. User selects a "create note" or selects a note(s) to delete
2. If "create note" is selected, the system will bring up a page that lists parts of the note to add before creating such as name, tag, note location, etc.
3. User will fill out the information page and click "create note"
4. System will check if required fields (name and location) are filled and confirm the decision with the user
5. User selects "yes" to create a note or "no" to cancel
6. If a note/notes are selected/highlighted by a user, a "delete note(s)" option will be available
7. User clicks on "delete note(s)"
8. System will show the note(s) that will be deleted and prompt the user to confirm the deletion
9. User can either cancel or confirm "yes" to delete note(s)
10. If "yes" is selected, the system will delete the note(s) 
- **Primary Postconditions:** User's desired note is created or desired note(s) is deleted
- **Alternate Sequence:** If the note being deleted has other collaborators on it
1. System will only delete the user's copy of the note and not the other collaborators' copies
2. System will remove the user from the list of editors/readers on the note


### 4. Autosave Functionality (Hannah Ta)
- **Pre-condition:** User must be logged in
- **Trigger:** User goes to the settings list
- **Primary Sequence:**
1. User selects/goes to the "autosave" section of the settings
2. User can bring down a list provided by the system to select the time interval for autosaves in minutes (1, 5, 10, etc. or custom)
3. User selects or inputs the time interval for the autosaves
4. System will set the internal timer for autosaves to the new set time interval
- **Primary Postconditions:** The system will change the timer to the newly selected/inputted time interval by the user and autosave at every increment of the new time interval
- **Alternate Sequence:** User wants to revert back to the previous time interval
1. System will have saved the previous time interval before the most recent change
2. The user has the option to select "revert to previous time interval"
3. Selecting the option will prompt the system to change the time interval back to the previous one using the saved time interval.


### 5. Editing Notes (KHAI TRUONG)
- **Pre-condition:** The user is logged into their account and has permission to edit the note.
                     The note that the user wishes to edit is accessible.
- **Trigger:** The user decides to edit the text within a note.
- **Primary Sequence:** 
1. The user navigates to the desired note through the sidebar or search function and opens it.
2. The user clicks on the 'Edit' button or directly clicks into the text area of the note to start editing.
3. The user adds new text, deletes existing text, or modifies it as needed.
4. To highlight, the user selects the text and clicks the 'Highlight' button.
5. To strike through, the user selects the text and clicks the 'Underline' button.
6. To make text bold, the user selects the text and clicks the 'Bold' button or uses the keyboard shortcut.
- **Primary Postconditions:** The user's changes are saved and reflected in the note.
                              The note displays the updated content with the applied formatting.
- **Alternate Sequence:** 
1. If the user attempts to save the changes and an error occurs, the system notifies the user of the failure and provides options to try saving again or to recover unsaved changes.
2. If the user wishes to undo recent changes, they can use the 'Undo' function or keyboard shortcut to revert to the previous state of the note.
3. If the system detects unsaved changes when the user attempts to navigate away from the note, it prompts the user to save or discard the changes before leaving.


### 6. Create an Account Page (Hannah Ta)
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


### 7. Advanced Search Using Regular Expressions (Martin Tran)

- **Pre-condition:**
  - User must have an active account with the webpage.
  - User must be logged in to their accounts.   
- **Trigger:** User clicks on the search bar 
- **Primary Sequence:**
1. The user accesses into one of their notes.
2. The user clicks on search bar to search the word or phrase in their notes.
3. The user types in the search bar with the word/phrase and add regular expression (optional) into the search bar
4. The system will look for the word/phrase that they want inside the note
5. The system will return the results of searching and redirect to the line of the first result that the system found.
- **Primary Postconditions:**
1. The user can click on Next/Prev. keywords (in the search bar) to direct themselves to the line of the word/phrase they want to search for.
2. The user can click "x" to end their search.
- **Alternate Sequence:** 
1. The user enters a word/phrase that doesn't exist
   a. The system won't show any results of the search
2. The user enters wrong regular expressions 
  a. The system won't show any results of the search 


### 8. Storing Notes in the Database (Martin Tran)
- **Pre-condition:** 
- **Trigger:** 
- **Primary Sequence:**
1. 
- **Primary Postconditions:**
1.
- **Alternate Sequence:** 
1.

### 9. Code Blocks Functionality (Martin Tran)
- **Pre-condition:** 
- **Trigger:** 
- **Primary Sequence:**
1. 
- **Primary Postconditions:**
1.
- **Alternate Sequence:** 


### 10. Edit/View Permissions to Others (KHAI TRUONG)
- **Pre-condition:** User must be logged into their account.
                    The note has already been created and saved in the user's account.
                    The user has permission to set access rights for the note.
- **Trigger:** The user adds collaborators to a note for viewing or editing.
- **Primary Sequence:** 
1. The user opens the note they wish to share and clicks on the 'Share' or 'Collaborate' button.
2. The user enters the email addresses or usernames of the individuals they want to collaborate with.
3. For each collaborator, the user sets the permission level: 'Can Edit' or 'Can View'.
4. The user clicks the 'Send Invites' button to send collaboration invites to the chosen individuals.
5. The system sends the invitations and displays a confirmation message to the user.
6. Collaborators receive the invitation and must accept it to gain access to the note.
- **Primary Postconditions:** The invited collaborators have received their invitations.
                              Once accepted, collaborators have the appropriate access rights set by the user.
- **Alternate Sequence:** 
1. If the system cannot send invitations (due to an invalid email address, system error, etc.), it informs the user of the failure and provides an option to try again.
2. If a collaborator does not accept the invitation within a specific timeframe, the system may remind the user to follow up or resend the invitation.
3. The user may revoke or change permissions at any time if they decide to modify access rights.

### 11. Connect with Notion API (Martin Tran)
- **Pre-condition:** 
- **Trigger:** 
- **Primary Sequence:**
1. 
- **Primary Postconditions:**
1.
- **Alternate Sequence:** 

