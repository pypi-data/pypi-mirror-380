import pytest
from unittest.mock import patch
from loan_analysis_toolkit.schedule import prepare_loan_summary

@pytest.fixture
def valid_loan_params():
    return {
        "start_date": "2023-01-01",
        "loan_amount": 500000,
        "annual_rate": 5.0,
        "loan_duration_years": 30,
        "loan_duration_months": 0,
        "repayment_frequency": "monthly",
        "initial_offset_amount": 10000,
        "offset_contribution_frequency": "monthly",
        "offset_contribution_regular_amount": 500,
        "extra_repayments_frequency": "annually",
        "extra_repayments_regular_amount": 5000,
        "capture_interest_accrual": True
    }

@patch("loan_analysis_toolkit.schedule.inputval_prepare_loan_summary")
def test_prepare_loan_summary_valid(mock_input_validation, valid_loan_params):
    result = prepare_loan_summary(valid_loan_params)
    
    # Check if the result contains the expected keys
    assert "all_transactions" in result
    assert "monthly_summary" in result
    assert "total_interest_charged" in result
    assert "total_repayments" in result

    # Check if the total interest and repayments are floats
    assert isinstance(result["total_interest_charged"], float)
    assert isinstance(result["total_repayments"], float)

    # Check if all_transactions and monthly_summary are DataFrames
    assert hasattr(result["all_transactions"], "columns")
    assert hasattr(result["monthly_summary"], "columns")

@patch("loan_analysis_toolkit.schedule.inputval_prepare_loan_summary")
def test_prepare_loan_summary_zero_loan_amount(mock_input_validation):
    loan_params = {
        "start_date": "2023-01-01",
        "loan_amount": 0,
        "annual_rate": 5.0,
        "loan_duration_years": 30,
        "loan_duration_months": 0,
        "repayment_frequency": "monthly",
        "initial_offset_amount": 10000,
        "offset_contribution_frequency": "monthly",
        "offset_contribution_regular_amount": 500,
        "extra_repayments_frequency": "annually",
        "extra_repayments_regular_amount": 5000,
        "capture_interest_accrual": True
    }
    result = prepare_loan_summary(loan_params)
    
    # Check if the total interest and repayments are zero
    assert result["total_interest_charged"] == 0
    assert result["total_repayments"] == 0

@patch("loan_analysis_toolkit.schedule.inputval_prepare_loan_summary")
def test_prepare_loan_summary_zero_interest_rate(mock_input_validation, valid_loan_params):
    valid_loan_params["annual_rate"] = 0
    result = prepare_loan_summary(valid_loan_params)
    
    # Check if the total interest charged is zero
    assert result["total_interest_charged"] == 0

@patch("loan_analysis_toolkit.schedule.inputval_prepare_loan_summary")
def test_prepare_loan_summary_invalid_frequency(mock_input_validation, valid_loan_params):
    valid_loan_params["repayment_frequency"] = "invalid_frequency"
    
    with pytest.raises(ValueError, match="Invalid repayment frequency"):
        prepare_loan_summary(valid_loan_params)