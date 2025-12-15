def count_words(text):
    return len(text.split())


def count_characters(text):
    character_counts = {}
    for character in text.lower():
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return character_counts

def sort_on(items):
    return items["num"]

def sort_characters_by_count(character_counts):
    character_list = []
    for character in character_counts:
        character_list.append({'char': character, 'num': character_counts[character]})

    character_list.sort(reverse=True, key=sort_on)
    return character_list