from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert make_full_name("Bryant" , "Taylor") == "Taylor; Bryant"
    assert make_full_name("Kelsey" , "Leavitt-Taylor") == "Leavitt-Taylor; Kelsey"
    assert make_full_name("Dave" , "Hink") == "Hink; Dave"
    

def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_family_name("Taylor; Bryant") == "Taylor"
    assert extract_family_name("Leavitt-Taylor; Kelsey") == "Leavitt-Taylor"
    assert extract_family_name("Hink; Dave") == "Hink"
    

def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """

    assert extract_given_name("Taylor; Bryant") == "Bryant"
    assert extract_given_name("Leavitt-Taylor; Kelsey") == "Kelsey"
    assert extract_given_name("Hink; Dave") == "Dave"
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])