def rem_vowels(s):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in s:
        if x in vowels:
            s = s.replace(x, "")
    print(s)


s = input()
rem_vowels(s)
