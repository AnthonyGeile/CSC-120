def pair_frequencies(word_list):
    combinations = []
    final = {}
    for word in word_list:
        for i in range(len(word)-1):
            combinations.append(word[i] + word[i+1])
    for combo in combinations:
        if combo in final:
            final[combo] += 1
        else:
            final[combo] = 1
    return final

print(pair_frequencies(['banana', 'bends', 'i', 'mend', 'sandy']))