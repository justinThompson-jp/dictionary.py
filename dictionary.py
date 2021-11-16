dictionary = dict()
data = input('Enter a word and number separated by a ":" ') # Get user input
temp = data.split(':') # Gets key and value in one input
dictionary[temp[0]] = int(temp[1])

print(dictionary)