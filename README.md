# SystemNotification
to notify user about system logged-in time

Prerequisites:
              pip install plyer

The program uses plyer module for notification and time module for tracking system time.

Algorithm:

1. Calculate the current time by using time module.
2. Set the target time for notification is equal to 5 hrs more than current time.
3. Run loop until current time is equal to system time.
4. If current time is equal to system time then send notification with some message and exit the loop.
