import re

# List of common technical skills
SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "Git",
    "GitHub",
    "Machine Learning",
    "Deep Learning",
    "Data Analysis",
    "Power BI",
    "Excel",
    "AWS",
    "Docker",
    "Flask",
    "Django",
    "Streamlit"
]

def parse_resume(text):
    """
    Extract email, phone number, and skills from resume text.
    """

    data = {}

    # ------------------------
    # Email
    # ------------------------
    email = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    data["Email"] = email[0] if email else "Not Found"

    # ------------------------
    # Phone Number
    # ------------------------
    phone = re.findall(
        r'\b\d{10}\b',
        text
    )

    data["Phone"] = phone[0] if phone else "Not Found"

    # ------------------------
    # Skills
    # ------------------------
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    data["Skills"] = found_skills

    return data