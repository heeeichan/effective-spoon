import streamlit as st
import time

st.title("streamlit 入門")

st.write("プログレスバーの表示")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f"Iteration {i + 1}")
  bar.progress(i + 1)
  time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
  right_column.write("ここは右カラム")

expander = st.expander("お問い合わせ1")
expander.write("お問い合わせの回答1")
expander = st.expander("お問い合わせ2")
expander.write("お問い合わせの回答2")
expander = st.expander("お問い合わせ3")
expander.write("お問い合わせの回答3")