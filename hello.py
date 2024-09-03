# hello_world_time/hello.py

import os
import time

def print_time_and_message():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Current OS Time: {current_time}")
    print("Hello, World!")

if __name__ == "__main__":
    print_time_and_message()
