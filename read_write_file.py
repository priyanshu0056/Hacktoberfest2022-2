filename = "cities.txt"

# Open file for writing
fileHandler = open(filename, "w")

# add cities
fileHandler.write("New York\n")
fileHandler.write("Washington\n")
fileHandler.write("Los Angeles\n")

# Close the file
fileHandler.close()

# Open file for reading
lines = open(filename, "r")

# Reading a file line by line
for line in lines:
print(line)

# Close the file
fileHandler.close()
