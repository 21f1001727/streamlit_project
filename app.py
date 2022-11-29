import streamlit as st
import pandas as pd

def main():
	st.title("Multiplication of 2 Given Numbers")
	# choice=st.sidebar.selectbox("Menu",['Home','About'])
	# if choice=="Home":
		# st.subheader("Home Page")

	col1,col2=st.columns([1,2])

	with col1:
		with st.form(key='myform'):
			input1=st.text_input("Enter Number1")
			input2=st.text_input("Enter Number2")
			submit_button=st.form_submit_button(label="Submit")
		if submit_button:
			with col2:
				
				num1=int(input1)
				num2=int(input2)
				res=num1*num2
				st.write(f"Multiplication Result: {num1}x{num2}={res}")	

if __name__=='__main__':
	main()
