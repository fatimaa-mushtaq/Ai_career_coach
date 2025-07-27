# prompts.py

def generate_career_prompt(name, degree, skills, interests, personality, goal):
    return f"""
Hi, my name is {name}. I have a degree in {degree}.
My key skills are: {skills}.
My interests include: {interests}.
My personality type is: {personality}.
My goal is: {goal if goal else 'I am not sure yet'}.

Please suggest:
1. 3-5 ideal career paths
2. Short explanation for each
3. Online courses to learn
4. Motivational advice
"""

def generate_styled_resume_html(name, email, cnic, address, degree, skills, interests, goal):
    return f"""
Create a modern, colorful, professional HTML resume based on:
Name: {name}
Email: {email}
CNIC: {cnic}
Address: {address}
Degree: {degree}
Skills: {skills}
Interests: {interests}
Goal: {goal or 'Not specified'}

Design instructions:
- Gradient header
- Elegant fonts (e.g., Poppins/Open Sans)
- Colorful section blocks with shadows
- Tag-style skill highlights
- Stylish resume sections with icons
Return HTML inside <div> only. No <html>, <head>, or <body>
"""

def generate_interview_prompt(role, experience, skills, company, concern):
    return f"""
You are an AI Interview Coach. I am preparing for an interview.

Job Role: {role}
Experience: {experience}
Skills: {skills}
Company: {company}
Concern: {concern or 'None'}

Please help me by:
1. Generating 5 relevant technical and behavioral questions
2. Providing ideal sample answers
3. Giving tips to improve my confidence
4. Suggestions to research about the company
"""



