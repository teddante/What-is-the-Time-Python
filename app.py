import datetime

import pyperclip

print('Time to get the time')

now = datetime.datetime.utcnow()
nowFormatted = now.strftime("%Y.%m.%d.%H.%M")

# Print the current time in UTC format to the console
print(nowFormatted)

print('The time will be copied to your clipboard')

# Copy the current time to the clipboard
pyperclip.copy(nowFormatted)
