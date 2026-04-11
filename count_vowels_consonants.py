s="machinelearning"
    vowels=[]
    consonants=[]
    for ch in s:
        if ch.lower() in "aieou":
            vowels.append(ch)
        else:
            consonants.append(ch)
print("VOWELS : ",vowels)
print("CONSONANTS : ",consonants)



