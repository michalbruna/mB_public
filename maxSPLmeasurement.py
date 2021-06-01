import streamlit as st
import numpy as np

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modelTraining = st.beta_container()

with header:
    st.title(f"Maximum SPL you can measure using your gear.\n")
    st.write("Please input following data:")

micSens = st.number_input('Microphone sensitivity [mV/Pa] :', min_value=1, max_value=200, value=15, step=1)
micSens = micSens
maxU = st.number_input('Maximum input voltage of the preamp [dBu] :', min_value=-20, max_value=26, value=10, step=1)

maxSPL = 154 + 20*np.log10((np.sqrt(0.001*600) * 10**(maxU/20)) / micSens)

st.text("And let's see the results now:")
st.markdown(f'When using a measurement microphone with sensitivity of **{micSens} mV/Pa** plugged into'
            f' a preamp with maximum input voltage of **{maxU} dBu** you can measure peak values up to \n\n'
            f'**{maxSPL:.1f} dB SPL**')
