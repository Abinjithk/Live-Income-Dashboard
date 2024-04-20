import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

st.set_page_config(
    page_title= "Income Dashboard"
)
st.title("Live Income Data Monitoring App")

df = pd.read_csv('income.csv')

# filters
job_filter = st.selectbox('Choose a Job',df['occupation'].unique(),index=2)

placeholer = st.empty()

df = df[df["occupation"] == job_filter]
# st.write(df)

while True:
    df['new_age'] = df['age'] * np.random.choice(range(1,5))
    df['whpw_new'] = df['hours-per-week'] * np.random.choice(range(1,5))

    # creating KPI's
    avg_age = np.mean(df['new_age'])
    count_married = int(df[df['marital-status'] == 'Married-civ-spouse']['marital-status'].count()+np.random.choice(range(1,30)))
    hpw = np.mean(df['whpw_new'])

    with placeholer.container():
        # create 3 colums
        kpi1,kpi2,kpi3 = st.columns(3)
        # filling columns with required values
        kpi1.metric(label='Age',value=round(avg_age),delta = round(avg_age)-10)
        kpi2.metric(label='Married Count', value=int(round(count_married)), delta=count_married + 10)
        kpi3.metric(label='Working hours per week', value=round(hpw), delta=round(count_married/hpw)/8)

        # create two columns for chart
        figcol1,figcol2 = st.columns(2)
        with figcol1:
            st.markdown(""" ### Age vs Marital status """)
            fig = px.density_heatmap(data_frame=df,y='new_age',x='marital-status')
            fig.update_layout(height=400, width=500)
            st.plotly_chart(fig)

        with figcol2:
            st.markdown(""" ### Age Count """)
            fig2 = px.histogram(data_frame=df,x='new_age')
            fig2.update_layout(height=300, width=400)
            st.plotly_chart(fig2)

        st.markdown(""" ### Data view as per selection""")
        st.dataframe(df)
        time.sleep(1)
