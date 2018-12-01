import sys

def calculate_frequency(lines):
    frequency = 0
    
    for line in lines:
        frequency += int(line)
    
    return frequency

if len(sys.argv) <= 1 :
    sys.exit("You have to provide filepath")

path = sys.argv[1]

try:
    f = open(path, "r")
except FileNotFoundError:
    print("File not found")
except IOError as err:
    print("Can't read the file", err)
else:
    lines = f.readlines()
    frequency = calculate_frequency(lines)
    print(frequency)
     