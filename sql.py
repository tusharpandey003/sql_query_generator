import google.generativeai as genai
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


# configure genai key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load google gemini model


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt, question])
    return response.text


# function to retrieve query from database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# define your prompt
prompt = (
    """
    you are an expert  in converting english questions to SQL query!
    The SQL database has the name STUDENT  and following columns -NAME ,CLASS,SECTION\n\n
    for example ,\nexample 1- how many entries of records are present ?,the SQL command could be something like SELECT COUNT(*) FROM STUDENT;
    \nexample 2- TELL me all the students studied in Data science class?,the SQL command could be something like SELECT * FROM STUDENT WHERE CLASS="Data Science";
    also the SQL code should not have ''' in begining or end and sql words in output

"""
)

# streamlit App

st.set_page_config(page_title="Retrive any SQL query")
st.header('GEMINI APP TO RETRIVE SQL DATA')
question = st.text_input("Input:", key='input')

submit = st.button('Ask the Query')
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    st.subheader("Query:")
    st.write(
        {response}
    )
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is :")
    for row in response:
        print(row)
        st.header(row)
