import subprocess
import time
import sys

while True:
    try:
        # Open the bot.py file using the subprocess module
        bot_process = subprocess.Popen([sys.executable, 'bot.py'])
        
        # Wait for the given amount of seconds
        time.sleep(43200)  # 12 hours
        
        # Terminate the bot.py process
        bot_process.terminate()
        
        # Wait a short while to ensure the process is terminated properly
        time.sleep(5)
        
    except Exception as e:
        print("An error occurred:", e)
        # You might want to log or handle the error in a more appropriate way
    
    # Repeat the loop
