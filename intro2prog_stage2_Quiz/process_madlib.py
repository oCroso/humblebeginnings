#Lesson 10 Mad Libs Generator

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    processed = ""
    checkstart = 0
    boxlength = 4
    while checkstart != len(mad_lib):
        currentword = mad_lib[checkstart:checkstart + boxlength]
        addword = word_transformer(currentword)
        processed += addword
        if len(addword) == 1:
            checkstart += 1
        else:
            checkstart += 4
    return processed
    
test_string_0 = "Test NOUN"    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_0)
print process_madlib(test_string_1)
print process_madlib(test_string_2)
