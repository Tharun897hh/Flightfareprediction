import numpy as np
import pickle
import streamlit as st
import pandas as pd
import bz2

#setting up the page title,icons


st.text('Fill in your detalis to predict your filght price')
st.image(r'C:\Users\tk896\OneDrive\Desktop\Temp\myproject\image1.png')
ch=st.selectbox('Airline',('Select','Vistara','Air India','Indigo','GO FIRST','AirAsia','SpiceJet'))
if(ch=='Vistara'):
    a=5
elif(ch=='Air India'):
    a=1
elif(ch=='Indigo'):
    a=3
elif(ch=='GO FIRST'):
    a=2
elif(ch=='AirAsia'):
    a=0
elif(ch=='SpiceJet'):
    a=4
cg=st.selectbox('From',('Select','Delhi','Mumbai','Bangalore','Kolkata','Hyderabad','Chennai'))
if(cg=='Delhi'):
    b=2
    cx=st.selectbox('Destination',('Select','Mumbai','Bangalore','Kolkata','Hyderabad','Chennai'))
    if(cx=='Mumbai'):
            f=5
    elif(cx=='Bangalore'):
            f=0
    elif(cx=='Kolkata'):
            f=4
    elif(cx=='Hyderabad'):
            f=3
    elif(cx=='Chennai'):
            f=1
elif(cg=='Mumbai'):
    b=5
    cx=st.selectbox('Destination',('Select','Delhi','Bangalore','Kolkata','Hyderabad','Chennai'))
    if(cx=='Delhi'):
        f=2
    elif(cx=='Bangalore'):
        f=0
    elif(cx=='Kolkata'):
        f=4
    elif(cx=='Hyderabad'):
        f=3
    elif(cx=='Chennai'):
        f=1
elif(cg=='Bangalore'):
    b=0
    cx=st.selectbox('Destination',('Select','Mumbai','Delhi','Kolkata','Hyderabad','Chennai'))
    if(cx=='Mumbai'):
        f=5
    elif(cx=='Delhi'):
        f=2
    elif(cx=='Kolkata'):
        f=4
    elif(cx=='Hyderabad'):
        f=3
    elif(cx=='Chennai'):
        f=1
elif(cg=='Kolkata'):
    b=4
    cx=st.selectbox('Destination',('Select','Mumbai','Delhi','Bangalore','Hyderabad','Chennai'))
    if(cx=='Mumbai'):
        f=5
    elif(cx=='Delhi'):
        f=2
    elif(cx=='Bangalore'):
        f=0
    elif(cx=='Hyderabad'):
        f=3
    elif(cx=='Chennai'):
        f=1
elif(cg=='Hyderabad'):
    b=3
    cx=st.selectbox('Destination',('Select','Mumbai','Delhi','Bangalore','Kolkata','Chennai'))
    if(cx=='Mumbai'):
        f=5
    elif(cx=='Delhi'):
        f=2
    elif(cx=='Bangalore'):
        f=0
    elif(cx=='Kolkata'):
        f=4
    elif(cx=='Chennai'):
        f=1
else:
    b=1
    cx=st.selectbox('Destination',('Select','Mumbai','Delhi','Bangalore','Kolkata','Hyderabad'))
    if(cx=='Mumbai'):
        f=5
    elif(cx=='Delhi'):
        f=2
    elif(cx=='Bangalore'):
        f=0
    elif(cx=='Kolkata'):
        f=4
    elif(cx=='Hyderabad'):
        f=3                        
cf=st.selectbox('Departure time',('Select','Morning','Early Morning','Evening','Night','Afternoon','Late Night'))
if(cf=='Morning'):
    c=4
elif(cf=='Early Morning'):
    c=1
elif(cf=='Evening'):
    c=2
elif(cf=='Night'):
    c=5
elif(cf=='Afternoon'):
    c=0
elif(cf=='Late Night'):
    c=3
ci=st.selectbox('Stops',('Select','one','zero','two or more'))
if(ci=='one'):
    d=0
elif(ci=='zero'):
    d=2
elif(ci=='two or more'):
    d=1
cs=st.selectbox('Arrival time',('Select','Night','Evening','Morning','Afternoon','Early Morning','Late Night'))
if(cs=='Night'):
    e=5
elif(cs=='Evening'):
    e=2
elif(cs=='Morning'):
    e=4
elif(cs=='Afternoon'):
    e=0
elif(cs=='Early Morning'):
    e=1
elif(cs=='Late Night'):
    e=3    
cb=st.selectbox('Class',('Select','Economy','Business'))
if(cb=='Economy'):
    g=1
else:
    g=0        
h=st.number_input('Duration(hrs)')
i=st.number_input('Days left')
btn=st.button('Check')
