## Functional Requirements
1. Login Page: A secure and user-friendly login interface with fields for username and password, a login button, and links for account recovery and new user registration.

2. Ability to Create Folders for their Notes (e.g., by topic, date, project)

3. Create/Delete Notes: Features to create new notes with a rich-text editor, tag and categorize them, and options to delete with a safeguard against accidental loss.

4. Password Recovery Function: when users forget their password, they can recover by changing to a new password.

5. Rich Text Editor: A feature that allows the user to add text in notes and edit the text in ways like highlighting, striking, or bolding the text.

6. Create Account Page: A page for the user to create a new account and confirm with the system for verification and security purposes before the system creates the account.

7. View Folders: Users can view their created folders and the notes associated with the folder.

8. Storing Notes in the Database: Notes and associated metadata (e.g., tags, folders, timestamps) should be stored securely in a database. This ensures persistent storage and retrieval of user-generated content.

9. Attach Images inside the Note Functionality: Images can be embedded inside the users' notes.

10. Editing Notes: users can edit their notes after creating them.

11. User Logout: Users can log out of their account.

[](IMG_7973.JPG)

## Non-functional Requirements
1. THe website is only expected to work better on Google Chrome.

2. The passwords of users will be stored in the Database integrating the hashing algorithm

<each of the 14 requirements will have a use case associated with it>
## Use Cases 

### 1. Login Page (Hannah Ta)
- **Pre-condition:** User is not currently logged in
- **Trigger:** Loading the website for the first time
- **Primary Sequence:**
  1. User will be met with a login page the first time they enter and open the website
  2. System prompts user to enter username and password
  3. The user inputs the information and presses "login" to attempt a login
  4. The system will verify that the account matches an existing account in a database containing all created accounts
- **Primary Postconditions:** User will be logged in given the system matches the information with an existing account
- **Alternate Sequence:** User information does not match or doesn't exist
  1. The system will tell the user "Information does not match with an existing account/does not exist"
  2. The user can select the "Forgot password?" option or "Create a new account"
  3. If "Forgot password?" is selected, the system will take the user to a different page that will prompt the user to enter their unique username then a new password, and re-enter said password
  4. Once confirmed by the user, the system will send an email to the inputted email account that contains a link to verify the user before the change
  5. After the user clicks the link in the email, the system will apply the changes and take the user to a page that says "Password has been changed. You may return to the login page" and has a link back to the login page
  

### 2. Ability to Create Folders for their Notes (Martin Tran)
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
    - After creating a folder, the user may edit the folder name. The system allows the user to update the folder's name.
  3. User Removes Note from Folders:
    - At any point, the user can remove a note from a Folder. The system updates the note accordingly.
  4. User Deletes the Folder:
    - The user will ask if they are sure about their decision
    - If yes, the system will delete the folder with associating notes inside the folder. 


### 3. Create/Delete Notes (Hannah Ta)
- **Pre-condition:** User must be a verified and logged-in account
- **Trigger:** Selection of note options in the form of a create/delete button 
- **Primary Sequence:**
  1. User selects a "create note" button or selects the delete button on an already existing note
  2. If "create note" is selected, the system will bring up a page that has two inputs for the user, the title and body of the note
  3. User will fill out the information page and click "create note"
  4. System will create note and take user back to home page
  6. If user presses the delete button of the note, system will delete note from their home page and the database
- **Primary Postconditions:** User's desired note is created or desired note(s) is deleted
- **Alternate Sequence:** If the note being deleted has other collaborators on it
  1. System will only delete the user's copy of the note and not the other collaborators' copies
  2. System will remove the user from the list of editors/readers on the note


### 4. Password Recovery (Hannah Ta)
- **Pre-condition:**   The user must have a registered account with the system.
                       The user must have access to the email address associated with the account.
- **Trigger:** The user clicks the "Forgot Password" link on the login page.
- **Primary Sequence:**
  1. The user selects the "Forgot Password" option on the login screen.
  2. The system prompts the user to enter their registered email address.
  3. The user enters their email address and submits the form.
  4. The system verifies the email address against the registered users.
  5. Upon successful verification, the system sends a password reset link to the user's email.
  6. The user receives the email and clicks on the provided password reset link.
  7. The link directs the user to a secure password reset page.
  8. The user enters a new password, confirms it, and submits the form.
  9. The system updates the user's password and confirms the change to the user.
  10. The user is then redirected to the login page to access the account with the new password. 
- **Primary Postconditions:** The user's password is successfully reset.
                              The user has access to their account with the new password.
                              The system logs the password reset activity for security purposes.
- **Alternate Sequence:** 
  1. If the email address is not found in the system (Step 4), the user is notified, and no email is sent.
  2. If the password reset link expires or is invalid (Step 6), the user is prompted to restart the password recovery process.
  3. If the user enters mismatched passwords on the reset page (Step 8), the system prompts the user to correct the mistake.
  4. If a technical issue prevents the password reset (any step), the system provides an error message and suggests the user try again later or contact support.


### 5. Rich Text Editor (KHAI TRUONG)
- **Pre-condition:** The user is logged into their account and has permission to edit the note.
                     The note that the user wishes to edit is accessible.
- **Trigger:** The user decides to edit the text within a note.
- **Primary Sequence:** 
  1. The user navigates to the desired note through the sidebar or search function and opens it.
  2. The user clicks on the 'Edit' button or directly clicks into the text area of the note to start editing.
  3. The user adds new text, deletes existing text, or modifies it as needed.
  4. To highlight, the user selects the text and clicks the 'Highlight' button.
  5. To strike-through, the user selects the text and clicks the 'Underline' button.
  6. To make text bold, the user selects the text and clicks the 'Bold' button or uses the keyboard shortcut.
- **Primary Postconditions:** The user's changes are saved and reflected in the note.
                              The note displays the updated content with the applied formatting.
- **Alternate Sequence:** 
  1. If the user attempts to save the changes and an error occurs, the system notifies the user of the failure and provides options to try saving again or to recover unsaved changes.
  2. If the user wishes to undo recent changes, they can use the 'Undo' function or keyboard shortcut to revert to the previous state of the note.
  3. If the system detects unsaved changes when the user attempts to navigate away from the note, it prompts the user to save or discard the changes before leaving.


### 6. Create an Account Page (Khai Truong)
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


### 7. View Folders (Martin Tran)

- **Pre-condition:**
 - The user must have an active account
 - The user must be logged in to their account
 - The user must have at least one created folder
- **Trigger:** The user clicks 'View' in one of the folder's action
- **Primary Sequence:**
  1. The user logged in the their account to the home page.
  2. The user clicks on the add folder icon to add a folder.
  3. After you named your folder's title, the folder should be created and appears two actions: 'View' and 'Delete'.
  4. The user clicks 'View' to view the folder
  5. The system will redirect you to the folder page where you can create notes inside the folder
- **Primary Postconditions:**
  1. The user can add as many notes inside the notes as they want 
- **Alternate Sequence:** 
  1. If the user hasn't created a folder, they cannot view the folder 
  2. If the folder is already deleted, they can't view it.


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

### 9. Attach Images inside the Note Functionality (Khai Truong)
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

### 10. Edit Notes Function (Hannah Ta)
- **Pre-condition:** The user must be logged into their account.
                     The note to be edited must already exist in the user's account.
- **Trigger:** The user selects a note to edit from their list of notes.
- **Primary Sequence:** 
    1. The user navigates to the note they wish to edit from their list of notes or by using the search function.
    2. The user clicks on the "Edit" option associated with the selected note.
    3. The system opens the note in an editable format, displaying the current content of the note.
    4. The user changes the note's text (e.g., adding new text, deleting existing text, formatting text).
    5. If the user wants to highlight text, they select it and click the 'Highlight' button.
    6. If the user wants to strike through text, they choose the text and click on the 'Strike Through' button.
    7. If the user wants to bold text, they select the text and click on the 'Bold' button.
    8. After making changes, the user clicks the “Save” button to update the note.
    9. The system saves the changes and updates the notes in the user's account.
    10. The user is either redirected to their list of notes or remains on the page to make further edits.
- **Primary Postconditions:**
    1. The note reflects all the changes made by the user.
    2. The updated note is saved in the user's account.
    3. The user can continue editing or return to their notes list.
- **Alternate Sequence:** 
    1. If the user attempts to leave the editing page without saving changes, the system prompts to save or discard changes.
    2. If the system encounters an error while saving (e.g., server issue), the user is notified of the failure and can attempt to save again.
    3. If the user decides to discard changes made to the note, they can click on a “Cancel” or “Back” button, which discards changes and returns them to their notes list without saving any modifications.
    4. If the user wants to undo changes, they can use an 'Undo' function or keyboard shortcut to revert to the previous state of the note.
 
### 11. User Logout (Martin Tran)
- **Pre-condition:**
   - User must have an active account with the webpage.
   - User must be logged in to their accounts.
- **Trigger:** The user wants to log out of their account
- **Primary Sequence:**
  1. The user decides to log out of their account.
  2. The user navigates to open the sidebar of the main webpage.
  3. The user clicks on Account to see the selections.
  4. The user clicks on Log Out.
  5. The system will automatically log out of the current user account.
  6. The webpage returns to the Login page.
- **Primary Postconditions:**
  1. The user is logged out of their account, and their session is terminated.
  2. The webpage shows a message that you logged out successfully.
- **Alternate Sequence:** 
  1. User Cancels Logout:
    - The user closes the sidebar to continue their notes
