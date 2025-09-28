from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
from .utils import inputval_prepare_loan_summary


def calculate_minimum_repayment(principal, annual_rate, years, months, repayment_frequency='annual'):
    """
    Calculate the minimum repayment amount for a home loan using the compound interest formula.
    Uses PMT formula to calculate the minimum repayment amount.
    Does not return the toal repayment amount over the life of the loan as 
    it would be inaccurate due to daily compounding of interest.
    Args:
        principal (float): The loan amount (principal).
        annual_rate (float): The annual interest rate (in percentage, e.g., 5 for 5%).
        years (int): The loan term in years.
        repayment_frequency (str): The repayment frequency ('annual', 'monthly', 'quarterly').

    Returns:
        float: The minimum repayment amount per period.
    """
    # Convert annual interest rate from percentage to decimal
    rate = annual_rate / 100

    # total loan duration in years, including months converted to years
    years += months / 12

    # Determine the number of payments per year based on the repayment frequency
    if repayment_frequency == 'annual':
        payments_per_year = 1
    elif repayment_frequency == 'monthly':
        payments_per_year = 12
    elif repayment_frequency == 'fortnightly':
        payments_per_year = 26
    elif repayment_frequency == 'weekly':
        payments_per_year = 52
    elif repayment_frequency == 'quarterly':
        payments_per_year = 4
    else:
        raise ValueError("Invalid repayment frequency. Choose 'weekly', 'fortnightly', 'annual', 'monthly', or 'quarterly'.")

    periodic_rate = rate / payments_per_year
    total_payments_count = payments_per_year * years

    # PMT = P * [r(1+r)^n] / [(1+r)^n - 1]
    if periodic_rate == 0:  # If interest rate is 0%
        minimum_repayments = principal / total_payments_count
    else:
        minimum_repayments = principal * (periodic_rate * (1 + periodic_rate) ** total_payments_count) / \
                             ((1 + periodic_rate) ** total_payments_count - 1)
    
    return minimum_repayments

def calculate_daily_interest(loan_balance, annual_rate):
    """
    Calculate the daily interest on the loan balance.
    
    Args:
        loan_balance (float): The current loan balance.
        annual_rate (float): The annual interest rate (in percentage, e.g., 5 for 5%).
    
    Returns:
        float: The daily interest amount.
    """
    daily_rate = (annual_rate / 100) / 365
    daily_interest = loan_balance * daily_rate
    return daily_interest

def find_relevant_dates(start_date, end_date, frequency):
    """
    Generate a list of  dates between start_date and end_date based on the specified frequency.
    
    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.
        frequency (str): The frequency of dates ('weekly', 'fortnightly', 'monthly', 'quarterly', 'annually').
    
    Returns:
        list: A list of datetime objects representing the dates.
    """
    
    dates = []
    current_date = start_date

    while current_date <= end_date:
        dates.append(current_date)
        if frequency == 'daily':
            current_date += timedelta(days=1)
        elif frequency == 'weekly':
            current_date += timedelta(weeks=1)
        elif frequency == 'fortnightly':
            current_date += timedelta(weeks=2)
        elif frequency == 'monthly':
            current_date += relativedelta(months=1)
        elif frequency == 'quarterly':
            current_date += relativedelta(months=3)
        elif frequency == 'annually':
            current_date += relativedelta(years=1)
        else:
            raise ValueError("Invalid frequency. Choose 'daily','weekly', 'fortnightly', 'monthly', 'quarterly', or 'annually'.")

    return dates


def calculate_end_date(start_date=datetime.now(), years:int=0, months:int=0):
    """
    Calculate the end date based on the start date, duration in years, and duration in months.

    Args:
        start_date (datetime): The start date in datetime format. Defaults to current time which is then converted to tomorrow.
        years (int): The duration in years.
        months (int): The duration in months.

    Returns:
        datetime: The calculated end date as a datetime object.
    """
    # If no start date is provided, default to tomorrow
    if start_date is None:
        start_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    
    # Add years and months to the start date
    end_date = start_date + relativedelta(years=years, months=months)
    
    return end_date


def generate_loan_transactions(start_date, loan_amount, annual_rate,
                               initial_offset_amount, minimum_repayments,
                               all_dates, interest_charge_dates, repayment_dates, 
                               offset_contribution_dates, offset_contribution_regular_amount,
                               extra_repayments_dates, extra_repayments_regular_amount,
                               capture_interest_accrual: bool = False):
    """
    Generate a loan schedule including repayments, interest charges, loan balance and offset.

    Args:
        loan_amount (float): The loan amount (principal).
        initial_offset_amount (float): The initial amount in the offset account.
        minimum_repayments (float): The minimum repayment amount per period.
        all_dates (list): A list of all dates to iterate through (daily).
        interest_charge_dates (list): A list of dates when interest is charged (monthly).
        offset_contribution_dates (list): A list of dates when offset contributions are made.
        offset_contribution_regular_amount (float): The regular amount contributed to the offset account.
        extra_repayments_dates (list): A list of dates when extra repayments are made.
        extra_repayments_regular_amount (float): The regular amount for extra repayments.
        capture_interest_accrual (bool): Whether to capture daily and monthly interest accruals in the transactions. Default is False.

    Returns:
        pd.DataFrame: A DataFrame containing the loan schedule.
    """
    monthly_interest = 0
    current_loan_balance = loan_amount
    offset_amount = initial_offset_amount
    transactions = []
    # first entry to transactions is the settlement
    # format: transaction date, transaction type, transaction amount, loan_balance, offset_balance
    transactions.append([start_date, 'Settlement', loan_amount, loan_amount, offset_amount])
    
    
    for c_date in all_dates:
        interest_chargeable_amount = current_loan_balance - offset_amount
        minimum_repayments = min(minimum_repayments, current_loan_balance)  # to ensure we don't pay more than the remaining loan balance
        daily_interest = calculate_daily_interest(interest_chargeable_amount, annual_rate)
        daily_interest = max(daily_interest, 0)  # to ensure interest is not negative
        monthly_interest += daily_interest
        if capture_interest_accrual:
            transactions.append([c_date, 'Daily Interest Acrrued', daily_interest, current_loan_balance, offset_amount])
            transactions.append([c_date, 'Monthly Interest Acrrued', monthly_interest, current_loan_balance, offset_amount])
        if c_date in interest_charge_dates:
            current_loan_balance += monthly_interest
            transactions.append([c_date, 'Interest Charged', monthly_interest, current_loan_balance, offset_amount])
            monthly_interest = 0
        # offset contribution needs to happen before interest calculation on that day
        if c_date in offset_contribution_dates:
            # Assuming offset contribution reduces the loan balance directly for interest calculation purposes
            offset_amount += offset_contribution_regular_amount
            transactions.append([c_date, 'Offset Contribution', offset_contribution_regular_amount, current_loan_balance, offset_amount])
        if c_date in repayment_dates:
            current_loan_balance -= minimum_repayments
            transactions.append([c_date, 'Repayment', minimum_repayments, current_loan_balance, offset_amount])
        if c_date in extra_repayments_dates:
            extra_repayment = min(extra_repayments_regular_amount, current_loan_balance)  # to ensure we don't pay more than the remaining loan balance
            current_loan_balance -= extra_repayment
            transactions.append([c_date, 'Extra Repayment', extra_repayment, current_loan_balance, offset_amount])
        
        if current_loan_balance <= 0.01:  # small threshold to account for floating point precision
            current_loan_balance = 0
            break

    # save results to a dataframe
    df = pd.DataFrame(transactions, 
                      columns=['Date', 'Transaction Type', 
                               'Transaction Amount', 'Loan Balance', 'Offset Balance'])
    return df


def create_amortization_schedule(start_date: str, 
                                loan_amount: float, 
                                annual_rate: float, 
                                loan_duration_years: int, 
                                loan_duration_months: int,
                                repayment_frequency: str, 
                                initial_offset_amount: float, 
                                offset_contribution_frequency: str, 
                                regular_amount_offset_contribution: float,
                                extra_repayments_frequency: str,
                                extra_repayments_regular_amount: float,
                                capture_interest_accrual: bool = False
                                 ):
    """ Generates loan transactions by passing required input to the daily routine.
    Args:
        start_date (str): the settlement date, or start date of the loan. Must be a string in YYYY-MM-DD format. Internally converted to datetime object.
        loan_amount (float): the loan amount, or principle amount. Also knowns as FUM.
        annual_rate (float): interest rate expressed as percentage without the sign e.g., 5.4
        loan_duration_years (int): duration of the loan in years e.g., 30
        loan_duration_months (int): duration of the loan in months after "loan_duration_years". For example, if a loan is 26 years and 5 months, then loan_duration_years=26 and loan_duration_months=5.
        repayment_frequency (str): frequency denoting how often repayment is made. Valid values are "weekly", "fortnightly" and "monthly".
        initial_offset_amount (float): initial contribution to the offset account when loan is set up.
        offset_contribution_frequency (str): frequency denoting how often the customer puts money to the offset account. Valid values are "weekly", "fortnightly" and "monthly".
        regular_amount_offset_contribution (float): regular contribution amount to the offset account. This is the amount contributed every "offset_contribution_frequency".
        capture_interest_accrual (bool): Whether to capture daily and monthly interest accruals in the transactions. Default is False.
    """
    # Convert start_date string to datetime object
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = calculate_end_date(start_date, loan_duration_years, loan_duration_months)
    minimum_repayments = calculate_minimum_repayment(principal=loan_amount, 
                                                     annual_rate=annual_rate, 
                                                     years=loan_duration_years, 
                                                     months=loan_duration_months, 
                                                     repayment_frequency=repayment_frequency)


    repayment_dates = find_relevant_dates(start_date, end_date, repayment_frequency)
    repayment_dates.pop(0)  # remove the first date as repayment starts after settlement date
    offset_contribution_dates = find_relevant_dates(start_date, end_date, offset_contribution_frequency)
    offset_contribution_dates.pop(0)  # remove the first date as offset contribution starts after settlement date
    interest_charge_dates = find_relevant_dates(start_date, end_date, 'monthly') # interest is calculated daily but charged monthly on the same day of the month as settlement date
    interest_charge_dates.pop(0)  # remove the first date as interest starts accruing after settlement date
    extra_repayments_dates = find_relevant_dates(start_date, end_date, extra_repayments_frequency)
    extra_repayments_dates.pop(0)  # remove the first date as extra repayments starts after settlement date
    # generate all dates between start and end date for daily interest calculation  
    all_dates = find_relevant_dates(start_date, end_date, 'daily') # daily dates for iterating through the schedule
    all_dates.pop(0)  # remove the first date as interest starts accruing after settlement date
   

    loan_transactions = generate_loan_transactions(start_date, loan_amount, annual_rate,
                                                   initial_offset_amount, minimum_repayments,
                                                   all_dates, interest_charge_dates, repayment_dates, 
                                                   offset_contribution_dates, 
                                                   regular_amount_offset_contribution,
                                                   extra_repayments_dates, 
                                                   extra_repayments_regular_amount,
                                                   capture_interest_accrual)
    
    return loan_transactions


def create_monthly_summary(transactions: pd.DataFrame):
    """ Creates a monthly summary of repayments made, interest charged, outstanding loan amount and offset account balance.
    """
    df = transactions.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year-Month'] = df['Date'].dt.to_period('M')
    # Group by 'Date' and calculate the required columns
    result = df.groupby('Year-Month').agg(
        TOTAL_REPAYMENT=('Transaction Amount', lambda x: x[df.loc[x.index, 'Transaction Type'] == 'Repayment'].sum()),
        TOTAL_INTEREST=('Transaction Amount', lambda x: x[df.loc[x.index, 'Transaction Type'] == 'Interest Charged'].sum()),
        LOAN_BALANCE_FIRSTDAY=('Loan Balance', 'first'),
        OFFSET_BALANCE_LASTDAY=('Offset Balance', 'last')
    ).reset_index()
    # Fill NaN values with 0 for TOTAL_REPAYMENT and TOTAL_INTEREST
    result['TOTAL_REPAYMENT'] = result['TOTAL_REPAYMENT'].fillna(0)
    result['TOTAL_INTEREST'] = result['TOTAL_INTEREST'].fillna(0)
    result['LOAN_BALANCE_FIRSTDAY'] = result['LOAN_BALANCE_FIRSTDAY'].fillna(0)
    result['OFFSET_BALANCE_LASTDAY'] = result['OFFSET_BALANCE_LASTDAY'].fillna(0)

    # compute summary metrices
    total_interest_paid = result['TOTAL_INTEREST'].sum()
    total_payments_made = result['TOTAL_REPAYMENT'].sum()


    result.columns = ['MONTH', 'Total Repayment', 'Total Interest Charged', 
                      'Loan Balance (First Day of Month)', 
                      'Offset Balance (Last Day of Month)']
    
    return result, total_interest_paid, total_payments_made


def prepare_loan_summary(loan_params : dict, store_results : bool = False):
    """ Create a loan summary from loan details.
    This function takes a dictionary with following keys (all mandatory):
        start_date (string) : the settlement date, or start date of the loan. Must be a string in YYYY-MM-DD format.
        loan_amount (float) : the loan amount, or principle amount. Also knowns as FUM.
        annual_rate (float): interest rate expressed as percentage without the sign e.g., 5.4
        loan_duration_years (integer) : duration of the loan in years e.g., 30
        loan_duration_months (integer) : duration of the loan in months after "loan_duration_years". For example, if a loan is 26 years and 5 months, then loan_duration_years=26 and loan_duration_months=5.
        repayment_frequency (string); frequency denoting how often repayment is made. Valid values are "weekly", "fortnightly" and "monthly".
        initial_offset_amount (float) : initial contribution to the offset account when loan is set up.
        offset_contribution_frequency (string): fvnt6requency denoting how often the customer puts money to the offset account. Valid values are "weekly", "fortnightly" and "monthly".
        offset_contribution_regular_amount (float): regular contribution amount to the offset account. This is the amount contributed every "offset_contribution_frequency".
        extra_repayments_frequency (string): frequency denoting how often extra repayments are made. Valid values are "weekly", "fortnightly" and "monthly".
        extra_repayments_regular_amount (float): regular extra repayment amount. This is the amount contributed every "extra_repayments_frequency".
        capture_interest_accrual (bool): Whether to capture daily and monthly interest accruals in the transactions. Default is False.
    Args:

    Returns a dictionary containing the following keys:
        all_transactions: pandas dataframe containing all transactions on the loan account.
        monthly_summary: pandas dataframe containing monthly summary of repayments, interest charged, loan account balance and offset balance
        total_interest_charged: total interest charged by the bank over the life of the loan, in dollars.
        total_repayments: total repayment made by the customers over the life of the loan, in dollars.
    """
    # validate inputs
    inputval_prepare_loan_summary(**loan_params)

    # extract loan parameters
    start_date = loan_params.get('start_date')
    loan_amount = loan_params.get('loan_amount')
    annual_rate = loan_params.get('annual_rate')
    loan_duration_years = loan_params.get('loan_duration_years')
    loan_duration_months = loan_params.get('loan_duration_months')
    repayment_frequency = loan_params.get('repayment_frequency')
    initial_offset_amount = loan_params.get('initial_offset_amount')
    offset_contribution_frequency = loan_params.get('offset_contribution_frequency')
    offset_contribution_regular_amount = loan_params.get('offset_contribution_regular_amount')
    extra_repayments_frequency = loan_params.get('extra_repayments_frequency')
    extra_repayments_regular_amount = loan_params.get('extra_repayments_regular_amount')
    capture_interest_accrual = loan_params.get('capture_interest_accrual', False)
    
    # generate all loan transactions
    all_transactions = create_amortization_schedule(start_date, loan_amount, 
                                                    annual_rate, loan_duration_years, loan_duration_months,
                                                    repayment_frequency, initial_offset_amount, 
                                                    offset_contribution_frequency, offset_contribution_regular_amount,
                                                    extra_repayments_frequency, extra_repayments_regular_amount,
                                                    capture_interest_accrual)
    if store_results:
        all_transactions.to_csv('loan_transactions.csv', index=False)

    # generate monthly summary table
    monthly_summary, total_interest_charged, total_repayments = create_monthly_summary(all_transactions)
    # Save the result to a new CSV file
    if store_results:
        monthly_summary.to_csv("loan_schedule_summary.csv", index=False)

    # return results
    results = {'all_transactions' : all_transactions,
               'monthly_summary': monthly_summary,
               'total_interest_charged' : total_interest_charged,
               'total_repayments' : total_repayments
               }
    return results
