"""
LinkedIn Auto Job Applier - Configuration

All personal/sensitive data loads from .env
Run `python setup.py` to configure interactively.
"""

import os
from dotenv import load_dotenv

load_dotenv()


# ============================================
# PERSONAL INFO (from .env)
# ============================================
first_name = os.getenv("FIRST_NAME", "")
middle_name = os.getenv("MIDDLE_NAME", "")
last_name = os.getenv("LAST_NAME", "")
phone_number = os.getenv("PHONE_NUMBER", "")
current_city = os.getenv("CURRENT_CITY", "")
street = os.getenv("STREET_ADDRESS", "")
state = os.getenv("STATE", "")
zipcode = os.getenv("ZIPCODE", "")
country = os.getenv("COUNTRY", "United States")

# EEO / Demographics
ethnicity = os.getenv("ETHNICITY", "Decline")
gender = os.getenv("GENDER", "Decline")
disability_status = os.getenv("DISABILITY_STATUS", "Decline")
veteran_status = os.getenv("VETERAN_STATUS", "Decline")


# ============================================
# CREDENTIALS & AI (from .env)
# ============================================
username = os.getenv("LINKEDIN_USERNAME", "")
password = os.getenv("LINKEDIN_PASSWORD", "")

use_AI = os.getenv("USE_AI", "false").lower() == "true"
ai_provider = os.getenv("AI_PROVIDER", "openai")
llm_api_url = os.getenv("LLM_API_URL", "https://api.openai.com/v1/")
llm_api_key = os.getenv("LLM_API_KEY", "not-needed")
llm_model = os.getenv("LLM_MODEL", "gpt-4o-mini")
llm_spec = os.getenv("LLM_SPEC", "openai")
stream_output = os.getenv("STREAM_OUTPUT", "false").lower() == "true"


# ============================================
# APPLICATION ANSWERS (from .env)
# ============================================
default_resume_path = os.getenv("DEFAULT_RESUME_PATH", "resumes/resume.pdf")
years_of_experience = os.getenv("YEARS_OF_EXPERIENCE", "0")
require_visa = os.getenv("REQUIRE_VISA", "No")
website = os.getenv("WEBSITE", "")
linkedIn = os.getenv("LINKEDIN_PROFILE", "")
us_citizenship = os.getenv("US_CITIZENSHIP", "U.S. Citizen/Permanent Resident")
desired_salary = int(os.getenv("DESIRED_SALARY", "100000"))
current_ctc = int(os.getenv("CURRENT_CTC", "80000"))
notice_period = int(os.getenv("NOTICE_PERIOD_DAYS", "14"))
recent_employer = os.getenv("RECENT_EMPLOYER", "")
confidence_level = os.getenv("CONFIDENCE_LEVEL", "7")


# ============================================
# PROFILE TEXT (edit these or regenerate with setup.py)
# ============================================
linkedin_headline = """Offensive Security Engineer | Python Automation & AI Integration Specialist"""

linkedin_summary = """Automation-focused Security Engineer with 8+ years of experience in software development, IT systems, and applied cybersecurity. Ranked #1 Verified Creator on n8n.io for secure automation workflows and contributor to open-source security and AI integration projects. Combines deep Python expertise, reverse engineering, and systems automation to identify and resolve existing and emerging vulnerabilities through intelligent tooling and creative problem-solving. Security+, PC Pro, and Computer Programming certified."""

cover_letter = """Dear Hiring Manager,

I am writing to express my strong interest in this position. As an Automation-focused Security Engineer with 8+ years of experience in software development, IT systems, and applied cybersecurity, I bring a unique combination of offensive security expertise and Python automation skills.

Key highlights of my background include:
• Ranked #1 Verified Creator on n8n.io, building 200+ secure automation workflows used by developers worldwide
• Contributing Developer at Browser Use, collaborating with founders on security improvements and bot detection bypass methods
• AI Differential Programmer at METR, developing AI-assisted workflows with focus on security and compliance
• Strong Python expertise with experience in Flask, REST APIs, web scraping, and security tooling
• Proficient with security tools including Burp Suite, Kali Linux, Nmap, Metasploit, and Wireshark

I am passionate about combining security engineering with intelligent automation to identify and resolve vulnerabilities. My experience spans penetration testing, vulnerability assessment, red teaming, and building secure AI integrations.

I would welcome the opportunity to discuss how my skills align with your team's needs.

Best regards,
David Ashby"""

user_information_all = """Name: David Ashby
Email: Dd@vidashby.com
Phone: 801.857.9474
LinkedIn: https://www.linkedin.com/in/david-ashby/
GitHub: https://github.com/Cfomodz
Location: Helena, Montana, United States

EXPERIENCE: 8+ years in software development, IT systems, and applied cybersecurity

CURRENT ROLES:
- N8N / AI Automation Workflow Creator (March 2025 - Present) - Ranked #1 Verified Creator on n8n.io
- Beyond Nodes Automation Lab Community Lead + Educator (July 2025 - Present) - Managing 600+ members
- YC Agents Hackathon Judge (August 2025)

RECENT EXPERIENCE:
- Browser Use / Contributing Developer (Feb 2025 - Aug 2025) - Security improvements, bot detection bypass
- METR / AI Differential Programmer (Jan 2025 - Aug 2025) - AI workflows with security focus
- Hughes Real Estate Group / Software Developer + IT Support (Jan 2021 - Mar 2024)

SKILLS:
Cybersecurity: Penetration Testing, Vulnerability Assessment, Red Teaming, Reverse Engineering, Ethical Hacking, Web App Security (XSS, SQLi, CSRF), Network Security, Threat Hunting, OSINT
Security Tools: Burp Suite, Kali Linux, Nmap, Metasploit, Wireshark, Active Directory, VPN, Firewalls, IAM, MFA
Programming: Python, Flask, JavaScript, SQL, REST APIs, OAuth2, Web Scraping, Automation (n8n, Cron)
Infrastructure: Linux Administration, Docker, Networking (TCP/IP, DNS, DHCP), AWS, Google Cloud
AI: Machine Learning APIs, RAG Pipelines, OpenAI, LangChain

EDUCATION:
- Western Governor's University - Bachelor's in Cybersecurity (in progress, estimated 2026)
- Brigham Young University - Idaho - Certificate in Computer Programming (December 2020)

CERTIFICATIONS: Security+, PC Pro
UPCOMING CERTS: PenTest+, ITIL 4, A+, Data+, Network+, Project+, CySA+, CCSP, SSCP"""


# ============================================
# JOB SEARCH
# ============================================
search_terms = [
    "Security Engineer",
    "Offensive Security Engineer",
    "Penetration Tester",
    "Python Developer",
    "Cybersecurity Engineer",
    "Application Security Engineer",
    "Red Team Engineer",
    "Security Automation Engineer",
    "AI Security Engineer",
    "DevSecOps Engineer",
    "Vulnerability Researcher",
    "Security Analyst",
]

search_location = "United States"
switch_number = 30
randomize_search_order = False

# Filters
sort_by = ""
date_posted = "Past month"
salary = "$80,000+"
easy_apply_only = True

experience_level = ["Mid-Senior level", "Associate"]
job_type = ["Full-time", "Contract"]
on_site = ["On-site", "Remote", "Hybrid"]

# Dynamic filters (leave empty if not needed)
companies = []
location = []
industry = []
job_function = []
job_titles = []
benefits = []
commitments = []

under_10_applicants = False
in_your_network = False
fair_chance_employer = False
pause_after_filters = True

# Skip jobs
about_company_bad_words = ["Crossover"]
about_company_good_words = []
bad_words = ["No C2C", "No Corp2Corp", ".NET", "Embedded Programming", "PHP", "Ruby", "CNC", "COBOL", "Mainframe"]

current_experience = int(os.getenv("CURRENT_EXPERIENCE", "8"))
security_clearance = False
did_masters = False


# ============================================
# BOT SETTINGS
# ============================================
close_tabs = False
follow_companies = False
run_non_stop = False
alternate_sortby = True
cycle_date_posted = True
stop_date_cycle_at_24hr = True

# Paths
generated_resume_path = "all resumes/"
file_name = "all excels/all_applied_applications_history.csv"
failed_file_name = "all excels/all_failed_applications_history.csv"
logs_folder_path = "logs/"

# Behavior
click_gap = 1
run_in_background = False
disable_extensions = False
safe_mode = False
smooth_scroll = False
keep_screen_awake = True
stealth_mode = True
showAiErrorAlerts = False

# Application flow
pause_before_submit = True
pause_at_failed_question = True
overwrite_previous_answers = False

