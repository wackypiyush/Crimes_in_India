import streamlit as st
import pandas as pd
import preprocessor,helper

df=pd.read_csv('india-crime.csv')
df=preprocessor.preprocess(df)

st.sidebar.header("Indian Crime Analysis")
user_menu=st.sidebar.radio(
    'Select an option',
    ('See whole Data','State/UT wise','Year wise','District wise','Total Percentage Division')
)

if user_menu=='See whole Data':
    st.dataframe(df)

elif user_menu=='State/UT wise':
    st.sidebar.header('State/UT Wise List')
    cases=helper.case_list()
    states=helper.state_list(df)
    selected_case=st.sidebar.selectbox("Select Case",cases)
    selected_state=st.sidebar.selectbox("Select State/UT",states)
    if selected_case=='Overall' and selected_state!='Overall':
        state_wise,chart,pie=helper.fetch_state_list(df,selected_case,selected_state)
        st.dataframe(state_wise)
        st.pyplot(chart)
        st.pyplot(pie)
    else:
        state_wise,chart=helper.fetch_state_list(df,selected_case,selected_state)
        st.dataframe(state_wise)
        st.pyplot(chart)

elif user_menu=="Year wise":
    st.sidebar.header("Year Wise Analysis")
    years=helper.year_list(df)
    selected_yr=st.sidebar.selectbox("Select Year",years)
    year_wise,chart=helper.fetch_year_wise(df,selected_yr)
    st.dataframe(year_wise)
    st.pyplot(chart)

elif user_menu=="District wise":
    st.sidebar.header("District wise Analysis")
    state=helper.state_list(df)
    selected_state=st.sidebar.selectbox("Select State/UT",state)
    district=helper.state_district(df,selected_state)
    selected_district=st.sidebar.selectbox("Select District",district)
    if selected_state=="Overall":
        pass
    else:
        district_wise,chart=helper.fetch_districts(df,selected_state,selected_district)
        st.dataframe(district_wise)
        #chart.update_layout(authorise=False,width=1000,height=600)
        st.pyplot(chart)


elif user_menu=='Total Percentage Division':
    st.sidebar.header("Total Percentage of cases")
    chart=helper.fetch_total(df)
    st.pyplot(chart)