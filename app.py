import streamlit as st
import pickle

model=pickle.load(open('mymodel.pkl','rb'))

st.title('Iris Classification using Decision Tree')
sl=st.number_input('sepal length')
sw=st.number_input('sepal width')
pl=st.number_input('petal length')
pw=st.number_input('petal width')

def prediction(sl,sw,pl,pw):
    value=model.predict([[sl,sw,pl,pw]])
    if value[0]==0:
        return 'Iris-setosa'
    elif value[0]==1:
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'
    
if st.button('predict'):
    output=prediction(sl,sw,pl,pw)
    st.write(f'This flower is {output}')    