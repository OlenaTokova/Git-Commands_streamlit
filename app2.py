import streamlit as st

import streamlit as st

def get_bot_response(user_input):
    responses = {
        "what is git": "Git is a distributed version control system for tracking changes in source code during software development.",
        "how to clone a repo": "You can clone a repository by using the command: `git clone [url]`.",
        "how to commit changes": "To commit changes, use: `git commit -m '[your message]'`.",
        # Add more predefined responses here
    }
    # Return the response if the question is recognized, else a default message
    return responses.get(user_input.lower(), "I'm not sure how to answer that. Can you ask something else?")

st.title('Git Commands Guide')

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ['Home', 'Git Basics', 'Git Branching', 'Additional Resources', 'AI Chatbot'])

if page == 'Home':
    st.header("Home")
    st.write("Welcome to the Git Commands Guide. Navigate through the sidebar.")
    st.markdown("""
        **Introduction to Git and GitHub Course**
        - What is Git and why should you use it?
        - Difference between Git and GitHub
        - Why Git is a distributed system
        - Installing Git
        - Setting up the author's name and email
        - Overview of basic commands in the Terminal
        - Differences between the Terminal and the Shell
        - How to initialize a Git repository
        - Initializing the Git repository in our project
        - Git Areas: Working directory, Index (staging area), Repository
        - Git saves different versions of the same file
        
        **Git Workflow**
        - File tracking statuses
        - Types of objects in Git
        - Object hashes and SHA1 hash function
        - What is a commit and what does it contain?
        - How commits are related to each other
        - What is HEAD, What is a branch
        - Example repository - first commit, second commit, moving between versions
        
        **Basic Git Commands**
        - Creating files and folders in a project
        - Creating the first commit
        - Analyzing internal Git objects
        - Creating a second commit
        - Moving between versions
        
        **Branches in Git**
        - Switching between branches
        - Commands for working with branches
        - Merging branches
        - Command to merge branches
        - Step-by-step process for merging branches
        
        **Working with GitHub**
        - Git repository hosting services
        - Cloning remote repositories
        - What is origin
        - Commands for interacting with a remote repository
        
        **Practical Exercises**
        - Practice for cloning a remote repository
        - Practice linking a local repository with a remote one
        - Creating an authorization token on GitHub
        - Creating a commit on GitHub
        - View all commits on GitHub
        - Downloading updates from GitHub
        
        **Summary**
        """, unsafe_allow_html=True)

elif page == 'Git Basics':
    st.header("Git Basics")
    st.markdown("""
    Here are some of the basic Git commands:

    - **git init**: Initializes a new Git repository.
    - **git clone [url]**: Clones a repository into a new directory.
    - **git add [file]**: Adds a file to the staging area.
    - **git commit -m "[message]"**: Commits the staged snapshot.
    - **git status**: Lists all new or modified files to be committed.
    - **git config**: Lets you configure your Git installation (or an individual repository) from the command line.
    """)
elif page == 'Git Branching':
    st.header("Git Branching")
    st.markdown("""
    Branching is a feature available in Git which lets you diverge from the main line of development and continue to do work without messing with that main line. Here are some commands related to branching:

    - **git branch**: Lists all the local branches in the current repository.
    - **git branch [name]**: Creates a new branch.
    - **git checkout [name]**: Switches to the specified branch.
    - **git merge [branch]**: Merges the specified branch’s history into the current branch.
    """)
elif page == 'Additional Resources':
    st.header("Additional Resources")
    st.image('./image.png', caption='Git Workflow Diagram')
    st.markdown("[Git Official Documentation](https://git-scm.com/doc)")
elif page == 'AI Chatbot':
    st.header("AI Chatbot")
    user_input = st.text_input("Ask the AI about Git")
    if user_input:
        response = get_bot_response(user_input)
        st.write(response)
