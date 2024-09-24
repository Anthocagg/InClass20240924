# dictionaries.py

def demo():
    """
    Demonstrate basic dictionary stuff
    """

    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)

    # Iterate over the dictionary by key - pretty much steps though them one at a time when printed
    for key in myDictionary.keys():
        print(key)

    # Iterate by key/value
    for item in myDictionary.items():
        print(item)

    #Iterate by value
    for value in myDictionary.values():
        print(value)

    # Add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"

    print(len(myDictionary))

    #Cause an exception . Add try/except logic to
    # handle this
    try:
        print(myDictionary["Ohio State"])
    except:
        print("Ohio State is an invalid key")


    # Reomove Xaiver by key and print the entire dictionary
    
    myDictionary.pop("Xavier")
    print(myDictionary)

    # Create another dictionary called newTeams
    # Add several key/valye pairs
    #Combine that with my dictionary and print the results
    newTeams = {"Delaware": "Hawks", "Nebraska": "Rutgers"}
    myDictionary.update(newTeams)
    print(myDictionary)
