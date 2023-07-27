import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    
    if x == "Less than 1 year":
        return 0.5
    if x == "More than 50 years":
        return 50
    
    return x

def clean_education(x):
    
    if "Bachelor's degree" in x:  
        return "Bachelor's degree"
    if "Master's degree" in x:
        return "Master's degree"
    if "Professional degree" in x:
        return "Post Grad"
    return "Less than Bachelors"

@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)     
    country_map = shorten_categories(df.Country.value_counts(), 1500)
    df['Country'] = df['Country'].map(country_map)   
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["YearsCodePro"] = df["YearsCodePro"].apply(pd.to_numeric)

    return df


df = load_data()


def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write("""### Stack Overflow Developer Survey 2023""")


    data = df["Country"].value_counts()
    fig1,ax1 = plt.subplots()
    ax1.pie(data,labels=data.index,startangle=90)
    ax1.axis("equal")

    st.write("""#### Data from different countries""")
    st.pyplot(fig1)


    st.write("""### Mean Salary Value""")

    data = df.groupby(["Country"])["Salary"].mean().sort_values()
    st.bar_chart(data)

    st.write("""### Mean Salary Based on Experience """)

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending = True)
    st.line_chart(data)
