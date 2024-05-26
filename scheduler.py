import time
import sched
import threading
from email_sender import send_email
from database import get_tasks_due_within_hour
from database import update_last_notified

scheduler = sched.scheduler(time.time, time.sleep)


def schedule_task():
    scheduler.enter(60, 1, check_and_send_emails)
    scheduler.run()


def check_and_send_emails():
    tasks = get_tasks_due_within_hour()
    for task_ in tasks:
        task_id, to_email, task, due_date = task_
        subject = f"Task Reminder: {task} "
        content = f"Task: {task} \nDue Date: " + \
                  f"{due_date.strftime('%Y-%m-%d %H:%M')}"
        success, message = send_email(to_email, subject, content)
        if success:
            print(f"Email sent to {to_email} successfully.")
            update_last_notified(task_id)
        else:
            print(f"Failed to send email to {to_email}: {message}")
    schedule_task()


def start_scheduler():
    thread = threading.Thread(target=schedule_task)
    thread.daemon = True
    thread.start()
