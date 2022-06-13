import pyperclip
import datetime

print('Time to get the time')

now = datetime.datetime.utcnow()
nowformated = now.strftime("%Y.%m.%d.%H.%M.%S")

# Print the current time in UTC format to the console
print(nowformated)

print('The time will be copied to your clipboard')

# Copy the current time to the clipboard
pyperclip.copy(nowformated)