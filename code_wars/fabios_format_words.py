# ['ninja', 'samurai', 'ronin', 'one', 'two'] 
#     --> "ninja, samurai, ronin, one and two"

# ['ninja', 'samurai', 'ronin'] 
#     --> "ninja, samurai and ronin"
# ['ninja', '', 'ronin'] 
#     --> "ninja and ronin"
# [] -->""

# ['one', 'two', 'three', 'four'] 
#               'one, two, three, four, ' 
#  should equal 'one, two, three and four'
#               'one, two, three and four, '

#               'one, two, and threethree, four, ' 

# len(words) == 4
# words = ['one', 'two', 'three', 'four'] 
#          0      1      2        3

#i = 0 --  "one, "
#i = 1 --  "one, two, "
#i = 2 --  "one, two, three and"
#i = 3 --  "one, two, three and"

#words = ['one', 'two', '', 'three', 'four'] 

def cleanup_words(words):
    res = []
    for word in words:
        if word != "":
            res.append(word)
    return res
    


def format_words(words):
    if words == None: return ""
    
    words = cleanup_words(words)
    
    res = ''
    for i in range(len(words)):
        word = words[i]
        res += word
        
        if i == len(words) - 2:
            res += " and "
        elif i == len(words) - 1:
            pass
        else:
            res += ", "

    return res