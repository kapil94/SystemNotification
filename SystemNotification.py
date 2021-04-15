########################system notification example####################################
from plyer import notification
import time,sys

current_time=""
target_time=""
flag=True

seconds=time.time()
local_time=time.ctime(seconds)
current_time+=local_time[11:19]
target_time+=str(int(current_time[0:2])+5)+current_time[2:len(current_time)]

target_time_list=[]

for i in range(1,5):
	target_time_list.append(str(int(current_time[0:2])+i)+current_time[2:len(current_time)])

count=len(target_time_list)

def exit_loop():
	sys.exit(0)

while flag:
	
	seconds=time.time()
	local_time=time.ctime(seconds)
	current_time=""
	current_time+=local_time[11:19]
		
	for i in range(0,len(target_time_list)):	
		
		if current_time==target_time_list[i]:
		
			notification.notify(
	    			title='Beep beep beep ....',
	    			message='Dude get a life!! '+str(i)+' hrs have passed since you logged in..',
	    			app_icon=None, 
	    			timeout=10,  
				)	
			count=count-1
			
			if count==0:
				
				exit_loop()
				

		
	
	
