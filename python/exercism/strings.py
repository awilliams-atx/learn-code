import string


def add_prefix_un(word: str) -> str:
    return "un" + word


def make_word_groups(vocab_words: list[str]) -> str:
    words = [
        word if idx == 0 else vocab_words[0] + word
        for idx, word in enumerate(vocab_words)
    ]
    return str.join(" :: ", words)


def remove_suffix_ness(word: str) -> str:
    word = word[:-4]
    return f"{word[:-1]}y" if word.endswith("i") else word


def adjective_to_verb(sentence: str, index: int) -> str:
    return sentence.strip(".").split(" ")[index] + "en"
