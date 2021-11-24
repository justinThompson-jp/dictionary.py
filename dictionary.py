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
    print('Saved dictionary:', dictionary)
                
def opModify():
    option = str(input('Enter 1 to modify key, 2 to modify value, or 0 to cancel: '))
        
    if option == str(1):
        print(list(dictionary))
        x = input('Enter key to modify: ')
        y = dictionary.pop(x)
        newKey = input('Enter new key: ')
        key = newKey
        value = y
        dictionary[key] = value
    
    if option == str(2):
        keyList = list(dictionary.keys())
        valList = list(dictionary.values())
        print(valList)
        x = input("Enter value to modify: ")
        pos = valList.index(x)
        key = keyList[pos]
        newValue = input("Enter new value: ")
        dictionary[key] = newValue
        
    if option == str(0):
        return
        
    else:
        opModify()
            
def opDelete():
    option = str(input('Enter 1 to delete by key, 2 to delete by value, or 0 to cancel: '))
        
    if option == str(1):
        print(list(dictionary))
        x = input("Choose key to delete: ")
        del dictionary[x]
        print(dictionary)
        print("\n")
            
    if option == str(2):
        keyList = list(dictionary.keys())
        valList = list(dictionary.values())
        print(valList)
        x = input("Enter value to delete: ")
        pos = valList.index(x)
        key = keyList[pos]
        del dictionary[key]
        print(dictionary)
        print("\n")
        
    if option == str(0):
        return
        
    else:
        opDelete()
        
        
        
def opSearch():
    option = str(input('Enter 1 to search by key, 2 to search by value, or 0 to cancel: '))
        
    if option == str(1):
        print(list(dictionary))
        x = input('Enter key: ')
        print(dictionary.get(x))
    
    if option == str(2):
        keyList = list(dictionary.keys())
        valList = list(dictionary.values())
        print(valList)
        def searchValue():
            x = input("Enter value: ")
            if x in dictionary.values():
                pos = valList.index(x)
                print(keyList[pos])
            if x not in dictionary.values():
                searchValue()
        searchValue()
        
    if option == str(0):
        return
    
    else:
        opSearch()
        
def opSort():
    option = str(input('Enter 1 to sort by key, 2 to sort by value, or 0 to cancel: '))
        
    if option == str(1):
        print(sorted(dictionary.items()))
    
    if option == str(2):
        print(sorted(dictionary.items(), key=lambda kv:kv[1]))
        
    if option == str(0):
        return
    
    else:
        opSort()        
    
        
        
def main():        
    operation = str(input('Enter a number\n 1 - Add\n 2 - Search\n 3 - Edit\n 4 - Delete\n 5 - Sort\n 6 - Print\n 9 - Save\n 0 - End: '))
        
    if operation == str(1):
        opInsert()

    if operation == str(2):
        opSearch()

    if operation == str(3):
        opModify()

    if operation == str(4):
        opDelete() 
    
    if operation == str(5):
        opSort() 

    if operation == str(6):
        print(dictionary)
    
    if operation == str(9):
        opSave()

    if operation == str(0):
        return
    
    else:
        main()


main()            
print(dictionary)