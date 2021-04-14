########################system notification example####################################
from plyer import notification
import time

current_time=""
target_time=""
flag=True

seconds=time.time()
local_time=time.ctime(seconds)
current_time+=local_time[11:19]
target_time+=str(int(current_time[0:2])+5)+current_time[2:len(current_time)]



while flag:
	
	seconds=time.time()
	local_time=time.ctime(seconds)
	current_time=""
	current_time+=local_time[11:19]
		
	
	if current_time==target_time:
		
		notification.notify(
    			title='Beep beep beep ....',
    			message='Dude get a life!!',
    			app_icon=None, 
    			timeout=10,  
			)	

		flag=False
		
	
