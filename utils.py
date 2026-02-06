from PyPDF2 import PdfReader


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


SKILLS = [
    "python", "sql", "git", "linux",
    "machine learning", "pandas", "numpy", "data analysis", "communication", "web development", "web design", "OOPS", "Object-Oriented Programming", "arrays", "linked lists", "trees", "graphs", "algorithms", "data structures"]


def calculate_ats_score(resume_text):
    text = resume_text.lower()
    score = 0
    matched = []

    # 1. Skill matching (40 points)
    skill_points = 0
    for skill in SKILLS:
        if skill in text:
            matched.append(skill)
            skill_points += 6  # each skill = 6 pts

    score += min(skill_points, 40)

    # 2. Length (20 points)
    word_count = len(text.split())

    if word_count > 500:
        score += 20
    elif word_count > 300:
        score += 15
    elif word_count > 200:
        score += 10
    elif word_count > 100:
        score += 5

    # 3. Sections (25 points)
    sections = ["skills", "projects", "experience", "education"]

    section_points = 0
    for sec in sections:
        if sec in text:
            section_points += 6

    score += min(section_points, 25)

    # 4. Action verbs (15 points)
    verbs = [
        "developed", "designed", "implemented",
        "optimized", "analyzed", "managed", "built"
    ]

    verb_points = 0
    for v in verbs:
        if v in text:
            verb_points += 3

    score += min(verb_points, 15)

    return min(score, 100), matched


def analyze_resume(resume_text):
    text = resume_text.lower()
    words = text.split()

    suggestions = []

    # Length
    if len(words) < 200:
        suggestions.append(
            "Add more detailed descriptions of projects and experience.")

    # Skills
    if "skills" not in text:
        suggestions.append("Include a dedicated Skills section.")

    # Projects
    if "project" not in text:
        suggestions.append("Add at least one technical project.")

    # Experience
    if "experience" not in text and "intern" not in text:
        suggestions.append("Mention internships or work experience.")

    # Action verbs
    verbs = [
        "developed", "implemented", "optimized",
        "designed", "analyzed", "built"
    ]

    if not any(v in text for v in verbs):
        suggestions.append("Use more strong action verbs in descriptions.")

    # Contact
    if "@" not in text:
        suggestions.append("Add a professional email address.")

    return suggestions
