import streamlit as st

st.title("Password Analyser")

password=st.text_input("Enter the password",type="password")

#st.button("Validate")

if st.button("Validate"):
    upper=lower=digit=special=False

    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digit=True
        else:
            special=True

    if len(password)>=8 and upper and lower and special and digit:
        st.success("Strong Password..Thank You!")
    else:
        st.error("Invalid Password!")
        if len(password)<8:
            st.write("Atleast 8 chara is needed")
        if upper==False:
            st.write("Atleast 1 uppercase is needed")
        if lower==False:
            st.write("Atleast 1 lowerercase is needed")
        if digit==False:
            st.write("Atleast 1 digit is needed")
        if special==False:
            st.write("Atleast 1 specialchara is needed")

#not digit,not upper can be used




















































































