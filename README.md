# Apple Stock Price Forecasting Model
# Business Objective:
Predict the apple stock market price for the next 30 days.
There are Open, High, Low and Close prices that have been given for each day starting from 2012 to 2019 for Apple stock.

Date: stock price date
Open: Opening price of the day
High: Maximum price of the day
Low : Minimum price of the day
Close : Closing price of the day  ---> Target variable
Adj Close : Adjusted closing of the day
Volume: total share cost from all the shareholders

# Tools Used
- Python: Pandas, NumPy, Scikit-learn for data preprocessing and feature engineering
- TensorFlow/Keras: For developing and training the Long Short-Term Memory (LSTM) model
# Solution 
- Collected and cleaned historical stock price data, addressing missing values and normalizing features for model optimization.
- Designed an LSTM model architecture to effectively capture temporal dependencies in the stock price data.
- Split the dataset into training, validation, and test sets for robust evaluation of the model's performance.
- Applied hyperparameter tuning to optimize model accuracy and addressed overfitting through regularization techniques and validation strategies.
# Conclusion
The LSTM model achieved a low RMSE of 10, demonstrating high accuracy in predicting stock price movements. The project provided valuable insights into time-series forecasting and highlighted the potential of machine learning models for financial market analysis and decision-making.
# Deployment using streamlit:
https://applestockpriceforecast-uhciuywtcehznq5mgmbowr.streamlit.app/
