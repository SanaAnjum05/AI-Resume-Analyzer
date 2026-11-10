# utils/skill_matcher.py

def match_skills(resume_skills, job_skills):
    """
    Compare resume skills with job description skills.
    """

    # Convert both lists to lowercase for comparison
    resume_set = {skill.lower() for skill in resume_skills}
    job_set = {skill.lower() for skill in job_skills}

    # Matched skills
    matched = sorted(resume_set.intersection(job_set))

    # Missing skills
    missing = sorted(job_set - resume_set)

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }