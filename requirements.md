## Functional Requirements
1. Login Page: A secure and user-friendly login interface with fields for username and password, a login button, and links for account recovery and new user registration.

2. Ability to Categorize and Organize their Notes (e.g., by topic, date, project)

3. Create/Delete Notes: Features to create new notes with a rich-text editor, tag and categorize them, and options to delete with a safeguard against accidental loss.

4. Autosave Functionality: An autosave feature with customizable intervals set by the user to ensure that all changes in the notes are saved automatically and frequently.

5. Editing Notes: A feature that allows the user to add text in notes and edit the text in ways like highlighting, striking, or bolding the text.

6. Create Account Page: A page for the user to create a new account and confirm with the system for verification and security purposes before the system creates the account.

7. Advanced Search Using Regular Expressions: A functionality that helps users to search for words and allows users to perform complex pattern matching.

8. Storing Notes in the Database: Notes and associated metadata (e.g., tags, folders, timestamps) should be stored securely in a database. This ensures persistent storage and retrieval of user-generated content.

9. Attach Images inside the Note Functionality: Images can be embedded inside the users' notes.

10. Adding Others as Editors/Viewers: Users can add other people to collaborate or view their notes.

11. Connect with Notion API: Integrates the note-taking app with Notion's API, allowing for seamless interaction with Notion's features and functionalities.


[](IMG_7973.JPG)

## Non-functional Requirements
1. Custom light/dark mode: An option for the user to set the page to have a light background and dark text (light mode) or a dark background and light text (dark mode)

2. Passwords of users will be stored in the Database integrating the MD5 hashing algorithm

<each of the 14 requirements will have a use case associated with it>
## Use Cases 

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
  

### 2. Ability to Categorize and Organize their Notes (KHAI TRUONG)
- **Pre-condition:**
  - The user is logged into their account.
  - There are existing notes and folders within the user's account.
- **Trigger:** The user creates a new folder 
- **Primary Sequence:**
  1. The user creates a new folder
  2. The system prompts the user for the name of the folder
  3. The user can type in the name of the folder according to subjects, topics, dates, or projects
  4. The user can either add existing notes or create new notes in the new folder
- **Primary Postconditions:**
  - The user's notes are successfully organized into big folders based on their chosen criterion (e.g., topic, date, project).
  - The user can easily access and retrieve notes within the designated folders.
- **Alternate Sequence:** 
  1. User Add New Folder with Existing Names:
    - The system will show an error and ask the user to re-enter a new unique name 
  2. User Edits Folder Name:
    - After creating a folder, the user may choose to edit the folder name. The system allows the user to update the folder's name.
  3. User Removes Note from Folders:
    - At any point, the user can remove a note from a Folder. The system updates the note accordingly.
  4. User Deletes the Folder:
    - The user will ask if they are sure about their decision
    - If yes, the system will delete the folder with associating notes inside the folder. 


### 3. Create/Delete Notes (Hannah Ta)
- **Pre-condition:** User must be a verified and logged-in account
- **Trigger:** Selection of note options in the form of a create/delete button or a list of note settings
- **Primary Sequence:**
  1. User selects a "create note" or selects a note(s) to delete
  2. If "create note" is selected, the system will bring up a page that lists parts of the note to add before creating such as name, tag, note location, etc.
  3. User will fill out the information page and click "create note"
  4. System will check if the required fields (name and location) are filled and confirm the decision with the user
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
  2. User can bring down a list provided by the system to select the time interval for autosaves in minutes (1, 5, 10, etc., or custom)
  3. User selects or inputs the time interval for the autosaves
  4. System will set the internal timer for autosaves to the new set time interval
- **Primary Postconditions:** The system will change the timer to the newly selected/inputted time interval by the user and autosave at every increment of the new time interval
- **Alternate Sequence:** User wants to revert to the previous time interval
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
  1. User selects "Create account" and is taken to the "Create account" page
  2. System will have empty boxes for the user to fill out information such as email, username, password (along with re-entering password), etc.
  3. User fills out the boxes with their information and selects "create account"
  4. System will check if the username is not taken
  5. System will send an email to verify the user and prompt them to click the link in the email before creating the account
  6. User gets an email and clicking the link will take them to a page that says "Congrats! Your new account has been created. You may return to the home page" and the system will save the new account information to a database containing all existing and newly created     accounts on the site
- **Primary Postconditions:** A new account is created for the user to use to login and use the features of the site
- **Alternate Sequence:** User inputs a username that already exists in the database
  1. System will check if the inputted username matches any existing username in the accounts database
  2. If the username matches an already existing username in the database, the system will tell the user's username has already been taken" and prompt the user to enter a new username


### 7. Advanced Search Using Regular Expressions (Martin Tran)

- **Pre-condition:**
  - User must have an active account with the webpage.
  - User must be logged in to their accounts.
  - User should have at least a note with the content inside it.
- **Trigger:** User clicks on the search bar 
- **Primary Sequence:**
  1. The user accesses one of their notes.
  2. The user clicks on the search bar to search for the word or phrase in their notes.
  3. The user types in the search bar with the word/phrase and adds regular expressions (optional) into the search bar
  4. The system will look for the word/phrase that they want inside the note
  5. The system will return the results of searching and redirect to the line of the first result that the system found.
- **Primary Postconditions:**
  1. The user can click on Next/Prev. keywords (in the search bar) to direct themselves to the line of the word/phrase they want to search for.
  2. The user can click "x" to end their search.
- **Alternate Sequence:** 
  1. The user enters a word/phrase that doesn't exist
     a. The system won't show any results of the search
  2. The user enters the wrong regular expressions 
    a. The system won't show any results of the search 


### 8. Storing Notes in the Database (Martin Tran)
- **Pre-condition:**
   - User must have an active account with the webpage.
   - User must be logged in to their accounts.  
- **Trigger:** The user creates new notes
- **Primary Sequence:**
  1. The user logins into their account
  2. The user clicks on "+" (add) to create new notes
  3. The system prompts the user for the name of the new note
  4. The user types in the name they want for the note
  5. The system will create and store a new empty note in the database with the name and the created date
  6. After a specific time, when the user makes some changes in their new note
  7. The user hits the "Save" button
  8. The system will update the new note with the content of the note at the time they hit "Save"
- **Primary Postconditions:**
  1. The user has successfully created and stored string notes in the database. They can access, edit, and manage their notes at any time.
- **Alternate Sequence:** 
  1. The new note has the same name as their previous notes
     a. The system will show the error
     b. The system asks the user to type in new unique names for the note 

### 9. Attach Images inside the Note Functionality (Martin Tran)
- **Pre-condition:**
   - User must have an active account with the webpage.
   - User must be logged in to their accounts.
   - User should have at least a note.
- **Trigger:** User clicks the "Add" keyword on top of the note 
- **Primary Sequence:**
  1. The user selects one of the notes they want to edit
  2. The user clicks the "Add" button on the top, then clicks "Images" from the dropdown list
  3. The system prompts the user if they want to upload their image or the image from the online URL
  4. The user can either drop the URL link of the image or upload the image from their local hard drive
  5. The system will load the image from the location and store it in the database
  6. The image will appear on the note
- **Primary Postconditions:**
  1. The image is successfully attached to the note and is displayed within the note editor.
  2. The user can save or update the note with the attached image.
  3. The image can be deleted by the user.
- **Alternate Sequence:** 
  1. User Cancels Image Upload:
    - At step 4, if the user decides not to add an image, they can cancel the process. The system returns to the note editor without attaching an image.
  2. Invalid Image Format:
    - At step 5, if the user selects an unsupported file format (e.g., not an image file), the system displays an error message and prompts the user to select a valid image file.
  3. Network Error During Upload:
    - If there is a network error during the image upload process, the system notifies the user and provides an option to retry the upload.
  4. Image Size Limit Exceeded:
    - If the selected image file exceeds the maximum allowed file size, the system displays an error message and prompts the user to select a smaller image.
  5. URL doesn't exist
    - The system will show an error, and ask the user to re-enter the link to load.

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
   - User must have an active account with the webpage.
   - User must be logged in to their accounts.
- **Trigger:** The user wants to connect with their Notion account
- **Primary Sequence:**
  1. The user navigates to the settings or configuration section of the project within the project management website.
  2. The user selects the option to connect the project with their Notion account.
  3. The system prompts the user to authorize the connection by logging in to their Notion account (if not already authenticated).
  4. The user enters their Notion credentials and grants the necessary permissions for the project to access their Notion account via the API.
  5. The system validates the user's credentials and permissions with the Notion API.
  6. The system establishes a secure connection with the Notion API.
  7. The user receives a confirmation message that the project is now connected to their Notion account.
  8. Within the project, the user can now perform actions such as importing data from Notion, exporting project details to Notion, or synchronizing project tasks with Notion pages.
- **Primary Postconditions:**
  1. The user's project in the project management website is successfully connected to their Notion account through the API.
  2. The user can perform actions related to their project that involve interaction with their Notion account.
- **Alternate Sequence:** 
  1. User Cancels Authorization:
    - At step 4, if the user decides not to authorize the connection, they can cancel the process. The system returns to the project settings without establishing the connection.
  2. Invalid Credentials:
    - If the user enters incorrect Notion credentials at step 4, the system displays an error message and prompts the user to re-enter their credentials.
  3. Authorization Denied by User:
    - If the user declines to grant the necessary permissions at step 4, the system notifies the user and prompts them to authorize the connection again.
