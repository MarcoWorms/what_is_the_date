import shutil
import re
import subprocess
from datetime import datetime
from datetime import timedelta

tomorrow = "Feb 22 2015 03:11AM"
today = "Feb 21 2015 03:10AM"

#STOP DO NOT USE ABOVE VARIABLES IN YOUR LOOP
#YOU WILL MAKE KITTENS SAD

this_script = open("test.py")
new_script = open("test_new.py", "w")

#YOUR CODE STARTS HERE
today_today = ''
new_file = []

for line in this_script:
    has_tomorrow = re.search(r'^tomorrow = "([^"]*)"', line)
    if has_tomorrow:
    	today_today = has_tomorrow.group(1)
    	today_today_datetime = datetime.strptime(today_today, '%b %d %Y %I:%M%p') + timedelta(days=1,minutes=1)
        tomorrow_tomorrow = datetime.strftime(today_today_datetime, '%b %d %Y %I:%M%p')
        new_line = 'tomorrow = "<<<TOMORROW>>>"\n'
    elif re.search(r'^today = "[^"]*"', line):
    		new_line = 'today = "<<<TODAY>>>"\n'
    else:
        new_line = line
    new_file.append(new_line)

lines = ''
for line in new_file:
    if re.search(r'^tomorrow = "([^"]*)"', line):
        lines += 'tomorrow = "' + tomorrow_tomorrow + '"\n'
    elif re.search(r'^today = "[^"]*"', line):
        lines += 'today = "' + today_today + '"\n'
    else:
        lines += line

#YOUR CODE ENDS HERE
new_script.write(lines)
this_script.close()
new_script.close()

shutil.move("test_new.py", "test.py")

subprocess.call("git add test.py" ,shell=True)
subprocess.call("git commit -m 'Fixed the time'" ,shell=True)
subprocess.call("git push", shell=True)

print today_today
print tomorrow_tomorrow

print "actual today " + datetime.strftime(datetime.now(), '%b %d %Y %I:%M%p')
