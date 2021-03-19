# this is a learning attempt at streamlit from the following Youtube link
#  https://www.youtube.com/watch?v=nNwVAc6OdN4&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=2

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pylab as plt
import time
#st.write(st.__version__)   # streamlit version 0.78.0
print(st.__version__)
st.title("The Running Professor")

st.header("this is the first STREAMLIT attempt")
st.subheader("an A.I company")
st.text("presented by ANAND KHANDEKAR")

st.markdown(""" # Header created using MARKDOWN """)
# emojis can be displayed using STREAMLIT as shownn below
st.markdown(""":sunglasses:""")

st.text("here is an example of LATEX formula as well in STREAMLIT")
st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
      \sum_{k=0}^{n-1}  a r^k =
       a \left(\frac{1-r^{n}}{1-r}\right)''')

# st.write(st)  # this will display basic information about STREAMLIT

 # we can pass dictionary to st.write
d = {  "name": "Anand",
       "Language": "Python",
        "topics":"Learning Basic Streamlit commands"}
st.write(d)

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
d = {
       "name": ["Anand","Khandekar"],
       "age": ["49", "94"],
       "company":["TRP", "my own"]
    }
st.write('passing the LIST below as a table :-- notice there are NO scroll bars')
st.table(a)

st.write(" now here below is a dictionary passed to table function")
st.table(d)

# we can ven display a JSON file using streamline
# note that dictionary is a  VALID example of JSON file
st.json(d)

# we use th CACHE decorrator inbuilt in Streamlit
# we will experriment with time library

@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))

# part 4 of the youtube series by HArsh Gupta
# we will add PLOTS and media such as video and sound files

data = pd .DataFrame(
    np.random.randn(100,3),
    columns = ['a','b','c']
)

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)
