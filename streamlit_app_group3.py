import streamlit as st
st.title('SpeedyBytes 🚚')
st.image('speedybytes_icon2.jpg',width=600)
tab1,tab2,tab3,tab4,tab5 = st.tabs(["tab1", "One year revenue forecast", "Optimal Shift Timing Recommendation",'tab4','tab5'])
with tab1: #ayrton
    st.header('omg tab1 works yay')


with tab2: #minh
    print('gelo')

with tab3: #javier
    st.header('Optimal Shift Timing Recommendation')
    st.subheader('Want to find out the optimal working hours for your truck?')
    st.subheader('1. Specify your truck details')
    st.subheader('2. Specify the number of hours your truck is working for')

    no_of_hours = st.text_input("Enter the number of hours (1-23): ")
    if no_of_hours.isnumeric():
        hours = int(user_input)
        if 1 <= hours <= 23:
            st.success(f"Your input of {hours} hours has been saved!")
        else:
            st.warning("Please enter a number between 1 and 23.")
    elif no_of_hours.strip() != "":
        st.warning("Please enter a valid numeric value.")
  

    st.subheader('3. Specify the date your truck is working on')
    st.subheader('4. Optimal shift timing will be recommended to you based on the forecasted total average revenue across all locations')
    



with tab4: #vibu
    print('vibu')

with tab5: #nathan
    print('nathan')
    
