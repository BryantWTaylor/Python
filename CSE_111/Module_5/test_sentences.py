from sentences import get_determiner, get_noun, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners



def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):
        # Call the get_noun function which
        # should return a single noun.
        noun = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert noun in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):
        # Call the get_noun function which
        # should return a plural noun.
        noun = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert noun in plural_nouns



def test_get_verb():

    # 1. Test the past tense verbs

    past_tense_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):
        # Call the get_verb function which
        # should return a past tense verb.
        verb = get_verb(1, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past_tense_verbs list.
        assert verb in past_tense_verbs

    # 2. Test the future tense verbs

    future_tense_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):
        # Call the get_verb function which
        # should return a future tense verb.
        verb = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future_tense_verbs list.
        assert verb in future_tense_verbs

    # 3. Test the present tense single verbs

    present_tense_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):
        # Call the get_verb function which
        # should return a present tense single verb.
        verb = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_tense_single_verbs list.
        assert verb in present_tense_single_verbs

    # 4. Test the present tense plural verbs

    present_tense_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):
        # Call the get_verb function which
        # should return a present tense plural verb.
        verb = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_tense_plural_verbs list.
        assert verb in present_tense_plural_verbs

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])