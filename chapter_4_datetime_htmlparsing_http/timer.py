# Create a Timer with the Time Module
import time

start = input('To start, write "yes". Start?: ')

seconds = 0

if start.lower() == 'yes':
    while seconds != 10:
        seconds += 1
        if seconds == 1:
            phrase = 'second has passed.'
        else:
            phrase = 'seconds have passed.'
        print(f'\t > {seconds} {phrase}')

        time.sleep(1) # Pauses the execution for 1 second
