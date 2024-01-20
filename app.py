import streamlit as st
import time
from prophet.serialize import model_from_json
import plotly.graph_objs as go

st.title('WEATHER FORECASTING')
with st.sidebar:
    st.write('Here you can write about Your project ')


fin = open('serialized_model.json', 'r')
model = model_from_json(fin.read())  # Load model
days = st.number_input('Number of days',value=10)
new_df= model.make_future_dataframe(periods=days)
result = model.predict(new_df)
data = result[['ds','trend','yhat','yhat_lower','yhat_upper']]
data.columns=['date','trend','final_outcome(predicted)','final_outcome_lower_limit','final_outcome_upper_limit']

sub = st.button(label='Submit')
if sub:
    with st.spinner():
        time.sleep(1)
    st.dataframe(data[10592:])

fin.close()


