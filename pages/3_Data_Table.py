import pandas as pd
import streamlit as st

dorseys = pd.read_csv('dorsey_knob_holes_csv.csv')

st.write(dorseys)