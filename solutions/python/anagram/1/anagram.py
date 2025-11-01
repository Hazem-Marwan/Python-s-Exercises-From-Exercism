def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())

    result = []
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue

        if sorted_word == sorted(candidate.lower()):
            result.append(candidate)

    return result