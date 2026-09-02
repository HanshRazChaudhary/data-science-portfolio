# Syntax To Create File And 
file = open("youtube.txt", 'w')

try:
    file.write("Python Is Good Language!")
finally:
    file.close()

# Another Synatax To Create A File With 'with' Keyword:
# with open ('youtube.txt', 'w') as file:
#     file.write("Python Is Good Langauage!")