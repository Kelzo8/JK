import streamlit as st
import random
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(page_title='Kelzo Coding Portfolio', page_icon='assets/logo.png', layout='wide')

# Styling for the new branding theme
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('assets/style.css')

# Hero Section with Background Image and Logo
st.markdown("""
    <div style="
        background: url('assets/logo.png') no-repeat center center;
        height: 400px;
        background-size: contain;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 3em;
        font-family: 'Roboto', sans-serif;
        font-weight: bold;
        text-shadow: 2px 2px 8px #000;
        position: relative;
        background-color: #0a1f44;
    ">
        Full Stack Developer Specializing in AI and Web Apps
    </div>
""", unsafe_allow_html=True)

# Navigation Tabs with Updated Branding Colors
selected_page = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Contact Me", "Get Motivated!"],
    icons=["house", "folder", "envelope", "lightbulb"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0a1f44"},
        "icon": {"color": "#00a8e8", "font-size": "25px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "color": "white",
            "padding": "10px 20px",
        },
        "nav-link-selected": {"background-color": "#007ea7"},
    },
)

# Home Page
if selected_page == "Home":
    st.title("Welcome to Kelzo Coding Portfolio")
    st.write("""
        Hi! I'm [Your Name], a software developer passionate about building
        beautiful web applications and cool AI-driven solutions. This website showcases
        some of the work I've done. Feel free to explore and get to know me better!
    """)
    st.subheader("Download my CV")
    st.download_button("Download Resume", data=open('assets/cv.pdf', 'rb').read(), file_name='cv.pdf')

# Projects Page
elif selected_page == "Projects":
    st.title("Projects")
    st.write("Filter projects by technology:")
    filter_options = ["All", "React", "Python", "AI"]
    selected_filter = st.selectbox("Select Technology", filter_options)

    projects = [
        {"name": "Project 1", "image": "project1.png", "github_link": "https://github.com/your-github-profile/project1", "tags": ["Python", "AI"]},
        {"name": "Project 2", "image": "project2.png", "github_link": "https://github.com/your-github-profile/project2", "tags": ["React"]}
    ]
    
    # Filtering projects based on selection
    filtered_projects = [p for p in projects if selected_filter == "All" or selected_filter in p['tags']]
    
    for project in filtered_projects:
        st.markdown("""
            <div style="
                border: 1px solid #007ea7;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                transition: transform 0.3s;
                background-color: #112240;
            ">
                <div onmouseover="this.style.transform='scale(1.05)';" onmouseout="this.style.transform='scale(1)';">
                    <h3 style="color: #00a8e8;">{name}</h3>
                    <img src="assets/project_images/{image}" style="width: 100%; border-radius: 10px; margin-bottom: 10px;">
                    <p>Tech Stack: {tags}</p>
                    <a href="{github_link}" style="color: #4fd1c5; text-decoration: none; font-weight: bold;">View on GitHub</a>
                </div>
            </div>
        """.format(name=project['name'], image=project['image'], tags=', '.join(project['tags']), github_link=project['github_link']), unsafe_allow_html=True)

# Contact Page
elif selected_page == "Contact Me":
    st.title("Contact Me")
    st.markdown("[LinkedIn](https://linkedin.com/in/your-profile)")
    st.markdown("[GitHub](https://github.com/your-github-profile)")

    st.subheader("Send me an Email")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send Email"):
        if name and email and message:
            st.success("Your email has been sent!")
        else:
            st.error("Please fill in all fields before sending the email.")

# Motivational Quote Generator Page
elif selected_page == "Get Motivated!":
    st.title("Get Motivated!")
    quotes = [
        {"text": "Believe you can and you're halfway there.", "image": "https://via.placeholder.com/600x200"},
        {"text": "It does not matter how slowly you go as long as you do not stop.", "image": "https://via.placeholder.com/600x200"},
        {"text": "Act as if what you do makes a difference. It does.", "image": "https://via.placeholder.com/600x200"},
        {"text": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "image": "https://via.placeholder.com/600x200"},
    ]
    if st.button("Generate Quote"):
        selected_quote = random.choice(quotes)
        st.image(selected_quote['image'], use_column_width=True)
        st.write(f"**{selected_quote['text']}**")