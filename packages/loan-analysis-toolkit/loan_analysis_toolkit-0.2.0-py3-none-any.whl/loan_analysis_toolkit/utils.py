from pydantic import BaseModel

class inputval_prepare_loan_summary(BaseModel):
    start_date: str
    loan_amount: float
    annual_rate: float
    loan_duration_years: int
    loan_duration_months: int
    repayment_frequency: str
    initial_offset_amount: float
    offset_contribution_frequency: str
    offset_contribution_regular_amount: float
    extra_repayments_frequency: str
    extra_repayments_regular_amount: float
    capture_interest_accrual: bool
