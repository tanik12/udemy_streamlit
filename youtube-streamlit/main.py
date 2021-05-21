import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interaction {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_column = st.beta_columns(2)
buttun = left_column.button('右カラムに文字を表示')
if buttun:
    right_column.write('ここは右カラム')

'Done!!!!!'

expander = st.beta_expander('問合せ1')
expander.write('問合せ1内容を書く')
expander2 = st.beta_expander('問合せ2')
expander2.write('問合せ2内容を書く')
expander3 = st.beta_expander('問合せ3')
expander3.write('問合せ3内容を書く')