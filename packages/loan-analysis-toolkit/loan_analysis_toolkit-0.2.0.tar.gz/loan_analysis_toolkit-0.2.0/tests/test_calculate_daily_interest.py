import pytest
from loan_analysis_toolkit.schedule import calculate_daily_interest


def test_calculate_daily_interest_valid():
    # Test with valid inputs
    principal = 1000
    annual_rate = 5  # 5% annual interest
    daily_rate = annual_rate / 100 / 365
    expected_interest = principal * daily_rate
    assert calculate_daily_interest(principal, annual_rate) == pytest.approx(expected_interest)

def test_calculate_daily_interest_zero_principal():
    # Test with zero principal
    principal = 0
    annual_rate = 5
    assert calculate_daily_interest(principal, annual_rate) == 0

def test_calculate_daily_interest_zero_rate():
    # Test with zero interest rate
    principal = 1000
    annual_rate = 0
    assert calculate_daily_interest(principal, annual_rate) == 0
