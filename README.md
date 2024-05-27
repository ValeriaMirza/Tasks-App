# Task Notification App - README


## Overview

This Task Notification App is designed to help users manage and track their tasks efficiently. The app allows users to add tasks with due dates, receive reminders via email, and mark tasks as completed. It integrates with SQL Server for database management and uses SendGrid for email notifications.


## Description
When you run the Task Notification App by executing main.py, the following processes take place:


### Initialization
**1.Database Initialization:**
- The application first checks if the specified SQL Server database and necessary tables exist. If they do not exist, it creates them.
- This ensures that the environment is set up correctly for storing and managing task data.
  
**2.Scheduler Initialization:**
- The application starts a scheduler that periodically checks for tasks that are due.
- This scheduler runs every minute to ensure timely notifications.
  
**3.GUI Launch:**
- The graphical user interface (GUI) built with Tkinter is launched.
- This GUI allows users to interact with the app, including adding new tasks, marking tasks as completed, and deleting tasks.

### User Interaction
**4. Adding a Task:**
- Users can add a new task through the GUI by entering the task description and due date.
- The task is saved to the SQL Server database.

**5. Completing a Task:**
- Users can mark a task as completed through the GUI.
- The task's status is updated in the database.

**6. Deleting a Task:**
- Users can delete a task through the GUI.
- The task is removed from the database.
  
**7.Voice Input:**
- Users can add tasks using voice input. The voice input is transcribed using AssemblyAI's API and added to the task list.

### Automated Processes
**8.Periodic Task Check:**
- Every minute, the scheduler triggers a check for tasks that are due within the next hour.
- This is done by querying the database for tasks whose due dates are approaching.

**9. Sending Email Notifications:**
- For each task that is found to be due soon, an email reminder is sent to the specified email address using SendGrid's API.
- The content of the email includes the task description and the due date.
  
**10.Updating Notification Status:**
- After sending the email, the task's last notified timestamp is updated in the database to prevent duplicate notifications.

### Exiting the Application
**11. Graceful Shutdown:**
- When the user exits the application, the GUI closes, and the scheduler stops running.
- Any ongoing database connections are closed properly.


## Requirements

- **Python Version:** 3.11.2
- **Other Dependencies:** Listed in `requirements.txt`

  
## Project Structure
```
TASKS PROJECT/
├── README.md
├── requirements.txt
├── config.py
├── database.py
├── email_sender.py
├── gui.py
├── main.py
├── scheduler.py
└── testing/
    └── test_config.py
    └── test_database.py
    └── test_email.py
    └── __init__.py
```


## Configuration Details
To make this Task Notification App work correctly, you need to provide specific information in the config.py file. Here's a detailed guide on what information you need to provide and how to obtain it.

### Step-by-Step Configuration

**1.Clone the Repository:** First, clone the repository to your local machine.
```
git clone https://github.com/ValeriaMirza/Tasks-App.git
cd Tasks-App
```

**2.Install Dependencies:** Ensure you have Python installed. Then, install the required packages using pip:
```
pip install -r requirements.txt
```
**3.Configure API Keys and Database Server:** Open the config.py file. You will need to fill in the following details:
```
SENDGRID_API_KEY = 'SG.XXXXXXXXXXXXXXXXXXXXXXXX'
AAI_SETTINGS_API_KEY = 'XXXXXXXXXXXXX'
server = 'DESKTOP-XXXXXX\\SQLEXPRESS'
user_email = 'your_email@example.com'
```

### 1. Obtain SendGrid API Key
SendGrid is used to send email notifications. Follow these steps to get your SendGrid API key:

 - Go to [SendGrid](https://sendgrid.com/en-us/1?adobe_mc_sdid=SDID%3D47A7D4C82F6C4FB7-79DA28CC2FCE1024%7CMCORGID%3D32523BB96217F7B60A495CB6%40AdobeOrg%7CTS%3D1716844787&adobe_mc_ref=https%3A%2F%2Fwww.google.com%2F) and sign up for an account if you don't have one.
 - Once logged in, navigate to the API Keys section under the Settings menu.
 - Click on Create API Key.
 - Give your API key a name (e.g., TaskNotificationApp) and select the permissions you need.
 - Click Create & View. Copy the generated API key.
 - Paste the API key in the SENDGRID_API_KEY variable in config.py.

### 2. Obtain AssemblyAI API Key
AssemblyAI is used for the voice transcription feature. Follow these steps to get your AssemblyAI API key:

 - Go to [AssemblyAI](https://www.assemblyai.com/dashboard/signup) and sign up for an account if you don't have one.
 - Once logged in, you will be taken to your dashboard where you can find your API key.
 - Copy the API key from the dashboard.
 - Paste the API key in the AAI_SETTINGS_API_KEY variable in config.py.

### 3. Configure SQL Server
The application uses SQL Server to store task data. You need to specify your SQL Server instance:

 - Ensure SQL Server is installed and running on your machine. If not, download and install SQL Server from here.
 - Replace the server variable in config.py with your SQL Server instance name.
   
![image](https://github.com/ValeriaMirza/Tasks-App/assets/87279317/c85da789-f1ee-4b04-976f-2f94cf2e272f)

For example:

```
server = 'DESKTOP-D3V5DUN\\SQLEXPRESS\\SQLEXPRESS'
```
 - If you are using the default SQL Server instance, it might just be server = 'localhost'

### 4. Specify Your Email
- Provide the email address where you want to receive task notifications. This will be used to send reminders about due tasks.
- Replace the user_email variable in config.py with your email address. 
For example:
```
user_email = 'valeriamirza5@gmail.com'
```


## Running the Application
Run main.py to start the application.
```
python main.py
```


## Modules

### database.py
Contains functions for database operations:

 - **get_conn_str(db):** Generates the connection string for the database.
 - **create_database_and_table_if_not_exists():** Creates the database and table if they do not exist.
 - **save_to_database(to_email, task, due_date):** Saves a new task to the database.
 - **get_tasks_due_within_hour():** Retrieves tasks that are due within the next hour.
 - **update_last_notified(task_id):** Updates the last notified time for a task.
 - **complete_task_in_database(task_id):** Marks a task as completed.
 - **get_last_inserted_id():** Retrieves the last inserted task ID.
 - **delete_task_from_database(task_id):** Deletes a task from the database.

### email_sender.py
Contains function for sending emails:

 - **send_email(to_email, subject, content):** Sends an email using SendGrid.

### gui.py
Implements the GUI using Tkinter:

 - **TaskApp:** The main class for the GUI application, allowing users to add, complete, and delete tasks, and use voice input.

### scheduler.py
Manages the scheduling of periodic checks for due tasks:

 - **schedule_task():** Schedules the task checker to run every minute.
- **check_and_send_emails():** Checks for due tasks and sends email reminders.
  
### main.py
The entry point of the application:

- Initializes the database and table.
- Starts the scheduler.
- Launches the Tkinter GUI.
  
### testing/
Contains unit tests for the application's modules:

- **test_config.py:** Tests the configuration settings.
- **test_database.py:** Tests the database functions.
- **test_email_sender.py:** Tests the email sending functionality.


## Running Tests
Run the unit tests to ensure everything is working correctly:
```
coverage run -m unittest discover -s testing
```


### Dependencies
The application requires the following Python packages:

- pyodbc
- tkinter
- sendgrid
- assemblyai
- beautifulsoup4
- requests
- pyaudio
- wave

All dependencies are listed in requirements.txt.


## Contact
For any questions or feedback, please contact valeriamirza5@gmail.com.


