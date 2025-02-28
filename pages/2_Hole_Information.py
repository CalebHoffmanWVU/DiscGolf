import streamlit as st
import pandas as pd

dorseys = pd.read_csv('dorsey_knob_holes_csv.csv')

all_bask = ["Basket 1", "Basket 2", "Basket 3", "Basket 4", "Basket 5", "Basket 6", "Basket 7", "Basket 8", "Basket 9", "Basket 10", "Basket 11", "Basket 12", "Basket 13", "Basket 14", "Basket 15", "Basket 16", "Basket 17", "Basket 18"]
all_tee = ["Tee 1", "Tee 2", "Tee 3", "Tee 4", "Tee 5", "Tee 6", "Tee 7", "Tee 8", "Tee 9", "Tee 10", "Tee 11", "Tee 12", "Tee 13", "Tee 14", "Tee 15", "Tee 16", "Tee 17", "Tee 18"]
all_hole = ["Hole 1", "Hole 2", "Hole 3", "Hole 4", "Hole 5", "Hole 6", "Hole 7", "Hole 8", "Hole 9", "Hole 10", "Hole 11", "Hole 12", "Hole 13", "Hole 14", "Hole 15", "Hole 16", "Hole 17", "Hole 18"]
whites = ["Hole 1", "Hole 2", "Hole 5", "Hole 13", "Hole 14", "Hole 16"]
tees = ["B", "Y"]
baskets = ["B", "Y"]
bask_white = ["B", "Y", "W"]
basket_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
basket_number_whites = [1, 2, 5, 13, 14, 16]

hole = st.selectbox('Select a hole', basket_number)

if hole in basket_number_whites:
    tee = st.selectbox("Select a tee", tees)
    basket = st.selectbox("Select a basket", bask_white)
    hole_df = dorseys[[f"Tee {hole}", f"Basket {hole}", f"Hole {hole}"]]
    hole_df = hole_df[hole_df[f"Tee {hole}"] == tee]
    hole_df = hole_df[hole_df[f"Basket {hole}"] == basket]

    hole_df[f"Hole {hole}"] = pd.to_numeric(hole_df[f"Hole {hole}"], errors="coerce")
    times = len(hole_df)
    count_ace = (hole_df[f"Hole {hole}"] == 1).sum()
    count_bird = (hole_df[f"Hole {hole}"] == 2).sum()
    count_par = (hole_df[f"Hole {hole}"] == 3).sum()
    count_bogey = (hole_df[f"Hole {hole}"] == 4).sum()
    count_worse = (hole_df[f"Hole {hole}"] >= 5).sum()
    average = hole_df[f"Hole {hole}"].mean()
    average = round(average, 2)

    st.write("You have played this hole", times, "times")
    st.write("You have aced this hole", count_ace, "times")
    st.write("You have birdied this hole", count_bird, "times")
    st.write("You have parred this hole", count_par, "times")
    st.write("You have bogeyed this hole", count_bogey, "times")
    st.write("You have double bogeyed or worse this hole", count_worse, "times")
    st.write("Your average on this hole is", average)
else:
    tee = st.selectbox("Select a tee", tees)
    basket = st.selectbox("Select a basket", baskets)
    hole_df = dorseys[[f"Tee {hole}", f"Basket {hole}", f"Hole {hole}"]]
    hole_df = hole_df[hole_df[f"Tee {hole}"] == tee]
    hole_df = hole_df[hole_df[f"Basket {hole}"] == basket]

    hole_df[f"Hole {hole}"] = pd.to_numeric(hole_df[f"Hole {hole}"], errors="coerce")
    times = len(hole_df)
    count_ace = (hole_df[f"Hole {hole}"] == 1).sum()
    count_bird = (hole_df[f"Hole {hole}"] == 2).sum()
    count_par = (hole_df[f"Hole {hole}"] == 3).sum()
    count_bogey = (hole_df[f"Hole {hole}"] == 4).sum()
    count_worse = (hole_df[f"Hole {hole}"] >= 5).sum()
    average = hole_df[f"Hole {hole}"].mean()
    average = round(average, 2)

    st.write("You have played this hole", times, "times")
    st.write("You have aced this hole", count_ace, "times")
    st.write("You have birdied this hole", count_bird, "times")
    st.write("You have parred this hole", count_par, "times")
    st.write("You have bogeyed this hole", count_bogey, "times")
    st.write("You have double bogeyed or worse this hole", count_worse, "times")
    st.write("Your average on this hole is", average)

