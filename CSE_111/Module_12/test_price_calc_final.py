from price_calc_final import get_lens_price, get_combined_price
from pytest import approx
import pytest

def test_get_lens_price():
    """Test the get_lens_price function by calling it and comparing the values it returns to the expected values. """

    assert get_lens_price("single vision", "y") == 79.99
    assert get_lens_price("single vision", "n") == 59.99
    assert get_lens_price("progressive", "y") == 159.99
    assert get_lens_price("progressive", "n") == 129.99

def test_get_combined_price():
    """Test the get_combined_price function by calling it and comparing the values it returns to the expected values. This test function will also call the get_lens_price function as that is how it will run in the program."""

    assert get_combined_price(get_lens_price("single vision", "y"), 59.99) == approx(139.98)
    assert get_combined_price(get_lens_price("single vision", "n"), 64.99) == approx(124.98)
    assert get_combined_price(get_lens_price("progressive", "y"), 99.99) == approx(259.98)
    assert get_combined_price(get_lens_price("progressive", "n"), 89.99) == approx(219.98)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])