## First, we will create a new Python script and import Streamlit.
* Create a new Python file named ( say ) ```first_app.py ``` , then open it with your IDE or text editor.
* Next, import Streamlit
```
import streamlit as st
# to make things easier later, we will also import numpy and pandas
import numpy as nnp
import pandas as pd
```
* Run our app. A new tab will open in your default browser. It will be blank for now.
```streamlit run first_app.py ```
* you can kill the app anytime by tying **Ctrl+c** in the terminal.

## Add text and data
### add a title

There are many ways to add test to the app. one of them is as follows
``` st.title(" My First App )```
Your app now has a title. You can usse specific text functions to add content \n
to your app, or use ```st.write()``` and add your own markdown.


## Write a data frame
Along with magic commands, ```st.write()``` is Streamlit's " Swiss Army knife". You can pass almost anything to ```st.write()```: text, data , Matplotlib figures,
Altair charts. Streamlit wil internally figure it out and redenr things in the right way.
```
st.srite(" Here we use data to create a table")
t.write(pd.DataFrame({
'first column ': [1,2,3],
'second column': [1000, 2123, 8678]
}))
```
