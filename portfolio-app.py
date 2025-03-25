# File: 📁 portfolio_app/app.py
import streamlit as st

def main():
    # Set up the page configuration
    st.set_page_config(
        page_title="Alex Rivera - Portfolio", 
        page_icon="💻", 
        layout="wide"
    )

    # Sidebar navigation
    st.sidebar.title("Portfolio Navigation")
    section = st.sidebar.radio(
        "Explore Sections", 
        ["Home", "About Me", "Skills", "Projects", "Contact"]
    )

    # Home Section
    if section == "Home":
        home_section()
    
    # About Me Section
    elif section == "About Me":
        about_me_section()
    
    # Skills Section
    elif section == "Skills":
        skills_section()
    
    # Projects Section
    elif section == "Projects":
        projects_section()
    
    # Contact Section
    elif section == "Contact":
        contact_section()

def home_section():
    st.title("Alex Rivera | Software Engineer")
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Welcome to My Digital Portfolio

        I'm a passionate **Software Engineer** specializing in:
        - Full Stack Web Development
        - Machine Learning
        - Data Science
        - Innovative Tech Solutions

        My mission is to create scalable, user-friendly applications that solve real-world problems.
        """)
    
    with col2:
        st.image("https://via.placeholder.com/300", caption="Alex Rivera", use_column_width=True)

def about_me_section():
    st.title("About Me")
    
    st.markdown("""
    ### Professional Journey

    I am a dedicated software engineer with 5+ years of experience in creating innovative web and mobile applications. My expertise lies in full-stack development, machine learning, and crafting scalable solutions.

    #### Professional Highlights
    - 🚀 Developed multiple end-to-end web and mobile applications
    - 🧠 Specialized in Machine Learning and AI technologies
    - 💡 Passionate about solving complex technical challenges
    - 🌐 Strong believer in continuous learning and technology evolution
    """)

def skills_section():
    st.title("Skills & Technologies")
    
    # Skill categories
    categories = {
        "Programming Languages": ["Python", "JavaScript", "TypeScript", "Java"],
        "Web Technologies": ["React", "Node.js", "Django", "Flask", "FastAPI"],
        "Machine Learning": ["TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "NumPy"],
        "Tools & Platforms": ["Git", "Docker", "Kubernetes", "AWS", "Streamlit"]
    }

    for category, skills in categories.items():
        st.subheader(category)
        st.write(" | ".join(skills))
        st.markdown("---")
        
def projects_section():
    st.title("Research & Development Projects")
    
    projects = [
        {
            "name": "LLM-Based Research Agent",
            "description": "CrewAI-based agent for academic content generation.",
            "technologies": ["CrewAI", "Python", "Large Language Models"],
            "details": [
                "Developed an autonomous research agent using CrewAI framework",
                "Implemented multi-agent collaboration for content generation",
                "Automated literature review and synthesis processes"
            ],
            "github": "https://github.com/username/llm-research-agent",
            "type": "AI Research"
        },
        {
            "name": "Finance Trading Bot",
            "description": "AI-powered trading bot using Django, CrewAI, and CCXT.",
            "technologies": ["Django", "CrewAI", "CCXT", "Machine Learning"],
            "details": [
                "Created an intelligent trading algorithm with AI decision-making",
                "Integrated multiple cryptocurrency exchanges via CCXT",
                "Implemented risk management and portfolio optimization strategies"
            ],
            "github": "https://github.com/username/ai-trading-bot",
            "type": "Financial Technology"
        },
        {
            "name": "MultiHQA Dataset",
            "description": "A dataset for multi-hop question answering in STEM.",
            "technologies": ["NLP", "Data Collection", "Question Answering"],
            "details": [
                "Curated a specialized dataset for complex STEM questions",
                "Developed multi-hop reasoning capabilities",
                "Contributed to advancing NLP research in scientific domains"
            ],
            "github": "https://github.com/username/multihqa-dataset",
            "type": "Academic Research"
        },
        {
            "name": "AI-Powered Chatbot",
            "description": "Django-based chatbot trained on Investopedia instruction-tuning dataset.",
            "technologies": ["Django", "NLP", "Machine Learning"],
            "details": [
                "Built a context-aware financial knowledge chatbot",
                "Fine-tuned on domain-specific financial instruction data",
                "Implemented advanced conversational AI techniques"
            ],
            "github": "https://github.com/username/financial-chatbot",
            "type": "Conversational AI"
        },
        {
            "name": "Streamlit Chrome Extension Integration",
            "description": "Added Chrome extension support for Streamlit web applications.",
            "technologies": ["Streamlit", "Chrome Extensions", "Web Development"],
            "details": [
                "Developed a novel integration method for Streamlit apps",
                "Created a bridge between browser extensions and web applications",
                "Enhanced user interaction and browser-based tool capabilities"
            ],
            "github": "https://github.com/username/streamlit-chrome-extension",
            "type": "Web Technology"
        },
        {
            "name": "Human-Centered AI Data Generation",
            "description": "Created sample data for pivot tables related to AI augmenting human capabilities.",
            "technologies": ["Data Science", "AI", "Data Visualization"],
            "details": [
                "Generated comprehensive datasets highlighting AI's collaborative potential",
                "Developed innovative pivot table methodologies",
                "Explored human-AI interaction data modeling"
            ],
            "github": "https://github.com/username/human-ai-data-gen",
            "type": "Data Research"
        },
        {
            "name": "Custom Transformer Model",
            "description": "Developed a transformer-based model for domain-specific NLP tasks.",
            "technologies": ["Transformers", "NLP", "Machine Learning"],
            "details": [
                "Designed a specialized transformer architecture",
                "Achieved state-of-the-art performance in domain-specific tasks",
                "Implemented custom tokenization and training strategies"
            ],
            "github": "https://github.com/username/custom-transformer",
            "type": "Machine Learning"
        },
        {
            "name": "Portfolio & Blogging Website",
            "description": "Built a personal website using Streamlit and Docker, integrating previous data.",
            "technologies": ["Streamlit", "Docker", "Web Development"],
            "details": [
                "Created a dynamic personal portfolio platform",
                "Implemented containerized deployment with Docker",
                "Developed a responsive and interactive web presence"
            ],
            "github": "https://github.com/username/personal-portfolio",
            "type": "Web Development"
        }
    ]

    # Project type filter
    project_types = ["All"] + list(set(project['type'] for project in projects))
    selected_type = st.selectbox("Filter Projects by Type", project_types)

    # Search functionality
    search_term = st.text_input("Search Projects")

    # Filter projects
    filtered_projects = [
        project for project in projects 
        if (selected_type == "All" or project['type'] == selected_type) and
           (search_term.lower() in project['name'].lower() or 
            search_term.lower() in project['description'].lower())
    ]

    # Display projects in a grid
    for i in range(0, len(filtered_projects), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(filtered_projects):
                project = filtered_projects[i + j]
                with cols[j]:
                    with st.expander(project['name']):
                        st.markdown(f"**Description:** {project['description']}")
                        st.markdown("**Technologies:** " + " | ".join(project['technologies']))
                        st.markdown("**Project Highlights:**")
                        for detail in project['details']:
                            st.markdown(f"- {detail}")
                        
                        # GitHub Link
                        st.markdown(f"[View on GitHub]({project['github']})")
                        
                        # Project Type Tag
                        st.badge(project['type'])

    for project in projects:
        with st.expander(project["name"]):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown("**Technologies:** " + " | ".join(project["technologies"]))
            st.markdown("**Project Highlights:**")
            for highlight in project["highlights"]:
                st.markdown(f"- {highlight}")

def contact_section():
    st.title("Get In Touch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Contact Information
        - 📧 Email: alex.rivera@example.com
        - 🌐 Website: [www.alexrivera.com](https://www.alexrivera.com)
        - 💼 LinkedIn: [Alex Rivera](https://linkedin.com/in/alexrivera)
        """)
    
    with col2:
        st.markdown("""
        ### Send a Message
        With this form, you can directly reach out to me:
        """)
        contact_form = st.form(key='contact_form')
        name = contact_form.text_input("Your Name")
        email = contact_form.text_input("Your Email")
        message = contact_form.text_area("Your Message")
        submit_button = contact_form.form_submit_button("Send Message")
        
        if submit_button:
            st.success("Message sent successfully! I'll get back to you soon.")

if __name__ == "__main__":
    main()
