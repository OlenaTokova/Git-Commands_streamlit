import streamlit as st

st.title('Git Commands Guide')

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ['Home', 'Git Basics', 'Git Branching', 'Additional Resources', 'AI Chatbot'])

if page == 'Home':
    st.header("Home")
    st.write("Welcome to the Git Commands Guide. Navigate through the sidebar.")
elif page == 'Git Basics':
    st.header("Git Basics")
    # Add content and commands here
elif page == 'Git Branching':
    st.header("Git Branching")
    # Add content and commands here
elif page == 'Additional Resources':
    st.header("Additional Resources")
    # Add diagrams and documentation links here
elif page == 'AI Chatbot':
    st.header("AI Chatbot")
    # Chatbot interface will be added here

## For additional diagrams, you can use tools like draw.io to create them and save them as images. 
# Then, use st.image to display these images in your app.

st.image('path_to_your_image.png', caption='Git Workflow Diagram')

# Link to additional documentation using st.markdown with the link syntax.
st.markdown("[Git Official Documentation](https://git-scm.com/doc)")

user_input = st.text_input("Ask the AI about Git")
if user_input:
    # This is where you would process the input and generate a response
    st.write("Response from AI: ...")




