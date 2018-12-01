import sys

def find_frequency(lines):
    past_frequencies = {}
    frequency = 0
    
    while True:
        for line in lines:
            frequency += int(line)
            
            if frequency in past_frequencies:
                return frequency
            else:
                past_frequencies[frequency] = True

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
    frequency = find_frequency(lines)
    print(frequency)
