def word_count(title): 
    return len(title.split())

def characters(book):
    letters = {}
    lower = book.lower()
    for i in lower:
        if i in letters:
            letters[i]+=1
        else:
           letters[i]=1 
    return letters

def dictionary(letters):
    letter_list = []
    for letter in letters:
        if letter.isalpha():
            letter_dict={}
            number = letters[letter]
            letter_dict["char"]=letter
            letter_dict["num"]=number
            letter_list.append(letter_dict)
    letter_list.sort(reverse=True,key=sort_dict)
    return letter_list

def sort_dict(items):
    return items["num"]