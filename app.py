import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="Akshat Pandey - Portfolio",
    page_icon="🎤",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .header {font-size: 50px !important; font-weight: bold !important;}
    .section-header {font-size: 30px !important; color: #2e86c1 !important;}
    .skill-box {padding: 15px; border-radius: 10px; background-color: #f2f3f4; margin: 10px 0;}
</style>
""", unsafe_allow_html=True)

# Profile Header
col1, col2 = st.columns([1, 3])
with col1:
    # Add your profile photo (replace 'profile.jpg' with your image file)
    st.image("photos/profile.jpeg", width=200)
with col2:
    st.markdown('<p class="header">Akshat Pandey</p>', unsafe_allow_html=True)
    st.write("Anchor | Orator | Public Speaker | Debater")
    st.write("📱 +91 9925112498")
    st.write("📧 akshatp0905@gmail.com")

# Navigation
st.write("---")
menu = ["Home", "Education", "Skills", "Experience", "Achievements", "Media", "Social Links"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Section
if choice == "Home":
    st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)
    st.write("""
    Dynamic communicator and event host with extensive experience in anchoring university events. 
    Proven track record in public speaking, debating, and content creation. Currently pursuing 
    Chemical Engineering while actively participating in academic and cultural initiatives.
    """)

# Education Section
elif choice == "Education":
    st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)
    st.subheader("Kendriya Vidyalaya Sangathan")
    st.write("- Alumni")
    
    st.subheader("Kendriya Vidyalaya No.4 ONGC, Vadodara")
    st.write("- Graduated in 2021")
    
    st.subheader("GSFC University, Vadodara")
    st.write("- Currently pursuing BTech in Chemical Engineering")

# Skills Section
elif choice == "Skills":
    st.markdown('<p class="section-header">Skills</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="skill-box">'
                    '🎤 Public Speaking & Anchoring<br>'
                    '💬 Communication & Debate<br>'
                    '📚 Literature & Mythology<br>'
                    '🎭 Event Management</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="skill-box">'
                    '🌐 Bilingual Proficiency (Hindi/English)<br>'
                    '✍️ Content Creation & Writing<br>'
                    '🎥 Video Production<br>'
                    '🎶 Music & Poetry</div>', unsafe_allow_html=True)

# Experience Section
elif choice == "Experience":
    st.markdown('<p class="section-header">Experience</p>', unsafe_allow_html=True)
    st.subheader("Event Anchoring")
    st.write("- Hosted 10+ university events including formal and informal functions")
    st.write("- Anchored major national celebrations (Independence Day, Republic Day, Foundation Day)")
    
    st.subheader("Content Creation")
    st.write("- Produced promotional reels for GSFC University social media")
    st.write("- Covered festivals and national events (Diwali, National Youth Day)")

# Achievements Section
elif choice == "Achievements":
    st.markdown('<p class="section-header">Achievements</p>', unsafe_allow_html=True)
    st.write("🏅 Campus Ambassador for GSFC University")
    st.write("🎖️ Top 1% Student - PMG (President's Meritorious Group)")
    st.write("🏛️ Participant - Youth Parliament at Mahatma Mandir, Gandhinagar")
    st.write("🌍 Delegate - International Youth Kindness Seminar, Hyderabad")

# Media Section
elif choice == "Media":
    st.markdown('<p class="section-header">Media Gallery</p>', unsafe_allow_html=True)
    
    # Video Section
    st.subheader("Featured Videos")
    tab1, tab2, tab3 = st.tabs(["Foundation Day", "Independence Day", "Republic Day"])
    
    with tab1:
        st.video("https://www.youtube.com/embed/7Fzq5t4BTVs?si=GNk68mqAGzz2ork7")
    with tab2:
        st.video("https://youtu.be/L1bDMYQ6mr8?si=MpZ3jE2vTcErPzWK")
    with tab3:
        st.video("https://www.youtube.com/embed/YMr-EaR5-QY?si=1k_x9NAQqv5Ipfqv")

    # Photo Gallery
    st.subheader("Portfolio Snapshots")
    
    # Create grid layout for photos
    cols = st.columns(4)
    for idx in range(2, 21):
        with cols[(idx-2) % 4]:
            try:
                st.image(f"photos/{idx}.jpeg", use_container_width=True)  # Updated parameter here
            except:
                st.error(f"Image {idx}.jpeg not found")

# Social Links Section
elif choice == "Social Links":
    st.markdown('<p class="section-header">Social Media Content</p>', unsafe_allow_html=True)
    
    st.subheader("Instagram Reels")
    reel_cols = st.columns(3)
    with reel_cols[0]:
        html(f"""
        <a href="https://www.instagram.com/reeI/C-mzJNDBsF3/">
            <img src="https://img.icons8.com/fluency/48/instagram-reel.png" width="50"/>
            <p>Independence Day 2024</p>
        </a>
        """)
    with reel_cols[1]:
        html(f"""
        <a href="https://www.instagram.com/reeI/DBIE37APqdB/">
            <img src="https://img.icons8.com/fluency/48/instagram-reel.png" width="50"/>
            <p>Diwali 2024</p>
        </a>
        """)
    with reel_cols[2]:
        html(f"""
        <a href="https://www.instagram.com/reeI/DEtXaymhuDd/">
            <img src="https://img.icons8.com/fluency/48/instagram-reel.png" width="50"/>
            <p>National Youth Day 2024</p>
        </a>
        """)