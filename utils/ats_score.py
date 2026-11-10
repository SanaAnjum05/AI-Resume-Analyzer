# utils/ats_score.py

def calculate_ats_score(matched_skills, job_skills):
    """
    Calculate ATS Score
    """

    if len(job_skills) == 0:
        return 0

    score = (len(matched_skills) / len(job_skills)) * 100

    return round(score, 2)