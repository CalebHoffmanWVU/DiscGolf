import streamlit as st
import pandas as pd
import datetime
import pybaseball
import matplotlib.pyplot as plt

dorseys = pd.read_csv('dorsey_knob_holes_csv.csv')

odd_bask = ["Basket 1", "Basket 3", "Basket 5", "Basket 7", "Basket 9", "Basket 11", "Basket 13", "Basket 15", "Basket 17"]
odd_tee = ["Tee 1", "Tee 3", "Tee 5", "Tee 7", "Tee 9", "Tee 11", "Tee 13", "Tee 15", "Tee 17"]
odd_hole = ["Hole 1", "Hole 3", "Hole 5", "Hole 7", "Hole 9", "Hole 11", "Hole 13", "Hole 15", "Hole 17"]

even_bask = ["Basket 2", "Basket 4", "Basket 6", "Basket 8", "Basket 10", "Basket 12", "Basket 14", "Basket 16", "Basket 18"]
even_tee = ["Tee 2", "Tee 4", "Tee 6", "Tee 8", "Tee 10", "Tee 12", "Tee 14", "Tee 16", "Tee 18"]
even_hole = ["Hole 2", "Hole 4", "Hole 6", "Hole 8", "Hole 10", "Hole 12", "Hole 14", "Hole 16", "Hole 18"]

front_bask = ["Basket 1", "Basket 2", "Basket 3", "Basket 4", "Basket 5", "Basket 6", "Basket 7", "Basket 8", "Basket 9"]
front_tee = ["Tee 1", "Tee 2", "Tee 3", "Tee 4", "Tee 5", "Tee 6", "Tee 7", "Tee 8", "Tee 9"]
front_hole = ["Hole 1", "Hole 2", "Hole 3", "Hole 4", "Hole 5", "Hole 6", "Hole 7", "Hole 8", "Hole 9"]

back_bask = ["Basket 10", "Basket 11", "Basket 12", "Basket 13", "Basket 14", "Basket 15", "Basket 16", "Basket 17", "Basket 18"]
back_tee = ["Tee 10", "Tee 11", "Tee 12", "Tee 13", "Tee 14", "Tee 15", "Tee 16", "Tee 17", "Tee 18"]
back_hole = ["Hole 10", "Hole 11", "Hole 12", "Hole 13", "Hole 14", "Hole 15", "Hole 16", "Hole 17", "Hole 18"]

all_bask = ["Basket 1", "Basket 2", "Basket 3", "Basket 4", "Basket 5", "Basket 6", "Basket 7", "Basket 8", "Basket 9", "Basket 10", "Basket 11", "Basket 12", "Basket 13", "Basket 14", "Basket 15", "Basket 16", "Basket 17", "Basket 18"]
all_tee = ["Tee 1", "Tee 2", "Tee 3", "Tee 4", "Tee 5", "Tee 6", "Tee 7", "Tee 8", "Tee 9", "Tee 10", "Tee 11", "Tee 12", "Tee 13", "Tee 14", "Tee 15", "Tee 16", "Tee 17", "Tee 18"]
all_hole = ["Hole 1", "Hole 2", "Hole 3", "Hole 4", "Hole 5", "Hole 6", "Hole 7", "Hole 8", "Hole 9", "Hole 10", "Hole 11", "Hole 12", "Hole 13", "Hole 14", "Hole 15", "Hole 16", "Hole 17", "Hole 18"]

tees = ["Blue", "Yellow"]
pins = ["Blue", "Yellow", "Blue/White", "Yellow/White"]

prompt_1 = ["Full Layout", "Odds and Evens", "Front 9 and Back 9"]
style = st.selectbox('Select a style of Layout', prompt_1)

if style == "Full Layout":
    select_tee = st.selectbox('Select your tees', tees)
    select_pin = st.selectbox('Select your baskets', pins)
else:
    st.markdown("""
    I haven't put anything here yet.
    """)

