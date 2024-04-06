TODO: 
Streamlit App made from this "Git Commands" article.  
Add in 1 or two more diagrams, and docs references.
Then an build in an AI chatbot to assist with specific problems, if and when they arise. 

Git Really Good Workflows
https://www.one-tab.com/page/YMvfvsmlQyq_9hm-XJtAWA


Git Commands - Learning git commands in an easy way, Start with git commands on terminal 
and make your daily development work in faster way, Useful Git Commands which will helpful in 
your daily development work.

Git for Beginners: A Simple Guide | by Anderson Servat | Medium
Dev Concepts: Git Workflow. How to properly approach Git Workflow | by Gregory Anderson | Medium
git commit workflow - Google Search
git commit workflow - Google Search
git commit workflow - Google Search
git commit workflow - Google Search


START_Project

Creating a Streamlit app that encompasses the Git commands from 
the specified article, includes additional diagrams and documentation references,
and integrates an AI chatbot for assistance involves several steps. 

        1. Environment Setup - DONE 
pip install streamlit

# Streamlit, version 1.33.0

        2. Streamlit App Structure
The app will have several components:

        1. A homepage with a summary of Git commands.
Introduction to Git and GitHub Course
What is Git and why should you use it?
  Difference between Git and GitHub
  Why Git is a distributed system
  Installing Git
  Setting up the author's name and email
  Overview of basic commands in the Terminal
  Differences between the Terminal and the Shell
  How to initialize a Git repository
  Initializing the Git repository in our project
  Git Areas
  Working directory
  Index (staging area)
  Repository
  Git saves different versions of the same file
Git Workflow
  File tracking statuses
  Types of objects in Git
  Object hashes and SHA1 hash function
  What is a commit and what does it contain?
  How commits are related to each other
  What is HEAD
  What is a branch
  Example repository - first commit
  Example repository - second commit
Example repository - moving between versions
  Basic Git Commands
  Creating files and folders in a project
  Creating the first commit
  Analyzing internal Git objects
  Creating a second commit
  Moving between versions
  Branches in Git
  Switching between branches
  Commands for working with branches
  Merging branches
  Command to merge branches
  Step-by-step process for merging branches
  Starting practice merging branches
  Installing the Visual Studio Code editor
  Creating the first commit in the feature branch
  Creating a commit in the code editor
  Switching between branches after changes
  Creating a commit in the main branch
  Merging the feature branch into main
  Analysis of the repository after merging branches
  Deleting the feature branch
  Git repository hosting services
  Cloning remote repositories
  What is origin
  Commands for interacting with a remote repository
  Connection between a local repository and a remote one
  Practice for cloning a remote repository
  Practice linking a local repository with a remote one
  Creating an authorization token on GitHub
  Creating a commit on GitHub
  View all commits on GitHub
  Downloading updates from GitHub
  Summary

        2. Sections for each Git workflow, as detailed in the article.
        3. Additional diagrams and documentation references.
        4. An AI chatbot interface.

        3. Basic Streamlit App - DONE
Create a Python script (app.py) for your Streamlit app. 
Start by importing Streamlit and setting up the basic structure.

        4. Adding Content
Fill in the sections for Git Basics, Git Branching, etc., 
by summarizing the information from the provided article and 
any additional resources you find useful. Use st.write, st.markdown, or st.code
 to display text, markdown, or code snippets, respectively.

        5. Adding Diagrams
For additional diagrams, you can use tools like draw.io to create them and 
save them as images. Then, use st.image to display these images in your app.

        6. Adding Documentation References
Link to additional documentation using st.markdown with the link syntax.

        7. Integrating an AI Chatbot
Integrating an AI chatbot into a Streamlit app can be complex and requires an AI model. 
For simplicity, you can simulate a chatbot by using predefined answers or integrate with
 third-party services like OpenAI's GPT-3, considering you have access and abide by OpenAI's use case policy.

For a basic implementation, you can use an input box for questions and a placeholder to display answers.

For a more advanced chatbot, you'll need to integrate an actual NLP model or API. This requires additional setup, including obtaining API keys and using appropriate libraries to interact with the service.

        8. Running Your App

To run your app, navigate to the folder containing app.py and run the following command in your terminal:
streamlit run app.py

