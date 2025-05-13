def num_of_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def get_characters(text):
    characters = list(text.lower())
    char_count = {}
    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_dict(dict):
    list_of_dict = []
    for key in dict:
        key_value_pair = {}
        key_value_pair.update({"char": key, "num": dict[key]})
        list_of_dict.append(key_value_pair)
    
    def sort_on(a):
        return a["num"]
    
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

    

