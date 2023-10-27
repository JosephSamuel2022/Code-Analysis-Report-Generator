import streamlit as st
import g4f
import json

g4f.debug.logging = True
g4f.check_version = False

# Set the page title
st.title("Code Analysis Report Generator")

# Create a text area for user input
user_input = st.text_area("Enter your code", "", max_chars=15000)

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
Code Quality:
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

# Generate and display the code analysis report
if st.button("Generate Code Analysis Report"):
    report = generate_code_analysis_report(user_input)
    st.subheader("Generated Code Analysis Report:")
    st.write(report)
