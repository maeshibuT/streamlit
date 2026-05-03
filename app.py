import streamlit as st
import pandas as pd
st.write("Hello world!")
st.write("Hello :blue[world]")
st.title("Hello world! :sunglasses:")
st.write("This is a simple Streamlit app that demonstrates how to use Streamlit to create interactive web applications. You can use Streamlit to create data visualizations, display dataframes, and much more!")

df= pd.DataFrame(
        {"fc": [1,2,3],
        "sc": [10,20,30]}
    )
csv = df.to_csv(index=False) #downloadするには、dfをcsv形式に変換する必要がある。

st.link_button("Go to Streamlit", "https://streamlit.io")
st.download_button(label="DownLoad CSV", data=csv, file_name="data.csv",mime="text/csv")

st.button("Click me!")

st.header("Hello world",divider="rainbow")

#コードをpython形式で表示する。
code = """print("hello world")"""
st.code(code, language="python")

#チェックボックス
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write(":red[Thank you for agreeing to the terms and conditions!]")

options= st.multiselect("Select your favorite colors", ["Red","Green","Blue"])
st.write("You selected:", options)

options= st.radio("Select color",["Red","Green","Yellow"])
st.write("You selected:", options)

#interactiveなDataDrame
df = pd.DataFrame(
    [
        {"colors": "red","rating": 5},
        {"colors": "green","rating":4},
        {"colors": "blue","rating":3}
    ]
)

edited_df = st.data_editor(df)
edited_df["rating"]=edited_df["rating"].astype(int)
st.write("Index of the row with the highest rating:",edited_df.loc[edited_df["rating"].idxmax()]["colors"])


#interactiveなDataDrame22
df = pd.DataFrame(
    [
        {"colors": "red","rating": 5,"mark":True},
        {"colors": "green","rating":4,"mark":False},
        {"colors": "blue","rating":3,"mark":True}
    ]
)

st.write("markがTrueの行だけを抽出して、ratingの最大値を持つ行のcolorsを表示する。")
edited_df = st.data_editor(df)
edited_df=edited_df[edited_df["mark"]==True]
st.write("Index of the row with the highest rating:",edited_df.loc[edited_df["rating"].idxmax()]["colors"])

csv = edited_df.to_csv(index=True).encode("utf-8") #downloadするには、dfをcsv形式に変換する必要がある。
st.download_button(label="DownLoad CSV", data=csv, file_name="sample_data.csv",mime="text/csv")
#mimeは拡張子
#trueだけDLされる。

#progress bar
df = pd.DataFrame(
    {
        "sales": [20,55,100,80],
        "progress_sales":[20,55,100,80],
    }
)

st.data_editor(
    df,
    column_config={
        "progress_sales": st.column_config.ProgressColumn(
            min_value=0,
            max_value=100,
        ),
    },
)

#時系列バー表示
df = pd.DataFrame(
    {
        "sales": [
            [0,4,20,49,80,100],
            [1,5,10,8,20,70]
        ]
    }
)

st.data_editor(df)

#bar chart
st.data_editor(
    df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            y_min=0,
            y_max=100,
        ),
    },
)

#line chart
st.data_editor(
    df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            y_min=0,
            y_max=100,
        ),
    },
)

#slider
age = st.slider("how old are you?", 0,120,40)

st.write("You are", age, "years old.")

#choose date
import datetime
date=st.date_input("Choose a birth date", datetime.date(2000,1,1))
st.write("Your birth date is", date)

#textbox
text = st.text_input("Enter your name", "John Smith")
st.write("Your name is", text)

#separate columns
col1, col2 = st.columns(2) #colunsの数を指定
with col1:
    st.title("Column1")
    st.write("This is column 1")

with col2:
    st.title("Column2")
    st.write("This is column 2")

#add tabs
tab1, tab2 = st.tabs(["Tab 1", "Tabs 2"]) #tabをそれぞれ指定する
with tab1:
    st.title("Tab1")
    st.write("This is tab 1")
with tab2:
    st.title("Tab2")
    st.write("This is tab 2")

with st.expander("see more details(アコーディオンもしくはExpanderと呼ばれる機能)"):
    st.write("This is an expander. You can put any content you want here, and it will be hidden until the user clicks on the expander.")

#サイドバー
with st.sidebar:
    st.title("Sidebar")
    st.write("This is the sidebar.")

#notification
agree = st.checkbox("Agree to show notification")
if agree:
    st.toast("Thank you", icon="👍")


st.success("This is a success message!")

#effects
birthday = st.checkbox("Is it your birthday today?")

if birthday:
    st.balloons()
    st.toast("happy birthday", icon="🎉")

#複数ページ実装
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/page1.py", label="Page1")
st.page_link("pages/page2.py", label="Page2")

 