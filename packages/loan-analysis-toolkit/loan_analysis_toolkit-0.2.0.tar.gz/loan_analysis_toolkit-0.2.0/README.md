
# Loan Analysis Toolkit
This packages generates all transactions and an interest schedule for loan accounts such as home loans. It runs daily interest accrual which makes it more accurate than simple formula based calculations. Most banks calculates interests daily and charge them monthly. This package mimics that process. In runs through a daily loop and performs calculation until the loan is paid off.  

## Technical Documentation
https://salaken-ds.github.io/loan_analysis_toolkit/

## Features:
- calculates daily interest which makes the schedule very accurate
- adjusts account balance on repayment dates
- charges interest on monthly loan anniversary e.g. if loan is settled on the 3rd of the month then interest is always charged on the 3rd of the month
- supports offset account with zero or non-zero initial balance
- regular contribution of offset account
- returns (1) all transactions, (2) monthly summary containing interest charged, repayment, loan balance and offset account balance and (3) total interest charged to the customer

## Assumption:
- Daily interest charge is based on 365 days in a year, even in a leap year. This is because most Australian bank does it that way.

## Usage examples:
- Generate all transactions to the loan account to cross-check against bank. Helps to make sure bank is not making any mistakes. (_It may sound surprising, but banks DO make a lot of mistakes!_)
- Calculate interest savings by adding an offset account, and making regular contributions. This helps creating strategies to pay out the loan faster and helps with financial wellbeing.

```
from loan_analysis_toolkit.schedule import prepare_loan_summary


if __name__ == "__main__":
    # loan parameters
    loan_amount = 650_000  # Loan amount in dollars
    annual_rate = 5.34     # Annual interest rate in percentage
    loan_duration_years = 30          # Loan term in years
    loan_duration_months = 0          # Additional months in loan term
    start_date = '2025-10-05'  # Loan settlement date
    repayment_frequency = 'fortnightly'  # Repayment frequency
    initial_offset_amount = 20_000  # Initial offset account balance in dollars
    offset_contribution_frequency = 'monthly'  # Offset contribution frequency
    offset_contribution_regular_amount = 500  # Offset contribution amount in dollars

    loan_parameters = {'loan_amount' : loan_amount,
                   'annual_rate' : annual_rate,
                   'loan_duration_years' : loan_duration_years,
                   'loan_duration_months' : loan_duration_months,
                   'start_date' : start_date,
                   'repayment_frequency' : repayment_frequency,
                   'initial_offset_amount' : initial_offset_amount,
                   'offset_contribution_frequency' : offset_contribution_frequency,
                   'offset_contribution_regular_amount' : offset_contribution_regular_amount
                   }

    res = prepare_loan_summary(loan_parameters, store_results = True)

    total_interest_paid_by_customer = res['total_interest_charged']
    print("total interested paid by the customer: {}".format(total_interest_paid_by_customer))
    print(res['monthly_summary'].head())
```

## Contributions
Please raise a pull request outlining changes.

## Others
- Pre-requisite: `uv` (either `pip install uv` or see https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)
- Clone and then build using: `uv build`
- Local install into another virtual environment using the built package (assuming you're currently in directory `xyz` which is at the same level as `loan_analysis_toolkit`):
`uv pip install ../loan_analysis_toolkit/dist/loan_analysis_toolkit-0.1.0.tar.gz`