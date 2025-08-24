import streamlit as st
import pandas as pd
import numpy as np
input = ""
output = st.write(f"{input}")

st.write("# Hello")

row = 5
col = 4

arr = np.random.randint(10, 100, size=(102,100))

st.scatter_chart(arr)

print(dir(st))
matrix = [
    ["1", "2", "3", "Div"],
    ["4", "5", "6", "Mul"],
    ["7", "8", "9", "Sub"],
    ["0", "^", "%", "Add"],
    ["(", ")", "Clear", "Enter"]
]

st.write(pd.DataFrame(matrix))

# for i in range(row):
#     icolumn = st.columns(col)
#     for j in range(col):
#         with icolumn[j]:
#             if st.button(str(matrix[i][j])):
#                 input += str(matrix[i][j])
