import time

for i in range(5):
    print(f"\rProgress: {i*20}%", end="")
    time.sleep(0.5)
print("\rComplete!       ") # Overwrite the last progress message
# Output (on a single line, updating in place):
# Progress: 0%
# Progress: 20%
# ...
# Complete!