import json

dictionary = dict()
editItem = dict()

j = json.dumps(dictionary)

def opInsert():
    data = input('Enter a word and number separated by a ":" ') # Get user input
    temp = data.split(':') # Gets key and value in one input
    dictionary[temp[0]] = int(temp[1])
    
def opSave():
    with open('dictionary.json', 'w') as f:
            for key, value in dictionary.items(): 
                f.write(j)
                
def opModify():
    option =  input('Enter 1 to modify key, 2 to modify value: ')
    if option == 1:
        print(list(dictionary))
        print('Enter key value to modify: ')
        
        



print(dictionary)
operation = 0

while (operation < 9):
    print('Enter 1 for input, 2 to save: ')
    operation = int(input())
    
    if operation ==  1:
        opInsert()
        continue


    if operation == 2:
        opSave()
        continue
    
    if operation == 3:
        opModify()
        continue
    
print(dictionary)    

with open('dictionary.json', 'w') as f:
    f.close()
            
print(dictionary)


""" 
- Write input and save into if statements and have user choose operation to use
- Make operation loop if response is not valid
"""