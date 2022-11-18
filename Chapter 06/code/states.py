import os
from kanren import run, fact, eq, Relation, var

adjacent = Relation()
coastal = Relation()

file_coastal = 'coastal_states.txt'
file_adjacent = 'adjacent_states.txt'
os.chdir(r'C:\\Users\\tanvi\\Documents\\GitHub\\test\\Artificial-Intelligence-with-Python\\Chapter 06\\code')

# Read the file containing the coastal states
with open(file_coastal, 'r') as f:
    line = f.read()
    coastal_states = line.split(',')

# Add the info to the fact base
for state in coastal_states:
    fact(coastal, state)

# Read the file containing the coastal states
with open(file_adjacent, 'r') as f:
    adjlist = [line.strip().split(',') for line in f if line and line[0].isalpha()]

# Add the info to the fact base
for L in adjlist:
    head, tail = L[0], L[1:]
    for state in tail:
        fact(adjacent, head, state)

# Initialize the variables
x = var()
y = var()

# Is Western Australia adjacent to Northern Territory?
output = run(0, x, adjacent('Northern Territory','Western Australia' ))
print('\nIs Northern Territory adjacent to Western Australia?:')
print('Yes' if len(output) else 'No')

# States adjacent to New South Wales
output = run(0, x, adjacent('New South Wales', x))
print('\nList of states adjacent to New South Wales:')
for item in output:
    print(item)

# List of states that adjacent to the two given states
output = run(0, x, adjacent('Western Australia', x), adjacent('Northern Territory', x))
print('\nList of states that are adjacent to Western Australia and Northern Territory:')
for item in output:
    print(item)

# Is Victoria adjacent to South Australia?
output = run(0, x, adjacent('Victoria', 'South Australia'))
print('\nIs Victoria adjacent to South Australia?:')
print('Yes' if len(output) else 'No')