# Credit to 

import pandas as pd
import joblib
from fastapi import FastAPI, Request, Depends,Form

app = FastAPI()


@app.get('/credit')
async def predict(request: Request, 
                  Annual_Income:float=Form(...),
                  Monthly_Inhand_Salary:float=Form(...),
                  Num_Bank_Accounts:int=Form(...),
                  Num_Credit_Card:int=Form(...),
                  Interest_Rate:int=Form(...),
                  Num_of_Loan:float=Form(...),
                  Delay_from_due_date:int=Form(...),
                  Num_of_Delayed_Payment:float=Form(...),
                  Credit_Mix:int=Form(...),
                  Outstanding_Debt:float=Form(...),
                  Credit_History_Year:int=Form(...),
                  Monthly_Balance:float=Form(...)
                  ):
   

    df = {
    "Annual_Income": [Annual_Income],
    "Monthly_Inhand_Salary": [Monthly_Inhand_Salary],
    "Num_Bank_Accounts": [Num_Bank_Accounts],
    "Num_Credit_Card": [Num_Credit_Card],
    "Interest_Rate": [Interest_Rate],
    "Num_of_Loan": [Num_of_Loan],
    "Delay_from_due_date": [Delay_from_due_date],
    "Num_of_Delayed_Payment": [Num_of_Delayed_Payment],
    "Credit_Mix": [Credit_Mix],
    "Outstanding_Debt": [Outstanding_Debt],
    "Credit_History_Year": [Credit_History_Year],
    "Monthly_Balance": [Monthly_Balance]
}   

    df = pd.DataFrame(df)
    model = joblib.load("./model/clf.joblib")
    credit_Score = int(model.predict(df)[0])
    return credit_Score
