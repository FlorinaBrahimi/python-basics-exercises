# 9.5 - Challenge: Wax Poetic
# Solution to challenge

# Import the random module to facilitate random selections
import random

# Define lists of words to be used in the poem: nouns, verbs, adjectives, prepositions, and adverbs
noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verb = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]
adjective = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]
preposition = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverb = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]

def make_poem():
    """Create a randomly generated poem, returned as a multi-line string."""
    
    # Pull three random nouns and ensure they are different
    n1 = random.choice(noun)
    n2 = random.choice(noun)
    n3 = random.choice(noun)
    
    # Ensure that all the nouns are different
    while n1 == n2:
        n2 = random.choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = random.choice(noun)

    # Pull three random verbs and ensure they are different
    v1 = random.choice(verb)
    v2 = random.choice(verb)
    v3 = random.choice(verb)
    
    # Ensure that all the verbs are different
    while v1 == v2:
        v2 = random.choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = random.choice(verb)

    # Pull three random adjectives and ensure they are different
    adj1 = random.choice(adjective)
    adj2 = random.choice(adjective)
    adj3 = random.choice(adjective)
    
    # Ensure that all the adjectives are different
    while adj1 == adj2:
        adj2 = random.choice(adjective)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = random.choice(adjective)

    # Pull two different prepositions
    prep1 = random.choice(preposition)
    prep2 = random.choice(preposition)
    
    # Ensure the prepositions are different
    while prep1 == prep2:
        prep2 = random.choice(preposition)

    # Pull one adverb
    adv1 = random.choice(adverb)

    # Determine the correct article based on the first letter of the first adjective
    if "aeiou".find(adj1[0]) != -1:  # Check if the first letter is a vowel
        article = "An"
    else:
        article = "A"

    # Create the poem structure using the randomly selected words
    poem = (
        f"{article} {adj1} {n1}\n\n"
        f"{article} {adj1} {n1} {v1} {prep1} the {adj2} {n2}\n"
        f"{adv1}, the {n1} {v2}\n"
        f"the {n2} {v3} {prep2} a {adj3} {n3}"
    )

    return poem

# Generate the poem and print it
poem = make_poem()
print(poem)
