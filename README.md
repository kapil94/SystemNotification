# SystemNotification
to notify user about system logged-in time

Prerequisites:
              pip install plyer

The program uses plyer module for notification and time module for tracking system time.

Algorithm:

1. Calculate the current time by using time module.
2. Create a list of target_time starting from 1 hr from current time till 4 hrs from current time.
3. Run loop until current time is equal to target_time list item.
4. Check if current time is equal to target_time list item then send a notifiaction to user with message stating how many hours have passed since you logged-in.
5. Continue step 4 till end of target_time list and after that exit loop.
