import streamlit as st
import g4f
import matplotlib.pyplot as plt
import numpy as np

g4f.debug.logging = True
g4f.check_version = False

# Set the page title
st.title("Code Analysis and Chatbot Dashboard")

# Create a text area at the top for user input
user_input = st.text_area("Enter your code", "", max_chars=15000)

# Create a tab bar for selecting the active tab
selected_tab = st.radio("Select a tab:", ["Report Generator", "Chatbot"])

if selected_tab == "Report Generator":
    # Code for the Report Generator tab
    st.subheader("Report Generator")
    
    # Check if the user has entered text
    def generate_code_analysis_report(user_input):
        if user_input:
            # Compose the query for g4f
            query = f"{user_input}\n\n"
            query += '''give a report for the above in this format:

Title(Give a suitable title for the code):
Executive Summary:

Briefly summarize the purpose and main findings of the code analysis.
Introduction:

Provide context for the analysis, including the code's purpose and background information.
Code Overview:

Describe the codebase being analyzed, including its size, technology stack, and any relevant libraries or frameworks used.
Analysis Methodology:

Explain the approach and tools used for code analysis.
Code Structure:

Provide an overview of the code's structure and organization.
Identify key modules, functions, or classes and their roles.
 Key Findings:

Present the main findings of the analysis, such as code quality, performance, security, and maintainability issues.
Highlight any critical issues that require immediate attention.
 Code Quality:

Assess the code quality based on coding standards and best practices.
Identify areas where code quality can be improved.
Performance Analysis:

Evaluate the code's performance, including bottlenecks, latency, and resource usage.
Suggest performance optimizations if applicable.
 Security Analysis:

Examine the code for potential security vulnerabilities.
Highlight any security risks and suggest mitigation strategies.
 Maintainability and Documentation:

Evaluate the code's maintainability, readability, and documentation.
Recommend improvements for easier maintenance and understanding.
Testing and Test Coverage:

Review the code's testing strategy and code coverage.
Suggest improvements for comprehensive testing.
Recommendations:

Summarize the key recommendations for improving the code.
Prioritize recommendations based on criticality.
Conclusion:

Summarize the overall assessment of the code.

I want all the headings in bold , the headings are 
Title
Executive Summary
Introduction
Code Overview
Analysis Methodology
Code Structure
Key Findings
Code Quality
Performance Analysis
Security Analysis
Testing and Test Coverage
Recommendations
Conclusion
'''

            
            # Make the API call to g4f
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}],
            )
    
            # Extract and format the generated report
            generated_report = response
    
            return generated_report
    
    # Create a space to display the code analysis report
    report_space = st.empty()
    
    # Generate and display the code analysis report
    if st.button("Generate Code Analysis Report"):
        generated_report = generate_code_analysis_report(user_input)
        report_space.subheader("Generated Code Analysis Report:")
        report_space.write(generated_report)
    
elif selected_tab == "Chatbot":
    # Code for the Chatbot tab
    st.subheader("Chatbot")
    
    # Create a text input for user queries in the Chatbot tab
    user_query = st.text_input("Enter your query")
    
    def generate_response(user_query, user_input):
        if user_input:
            user_query += f"Assume you know everything about this code \n\n{user_input}\n\n and you are a Code Expert(Human) ,answer the below question"
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_query}],
            )
            return response
    
    # Create a space to display the response from the chatbot
    response_space = st.empty()
    
    if st.button("Ask Chatbot"):
        chatbot_response = generate_response(user_query, user_input)
        response_space.subheader("Response From Chatbot:")
        response_space.write(chatbot_response)
