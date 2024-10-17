def capitalize_title(title: str) -> str:
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    return sentence.replace(old_word, new_word)
