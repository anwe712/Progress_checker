# import OS
import os
# import datetime to see only today's file 
import datetime
#import pywhatkit to send messages
import pywhatkit as kit

recipient = '+91 8902485427'

hour = 18
minute = 10
message = "hello world"
today = datetime.date.today()
count = 0
today = datetime.date.today()
s = 0
dir_path = r'/home/anwesha/Videos'

for filename in os.listdir('.'):
    # Get the creation time of the file
    creation_time = datetime.date.fromtimestamp(os.path.getctime(filename))
    
for x in os.listdir(dir_path):
	if x.endswith(".mp4" or ".mov" or ".mkv") and (creation_time == today):
		count = count + 1       

for x in os.listdir(dir_path):
	if x.endswith(".jpg" or ".jpeg" ) and (creation_time == today):
		s = s + 1  
if os.path.exists(dir_path):
    files = os.listdir(dir_path)
    print(files)
else:
    print(f"The directory {dir_path} does not exist.")
print("::TODAY'S PROGRESS::")    
print("  Today's Date:", today)
print("NUMBER OF PICTURES:", s)
print('NUMBER OF VIDEOS:',count)

kit.sendwhatmsg(recipient, message, hour, minute)
