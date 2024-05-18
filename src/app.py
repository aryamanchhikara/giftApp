import streamlit as st
import pandas as pd
import numpy as np

st.title("This is a Prototype for a gift app")

giftInput = st.text_input("What is the item ", "")
st.write("The entered item is", giftInput)

