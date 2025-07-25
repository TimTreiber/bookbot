def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(booktext):
    words = booktext.split()
    return len(words)

def count_characters(booktext):
    chars = {}
    booktext_lower = booktext.lower()
    for char in booktext_lower:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1            
    return chars

def sort_on(items):
    return items["num"]

def sort_dictionary(dict_unsorted):
    dict_sorted = []
    for num in dict_unsorted:
        number = dict_unsorted[num]
        dict_sorted.append({"char": num, "num": number})
    #print(dict_sorted)
    dict_sorted.sort(reverse=True, key=sort_on)
    #print(dict_sorted)
    return dict_sorted
