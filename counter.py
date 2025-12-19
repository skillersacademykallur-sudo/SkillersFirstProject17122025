import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")

countdown(10)  # counts down from 10 seconds
