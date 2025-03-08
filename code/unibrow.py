import pandas as pd
import streamlit as st
import pandaslib as pl
import numpy as np

st.title("UniBrow")
st.caption("The Universal data browser")

dataset = st.file_uploader("Please upload file: ")


if dataset:
    file_name = dataset.name
    file_type = pl.get_file_extension(file_name)
    new_df = pl.load_file(dataset, file_type)
    col_list = pl.get_column_names(new_df)

    selected_columns = st.multiselect("Select columns:", options= col_list)
    set = st.toggle("Toggle filtering:")

    if set:
        filter_cols = pl.get_columns_of_type(new_df, "object")
        filter_select = st.selectbox("Select column: ", options = filter_cols)
        
        unique_list = pl.get_unique_values(new_df, filter_select)
        unique_select = st.selectbox("Select unique values:", options = unique_list)

        filtered_df = new_df[new_df[filter_select] == unique_select][selected_columns]
        st.dataframe(filtered_df)
        st.text(filtered_df.describe(include = np.number))
    else:
        st.dataframe(new_df[selected_columns])
        st.text(new_df[selected_columns].describe(include = np.number))

