import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

pipe = pickle.load(open('Score_Predictor.pkl','rb'))

teams = ['New Zealand',
 'India',
 'Sri Lanka',
 'Australia',
 'England',
 'West Indies',
 'South Africa',
 'Pakistan',
 'Bangladesh',
 'Afghanistan']

cities = ['Shere Bangla National Stadium',
 'Rangiri Dambulla International Stadium',
 'R Premadasa Stadium',
 'Sydney Cricket Ground',
 'County Ground',
 'Kennington Oval',
 'Melbourne Cricket Ground',
 'Sheikh Zayed Stadium',
 "Lord's",
 'SuperSport Park',
 'Adelaide Oval',
 'Pallekele International Cricket Stadium',
 'Edgbaston',
 'Dubai International Cricket Stadium',
 'Sharjah Cricket Stadium',
 'Eden Park',
 'Brisbane Cricket Ground, Woolloongabba',
 'Western Australia Cricket Association Ground',
 'The Rose Bowl',
 'Kingsmead',
 'Trent Bridge',
 'Sophia Gardens',
 'Seddon Park',
 'Old Trafford',
 'Newlands',
 "St George's Park",
 'New Wanderers Stadium',
 'Headingley',
 'Senwes Park',
 'Westpac Stadium',
 'Sir Vivian Richards Stadium, North Sound',
 'National Stadium',
 'Providence Stadium',
 'McLean Park',
 "Queen's Park Oval, Port of Spain",
 'Brabourne Stadium',
 'Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa',
 'Bay Oval',
 'Kensington Oval, Bridgetown',
 'Bellerive Oval',
 'Riverside Ground',
 'Gaddafi Stadium',
 'Sabina Park, Kingston',
 'Warner Park, Basseterre',
 'Hagley Oval',
 'Punjab Cricket Association Stadium, Mohali',
 'Grace Road',
 'Kinrara Academy Oval',
 'Beausejour Stadium, Gros Islet',
 'Wankhede Stadium',
 'Sinhalese Sports Club Ground',
 'MA Chidambaram Stadium, Chepauk',
 'Shere Bangla National Stadium, Mirpur',
 'National Stadium, Karachi',
 'University Oval']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select Venue',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets left')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'venue':city, 'cur_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))


