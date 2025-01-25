# from pydantic import BaseModel


# class Bankrupty(BaseModel):
#     ROA(C) before interest and depreciation before interest : float
#     ROA(A) before interest and % after tax : float
#     ROA(B) before interest and depreciation after tax : float
#     Operating Gross Margin : float
#     Realized Sales Gross Margin : float
#     Operating Profit Rate : float
#     Pre-tax net Interest Rate : float
#     After-tax net Interest Rate : float
#     Non-industry income and expenditure/revenue : float
#     Continuous interest rate (after tax) : float

from pydantic import BaseModel, Field

class Bankrupty(BaseModel):
    roa_c_before_interest_and_depreciation_before_interest: float = Field(..., alias="ROA(C) before interest and depreciation before interest")
    roa_a_before_interest_and_percent_after_tax: float = Field(..., alias="ROA(A) before interest and % after tax")
    roa_b_before_interest_and_depreciation_after_tax: float = Field(..., alias="ROA(B) before interest and depreciation after tax")
    operating_gross_margin: float = Field(..., alias="Operating Gross Margin")
    realized_sales_gross_margin: float = Field(..., alias="Realized Sales Gross Margin")
    operating_profit_rate: float = Field(..., alias="Operating Profit Rate")
    pre_tax_net_interest_rate: float = Field(..., alias="Pre-tax net Interest Rate")
    after_tax_net_interest_rate: float = Field(..., alias="After-tax net Interest Rate")
    non_industry_income_and_expenditure_revenue: float = Field(..., alias="Non-industry income and expenditure/revenue")
    continuous_interest_rate_after_tax: float = Field(..., alias="Continuous interest rate (after tax)")

