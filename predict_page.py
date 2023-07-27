import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('salary_pred.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["pred_model"]
le_country = data["le_country"]
le_education = data["le_education"]




def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")


    
    countries = ("United States of America",                                   
    "Germany",                                                  
    "United Kingdom of Great Britain and Northern Ireland",   
    "India",                                                   
    "Canada",                                                   
    "France",                                                   
    "Netherlands",                                              
    "Australia",                                             
    "Spain",                                                   
    "Brazil" ,                                                  
    "Sweden",                                                   
    "Italy",                                                    
    "Poland",                                                   
    "Switzerland",                                              
    "Israel",                                                    
    "Denmark",                                                   
    "Russian Federation",                                        
    "Austria",                                                   
    "Norway",                                                  
    "Belgium",                                                   
    "Ukraine",                                                   
    "Portugal",                                                  
    "Turkey",                                                    
    "Finland",                                                   
    "Czech Republic",                                            
    "New Zealand",                                               
    "Romania")      

    education = ("Bachelor's degree", 'Less than Bachelors', "Master's degree",
        "Post Grad")


    country = st.selectbox("Country",countries)
    edu = st.selectbox("Education",education)
    experience = st.slider("Years of Experience ",0,50,3)

    sal = st.button("Predict Salary")

    if sal:
        z = np.array([[country, edu, experience ]])
        z[:, 0] = le_country.transform(z[:,0])
        z[:, 1] = le_education.transform(z[:,1])
        z = z.astype(float)

        salary = regressor.predict(z)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")