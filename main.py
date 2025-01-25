from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Bankrupty

app=FastAPI(
    title="Bankrupty",
    description="predicting bankrupty protability"
)


with open("/home/ravivarma/Downloads/preplaced/PROJECTS/Bankrupty/model.pkl","rb") as file:
    model=pickle.load(file)
    
@app.get("/")
def index():
    return "welcome to bankrupty prediciton fastapi"


@app.post("/predict")
def model_predict(bankrupty:Bankrupty):
    sample = pd.DataFrame({
    " ROA(C) before interest and depreciation before interest": [bankrupty.roa_c_before_interest_and_depreciation_before_interest],
    " ROA(A) before interest and % after tax": [bankrupty.roa_a_before_interest_and_percent_after_tax],
    " ROA(B) before interest and depreciation after tax": [bankrupty.roa_b_before_interest_and_depreciation_after_tax],
    " Operating Gross Margin": [bankrupty.operating_gross_margin],
    " Realized Sales Gross Margin": [bankrupty.realized_sales_gross_margin],
    " Operating Profit Rate": [bankrupty.operating_profit_rate],
    " Pre-tax net Interest Rate": [bankrupty.pre_tax_net_interest_rate],
    " After-tax net Interest Rate": [bankrupty.after_tax_net_interest_rate],
    " Non-industry income and expenditure/revenue": [bankrupty.non_industry_income_and_expenditure_revenue],
    " Continuous interest rate (after tax)": [bankrupty.continuous_interest_rate_after_tax]
})
    



    predicted_value=model.predict(sample)


    if predicted_value==1:
        return "bankrupyt"

    else:
        return "no bankrupty"