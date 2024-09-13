def duplicate_count(text):
    new_text=text.lower()
    new = []
    repeated = []
    for item in new_text:
        if item not in new:
            new.append(item)
    count = 1
    for item in new:
        for item1 in new_text:
            if item1 == item:
                count +=1
        if count >2:
            repeated.append(item)
        count = 1
    print(repeated) 
    
    # Your code goes here
duplicate_count("aA11awwwdrf")