def build_prompt(interest, skill, goal):
    return f"""
You are a career intelligence system.

User Profile:
- Interest: {interest}
- Skill Level: {skill}
- Goal: {goal}

Task:
1. Recommend top 3 career paths
2. For EACH career provide:
   - Why it fits the user
   - Required skills
   - Tools/technologies

3. Generate a structured roadmap:
   - 6 month plan
   - 1 year plan
   - 3 year plan

4. Suggest 2 alternative career paths

Output Format:
Use clear headings, bullet points, and sections.
Be specific and practical.
"""
