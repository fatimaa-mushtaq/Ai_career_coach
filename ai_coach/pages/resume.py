import streamlit as st
import openai
import pdfkit
import base64
import os
from resume_template import render_resume_html

openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = os.getenv("GROQ_API_BASE")

pdf_config = pdfkit.configuration(wkhtmltopdf=os.getenv("WKHTMLTOPDF_PATH"))

def run():
    st.title("📄 Stylish Resume Builder")

    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email")
    cnic = st.text_input("🆔 CNIC Number")
    address = st.text_input("🏠 Address")
    degree = st.text_input("🎓 Degree")
    skills = st.text_area("🧠 Skills (comma-separated)")
    interests = st.text_area("💡 Interests (comma-separated)")
    goal = st.text_input("🎯 Career Goal (optional)")
    image = st.file_uploader("🖼️ Upload Your Profile Picture", type=["png", "jpg", "jpeg"])

    if st.button("🎨 Build Resume"):
        if not all([name, email, cnic, address, degree, skills, interests, image]):
            st.warning("Please fill all fields and upload an image.")
        else:
            with st.spinner("Generating resume..."):
                try:
                    image_bytes = image.read()
                    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
                    image_url = f"data:image/png;base64,{image_base64}"

                    html = render_resume_html(name, email, cnic, address, degree, skills, interests, goal, image_url)
                    
                    st.markdown("### 💎 Preview")
                    st.components.v1.html(html, height=900, scrolling=True)

                    pdf_file = f"{name.replace(' ', '_')}_Resume.pdf"
                    pdfkit.from_string(html, pdf_file, configuration=pdf_config)

                    with open(pdf_file, "rb") as f:
                        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
                        download_link = f'<a href="data:application/pdf;base64,{base64_pdf}" download="{pdf_file}">📥 Download Stylish Resume</a>'
                        st.markdown(download_link, unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error: {e}")
