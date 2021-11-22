import json

# Load dictionary from json file
with open('dictionary.json') as f:
    dictionary = json.load(f)

def opInsert():
    key = input("enter key: ")
    value = input("enter value: ")
    dictionary[key] = value
    print(dictionary)
    
def opSave():
    with open('dictionary.json', 'w') as f:
        json.dump(dictionary, f)
                
def opModify():
    option = 0
    while (option < 3):
        option = int(input('Enter 1 to modify key, 2 to modify value: '))
        
        if option == 1:
            print(list(dictionary))
            x = input('Enter key to modify: ')
            y = dictionary.pop(x)
            newKey = input('Enter new key: ')
            key = newKey
            value = y
            dictionary[key] = value
            continue
       
        if option == 2:
            keyList = list(dictionary.keys())
            valList = list(dictionary.values())
            print(valList)
            x = input("Enter value to modify: ")
            pos = valList.index(x)
            key = keyList[pos]
            newValue = input("Enter new value: ")
            dictionary[key] = newValue
            
def opDelete():
    option = 0
    while (option < 3):
        option = int(input('Enter 1 to delete by key, 2 to delete by value: '))
        
        if option == 1:
            print(list(dictionary))
            x = input("Choose key to delete: ")
            del dictionary[x]
            print(dictionary)
            print("\n")
            
        if option == 2:
            keyList = list(dictionary.keys())
            valList = list(dictionary.values())
            print(valList)
            x = input("Enter value to delete: ")
            pos = valList.index(x)
            key = keyList[pos]
            del dictionary[key]
            print(dictionary)
            print("\n")
    
        
        
        
operation = 0

while (operation < 9):
    print('Enter 1 for input, 2 to save, 3 to modify, 4 to delete: ')
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
    
    if operation == 4:
        opDelete()
        continue
            
print(dictionary)


""" 
- Write input and save into if statements and have user choose operation to use
- Make operation loop if response is not valid
"""