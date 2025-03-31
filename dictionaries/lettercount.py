def letter_counter(word):
    
    letters = {}
    for i in word:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
            
    return letters

print(letter_counter("Florianistsocool"))