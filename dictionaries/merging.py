
a = ["a", "b", "c", "d"]
b = [10,20,30,40]

c = dict(zip(a,b))

#"hello my name is florian"
def return_lettersamount(str):
    letters = {}

    for i in str:
        letter = i.lower()
        if i.isalpha():
            letters[letter] = letters.get(letter,0) + 1
    return dict(sorted(letters.items()))
print(return_lettersamount("hello my name is Florian"))
