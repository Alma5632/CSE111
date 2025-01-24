import random

# This program generates random sentences with varying grammatical structures
# using simple rules based on the quantity (singular or plural) and tense (past, present, future).
# The creativity lies in combining basic linguistic components (determiners, nouns, verbs, adjectives, and prepositions)
# in a flexible way to produce unique and grammatically diverse sentences each time the program runs.
# A fun feature of the program is its ability to automatically adjust the verb form according to both
# the quantity and tense of the sentence, making it feel dynamic and personalized.
# By using random.choice(), the program ensures that no two sentences are exactly alike, keeping the output fresh and engaging.
# It's an excellent exercise in understanding parts of speech, sentence structure, and how logic can drive sentence formation.
# Done by Chris Kofi Owusu, Assignment Type: Prove: Sentences, Course CSE 111


def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think",
                     "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    word = random.choice(words)
    return word

def get_preposition():
    words = ["about", "above", "across", "after", "along",
             "around", "at", "before", "behind", "below",
             "beyond", "by", "despite", "except", "for",
             "from", "in", "into", "near", "of",
             "off", "on", "onto", "out", "over",
             "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

def get_adjective():
    words = ["quick", "lazy", "sleepy", "noisy", "hungry",
             "happy", "sad", "angry", "brave", "calm"]
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {adjective} {noun} {verb} {prepositional_phrase1} {prepositional_phrase2}."
    return sentence

def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()