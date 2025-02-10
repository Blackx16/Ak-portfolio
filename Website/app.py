import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="Akshat Pandey - Portfolio",
    page_icon="🎤",
    layout="wide"
)

# Custom CSS with white headers
st.markdown("""
<style>
    :root {
        scroll-behavior: smooth;
        --primary-color: #333333;
        --accent-color: #666666;
        --light-gray: #f5f5f5;
        --medium-gray: #999999;
        --dark-gray: #444444;
    }
    body {
        color: var(--primary-color);
        background-color: white;
    }
    .header {
        font-size: clamp(2rem, 6vw, 3.5rem) !important; 
        font-weight: bold !important;
        color: white;
    }
    .section-header {
        font-size: clamp(1.5rem, 4vw, 2rem) !important; 
        color: white !important;
        margin: 2rem 0 1rem !important;
        background-color: var(--primary-color);
        padding: 1rem !important;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
   .skill-box {
    padding: 1.5rem;
    border-radius: 10px;
    background-color: var(--light-gray);
    margin: 1rem 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border: 1px solid var(--medium-gray);
    color: #000000; /* Added text color */
}
    }
    .highlight {
        color: var(--dark-gray); 
        font-weight: bold;
    }
    .nav-links {
        position: sticky;
        top: 0;
        background-color: rgba(255,255,255,0.95);
        padding: 1rem 0;
        z-index: 1000;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
        backdrop-filter: blur(5px);
    }
    .nav-link {
        color: var(--primary-color);
        padding: 0.5rem 1rem;
        border-radius: 25px;
        transition: all 0.3s ease;
        text-decoration: none !important;
        border: 1px solid var(--accent-color);
        font-size: clamp(0.8rem, 2vw, 1rem);
    }
    .nav-link:hover {
        background-color: var(--primary-color);
        color: white !important;
    }
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        padding: 1rem 0;
    }
    .gallery-item {
        border-radius: 10px;
        overflow: hidden;
        transition: transform 0.3s ease;
        aspect-ratio: 1;
        border: 1px solid var(--medium-gray);
    }
    .gallery-item img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(100%);
        transition: filter 0.3s ease;
    }
    .gallery-item:hover img {
        filter: grayscale(0%);
    }
    .social-card {
    text-align: center;
    padding: 1.5rem;
    border-radius: 10px;
    background: var(--light-gray);
    border: 1px solid var(--medium-gray);
    transition: transform 0.2s ease;
    color: #000000; /* Added text color */
}
    .social-card:hover {
        transform: translateY(-5px);
    }
    .social-button {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        background: var(--primary-color);
        color: white;
        border-radius: 25px;
        text-decoration: none;
        transition: background-color 0.2s ease;
    }
    .social-button:hover {
        background: var(--dark-gray);
        color: white;
    }
    [data-testid="stImage"] img {
        filter: grayscale(100%);
        transition: filter 0.3s ease;
    }
    [data-testid="stImage"] img:hover {
        filter: grayscale(0%);
    }
    .stSubheader {
        color: white !important;
        background-color: var(--primary-color);
        padding: 0.5rem 1rem !important;
        border-radius: 5px;
        margin-bottom: 1rem !important;
    }
    [data-testid="stSubheader"] {
        color: white !important;
        background-color: var(--primary-color);
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    @media (max-width: 768px) {
        .gallery-grid { grid-template-columns: repeat(2, 1fr); }
        .nav-links { gap: 0.5rem; padding: 0.5rem; }
    }
    @media (max-width: 480px) {
        .gallery-grid { grid-template-columns: 1fr; }
    }
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
<nav class="nav-links">
    <a href="#about" class="nav-link">About</a>
    <a href="#education" class="nav-link">Education</a>
    <a href="#skills" class="nav-link">Skills</a>
    <a href="#experience" class="nav-link">Experience</a>
    <a href="#achievements" class="nav-link">Achievements</a>
    <a href="#media" class="nav-link">Media</a>
    <a href="#social" class="nav-link">Social</a>
</nav>
""", unsafe_allow_html=True)

# Profile Header
with st.container():
    col1, col2 = st.columns([1, 3], gap="medium")
    with col1:
        st.image("photos/profile.jpeg", use_container_width=True)
    with col2:
        st.markdown('<p class="header">Akshat Pandey</p>', unsafe_allow_html=True)
        st.markdown("### Anchor | Orator | Public Speaker | Debater")
        st.markdown("📱 +91 9925112498  \n📧 akshatp0905@gmail.com")

# About Section
with st.container():
    st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)
    st.markdown("""
    I am a passionate anchor, public speaker, and debater with a deep love for literature, mythology, and poetry. 
    With experience in anchoring major formal and informal events, I take pride in my ability to engage audiences 
    with confidence and clarity. My journey has been enriched by numerous opportunities that have helped me grow 
    into a versatile speaker and performer.
    """)

# Education Section
with st.container():
    st.markdown('<div id="education" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-header">Educational Background</p>', unsafe_allow_html=True)
    cols = st.columns(3, gap="medium")
    with cols[0]:
        st.markdown("**Kendriya Vidyalaya Sangathan**  \n- Alumni")
    with cols[1]:
        st.markdown("**Kendriya Vidyalaya No.4 ONGC**  \n- Passed out in 2021")
    with cols[2]:
        st.markdown("**GSFC University**  \n- B.Tech Chemical Engineering")

# Skills Section
with st.container():
    st.markdown('<div id="skills" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-header">Skills</p>', unsafe_allow_html=True)
    cols = st.columns(2, gap="medium")
    with cols[0]:
        st.markdown('''
        <div class="skill-box">
            <span class="highlight">✦</span> Exceptional Oratory & Public Speaking<br>
            <span class="highlight">✦</span> Debating & Anchoring Expertise<br>
            <span class="highlight">✦</span> Poetry Recitation & Singing<br>
            <span class="highlight">✦</span> In-depth Literature Knowledge
        </div>''', unsafe_allow_html=True)
    with cols[1]:
        st.markdown('''
        <div class="skill-box">
            <span class="highlight">✦</span> Bilingual Proficiency (Hindi/English)<br>
            <span class="highlight">✦</span> Mythology Expertise<br>
            <span class="highlight">✦</span> Communication & Writing Skills<br>
            <span class="highlight">✦</span> Event Management
        </div>''', unsafe_allow_html=True)

# Experience Section
with st.container():
    st.markdown('<div id="experience" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-header">Experience</p>', unsafe_allow_html=True)
    st.markdown("""
    - **Hosted 10+ events** at GSFC University (both formal and informal)
    - **Anchored key national celebrations**:
      - Independence Day
      - Republic Day
      - University Foundation Day
    - **Featured in social media reels** for:
      - Independence Day 2024
      - Diwali 2024
      - National Youth Day 2024
    """)

# Achievements Section
with st.container():
    st.markdown('<div id="achievements" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-header">Achievements</p>', unsafe_allow_html=True)
    cols = st.columns(2, gap="medium")
    with cols[0]:
        st.markdown("""
        🏅 **Campus Ambassador**  
        GSFC University  
        
        🥇 **Top 1% Student**  
        PMG (President's Meritorious Group)
        """)
    with cols[1]:
        st.markdown("""
        🎖️ **Youth Parliament Representative**  
        Mahatma Mandir, Gandhinagar (2024)  
        
        🌍 **International Delegate**  
        Youth Kindness Seminar, Hyderabad (2024)
        """)
# Media Section
with st.container():
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
with st.container():
    st.markdown('<div id="social" class="section-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-header">Social Media Engagement</p>', unsafe_allow_html=True)
    
    cols = st.columns(3, gap="medium")
    social_links = [
        ("Independence Day", "https://www.instagram.com/reel/C-mzJNDBsF3/", "🎆"),
        ("Diwali Celebrations", "https://www.instagram.com/reel/DBIE37APqdB/", "🪔"),
        ("Youth Day", "https://www.instagram.com/reel/DEtXaymhuDd/", "🌟")
    ]
    
    for col, (title, link, emoji) in zip(cols, social_links):
        with col:
            st.markdown(f"""
            <div class="social-card">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">{emoji}</div>
                <h3 style="margin: 0.5rem 0;">{title}</h3>
                <a href="{link}" target="_blank" class="social-button">
                    Watch Reel
                </a>
            </div>
            """, unsafe_allow_html=True)



# Smooth scrolling JavaScript
html("""
<script>
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if(target) {
                window.scrollTo({
                    top: target.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
</script>
""")