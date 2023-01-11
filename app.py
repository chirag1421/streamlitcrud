import streamlit as st
import pandas as pd
from PIL import Image
from data import create_table,add_data,view_data,view_StudentID,get_StudentID,edit,delete
import streamlit.components.v1 as stc


HTML_BANNER = """<div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Student LMS</h1>
    </div>"""

def main():
    stc.html(HTML_BANNER)
    menu = ['Create','Read', 'Update', 'Delete']
    choice = st.sidebar.selectbox("Menu",menu)
    create_table()
    if choice=='Create':
        st.subheader('Add Items')

        col1,col2,col3,col4 = st.columns(4)

        with col1:
            StudentID = st.text_input("STUDENTID")

        with col2:
            firstname = st.text_input("FIRSTNAME")
        with col3:
            lastname = st.text_input("LASTNAME")
        with col4:
            city = st.selectbox("CITY",["Ahmedabad","Surat","Rajkot","Vadodra","Bhuj"])

        if st.button("Submit"):
            if(StudentID==""):
                st.warning("Enter the StudentID first")
            elif(len(get_StudentID(StudentID))):
                st.error("StudentId Exists")
            else:
                add_data(StudentID,firstname,lastname,city)
                st.success("Submit::{}".format(StudentID))

    elif choice == 'Read':
            data = sorted(view_data())

            sf = pd.DataFrame(data, columns=["StudentID","firstname", "lastname","city"])
            with st.expander("View All"):
                st.dataframe(sf)
            with st.expander("StudentID"):
                StudentID = sf["StudentID"].value_counts().to_frame()
                StudentID = StudentID.reset_index()
                st.dataframe(StudentID)

    elif choice == 'Update':
            st.subheader("Edit/Update Items")
            data = sorted(view_data())
            sf = pd.DataFrame(data, columns=["StudentID","firstname", "lastname","city"])
            with st.expander("Current data"):
                st.dataframe(sf)

            list_of_StudentIDS = [i[0] for i in view_StudentID()]
            selected_StudentID = st.selectbox("Student", list_of_StudentIDS)
            StudentID_result = get_StudentID(selected_StudentID)

            if StudentID_result:
                StudentID = StudentID_result[0][0]

                StudentID_firstname = StudentID_result[0][1]
                StudentID_lastname = StudentID_result[0][2]
                StudentID_city = StudentID_result[0][3]
                StudentID_list = ["Ahmedabad","Surat","Rajkot","Vadodra","Bhuj"]
                StudentID_index = StudentID_list.index(StudentID_city)

                col1, col2,col3,col4 = st.columns(4)


                with col1:
                    new_firstname = st.text_input("firstname")
                with col2:
                    new_lastname = st.text_input("lastname")
                with col3:
                    new_city = st.selectbox("city", StudentID_list, index=StudentID_index)

                if st.button("Update Student"):
                    if (StudentID == ''):
                        st.error('Enter the StudentID first')
                    elif (len(get_StudentID(
                            StudentID))  and StudentID_firstname == new_firstname and StudentID_lastname == new_lastname and StudentID_city == new_city):
                        st.error('Student already exists')
                    else:
                        edit(new_firstname, new_lastname,new_city, StudentID_firstname, StudentID_lastname, StudentID_city)
                        st.success("Updated StudentID :: {}".format(StudentID))

                        with st.expander("View Updated Data"):
                            result = view_data()
                            clean_df = pd.DataFrame(result, columns=["StudentID","firstname", "lastname","city"])
                            st.dataframe(clean_df)

    elif choice == 'Delete':
            st.subheader("Delete Items")
            data = view_data()
            sf = pd.DataFrame(data, columns=["StudentID", "firstname", "lastname","city"])
            with st.expander("Current data"):
                st.dataframe(sf)

            list_of_StudentID = [i[0] for i in view_StudentID()]
            selected_StudentID = st.selectbox("Select Student Data", list_of_StudentID)
            if st.button("Delete"):
                delete(selected_StudentID)
                st.success("Deleted StudentID: '{}'".format(selected_StudentID))

                with st.expander("Updated Data"):
                    result = view_data()
                    clean_df = pd.DataFrame(result, columns=["StudentID","firstname","lastname","city"])
                    st.dataframe(clean_df)

if __name__ == '__main__':
    main()