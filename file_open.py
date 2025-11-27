import os
import subprocess
import sys


def open_json(filepath):
    
    try:
        #This is for windows using os
        if sys.platform == "win32":
            os.startfile(filepath)
        #This is for mac using subprocess
        elif sys.platform == "darwin":
            subprocess.call(('open', filepath))
        #This is for other operating systems such as Linux
        else:
            subprocess.call(('xdg-open', filepath))
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        