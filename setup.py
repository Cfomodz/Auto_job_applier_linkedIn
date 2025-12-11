#!/usr/bin/env python3
"""
Interactive Setup Script for LinkedIn Auto Job Applier

Run this after cloning to configure your settings.
"""

import os
import sys
from pathlib import Path


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title: str):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")


def get_input(prompt: str, default: str = "", required: bool = False, options: list = None) -> str:
    """Get user input with optional default value and validation."""
    if options:
        options_str = " / ".join(options[:4])
        if len(options) > 4:
            options_str += " / ..."
        prompt = f"{prompt} ({options_str})"
    
    if default:
        prompt = f"{prompt} [{default}]"
    
    prompt = f"{prompt}: "
    
    while True:
        value = input(prompt).strip()
        
        if not value and default:
            return default
        
        if not value and required:
            print("  ⚠️  This field is required.")
            continue
        
        if options and value and value not in options:
            print(f"  ⚠️  Choose from: {', '.join(options)}")
            continue
        
        return value


def save_env_file(config: dict, filepath: Path):
    """Save configuration to .env file."""
    content = """# LinkedIn Auto Job Applier - Environment Configuration
# NEVER commit this file to version control!

# ============================================
# LINKEDIN CREDENTIALS
# ============================================
LINKEDIN_USERNAME={LINKEDIN_USERNAME}
LINKEDIN_PASSWORD={LINKEDIN_PASSWORD}

# ============================================
# PERSONAL INFORMATION
# ============================================
FIRST_NAME={FIRST_NAME}
MIDDLE_NAME={MIDDLE_NAME}
LAST_NAME={LAST_NAME}
PHONE_NUMBER={PHONE_NUMBER}
CURRENT_CITY={CURRENT_CITY}
STREET_ADDRESS={STREET_ADDRESS}
STATE={STATE}
ZIPCODE={ZIPCODE}
COUNTRY={COUNTRY}

# ============================================
# DEMOGRAPHICS (EEO)
# ============================================
ETHNICITY={ETHNICITY}
GENDER={GENDER}
DISABILITY_STATUS={DISABILITY_STATUS}
VETERAN_STATUS={VETERAN_STATUS}

# ============================================
# PROFESSIONAL INFO
# ============================================
YEARS_OF_EXPERIENCE={YEARS_OF_EXPERIENCE}
CURRENT_EXPERIENCE={CURRENT_EXPERIENCE}
REQUIRE_VISA={REQUIRE_VISA}
WEBSITE={WEBSITE}
LINKEDIN_PROFILE={LINKEDIN_PROFILE}
US_CITIZENSHIP={US_CITIZENSHIP}
RECENT_EMPLOYER={RECENT_EMPLOYER}
CONFIDENCE_LEVEL={CONFIDENCE_LEVEL}

# ============================================
# SALARY & COMPENSATION
# ============================================
DESIRED_SALARY={DESIRED_SALARY}
CURRENT_CTC={CURRENT_CTC}
NOTICE_PERIOD_DAYS={NOTICE_PERIOD_DAYS}

# ============================================
# AI CONFIGURATION
# ============================================
USE_AI={USE_AI}
AI_PROVIDER={AI_PROVIDER}
LLM_API_URL={LLM_API_URL}
LLM_API_KEY={LLM_API_KEY}
LLM_MODEL={LLM_MODEL}
LLM_SPEC={LLM_SPEC}
STREAM_OUTPUT={STREAM_OUTPUT}

# ============================================
# RESUME
# ============================================
DEFAULT_RESUME_PATH={DEFAULT_RESUME_PATH}
"""
    with open(filepath, 'w') as f:
        f.write(content.format(**config))
    print(f"✅ Saved {filepath}")


def save_config_file(search_config: dict, text_config: dict, settings_config: dict, filepath: Path):
    """Save the single config.py file."""
    content = '''"""
LinkedIn Auto Job Applier - Configuration

All personal/sensitive data loads from .env
Run `python setup.py` to reconfigure.
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
# PROFILE TEXT
# ============================================
linkedin_headline = """{linkedin_headline}"""

linkedin_summary = """{linkedin_summary}"""

cover_letter = """{cover_letter}"""

user_information_all = """{user_information_all}"""


# ============================================
# JOB SEARCH
# ============================================
search_terms = {search_terms}

search_location = "{search_location}"
switch_number = {switch_number}
randomize_search_order = {randomize_search_order}

# Filters
sort_by = "{sort_by}"
date_posted = "{date_posted}"
salary = "{salary}"
easy_apply_only = {easy_apply_only}

experience_level = {experience_level}
job_type = {job_type}
on_site = {on_site}

# Dynamic filters
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
about_company_bad_words = {about_company_bad_words}
about_company_good_words = []
bad_words = {bad_words}

current_experience = int(os.getenv("CURRENT_EXPERIENCE", "0"))
security_clearance = {security_clearance}
did_masters = {did_masters}


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
click_gap = {click_gap}
run_in_background = {run_in_background}
disable_extensions = False
safe_mode = False
smooth_scroll = False
keep_screen_awake = True
stealth_mode = {stealth_mode}
showAiErrorAlerts = False

# Application flow
pause_before_submit = {pause_before_submit}
pause_at_failed_question = {pause_at_failed_question}
overwrite_previous_answers = False
'''
    
    # Merge all configs
    all_config = {**search_config, **text_config, **settings_config}
    
    with open(filepath, 'w') as f:
        f.write(content.format(**all_config))
    
    print(f"✅ Saved {filepath}")


def run_setup():
    """Main setup function."""
    clear_screen()
    print_header("LinkedIn Auto Job Applier - Setup")
    
    print("This wizard configures the bot. Press Enter for defaults.\n")
    
    base_path = Path(__file__).parent
    env_file = base_path / ".env"
    config_file = base_path / "config.py"
    
    env_config = {}
    search_config = {}
    text_config = {}
    settings_config = {}
    
    # Check existing .env
    if env_file.exists():
        choice = get_input("⚠️  .env exists. What to do?", "skip", 
                          options=["skip", "overwrite"])
        if choice == "skip":
            print("Keeping existing .env, configuring other settings...\n")
            skip_env = True
        else:
            skip_env = False
    else:
        skip_env = False
    
    if not skip_env:
        # ==========================================
        # Personal Information
        # ==========================================
        print_header("Personal Information")
        
        env_config["FIRST_NAME"] = get_input("First name", required=True)
        env_config["MIDDLE_NAME"] = get_input("Middle name")
        env_config["LAST_NAME"] = get_input("Last name", required=True)
        env_config["PHONE_NUMBER"] = get_input("Phone (10 digits)", required=True)
        env_config["CURRENT_CITY"] = get_input("City")
        env_config["STREET_ADDRESS"] = get_input("Street address")
        env_config["STATE"] = get_input("State")
        env_config["ZIPCODE"] = get_input("Zip code")
        env_config["COUNTRY"] = get_input("Country", "United States")
        
        # Demographics
        print_header("Demographics (EEO)")
        env_config["ETHNICITY"] = get_input("Ethnicity", "Decline",
            options=["Decline", "White", "Asian", "Black or African American", 
                    "Hispanic/Latino", "Other"])
        env_config["GENDER"] = get_input("Gender", "Decline",
            options=["Male", "Female", "Other", "Decline"])
        env_config["DISABILITY_STATUS"] = get_input("Disability", "Decline",
            options=["Yes", "No", "Decline"])
        env_config["VETERAN_STATUS"] = get_input("Veteran", "Decline",
            options=["Yes", "No", "Decline"])
        
        # Professional
        print_header("Professional Information")
        env_config["YEARS_OF_EXPERIENCE"] = get_input("Years of experience", "0")
        env_config["CURRENT_EXPERIENCE"] = get_input("Experience level for matching", 
                                                     env_config["YEARS_OF_EXPERIENCE"])
        env_config["REQUIRE_VISA"] = get_input("Need visa sponsorship?", "No",
            options=["Yes", "No"])
        env_config["WEBSITE"] = get_input("Portfolio/GitHub URL")
        env_config["LINKEDIN_PROFILE"] = get_input("LinkedIn profile URL")
        env_config["US_CITIZENSHIP"] = get_input("Citizenship status", 
            "U.S. Citizen/Permanent Resident")
        env_config["RECENT_EMPLOYER"] = get_input("Most recent employer")
        env_config["CONFIDENCE_LEVEL"] = get_input("Confidence (1-10)", "7")
        
        # Salary
        print_header("Compensation")
        env_config["DESIRED_SALARY"] = get_input("Desired salary (annual)", "100000")
        env_config["CURRENT_CTC"] = get_input("Current compensation", "80000")
        env_config["NOTICE_PERIOD_DAYS"] = get_input("Notice period (days)", "14")
        
        # LinkedIn & AI
        print_header("LinkedIn & AI")
        print("Leave credentials empty to login manually.\n")
        env_config["LINKEDIN_USERNAME"] = get_input("LinkedIn email")
        env_config["LINKEDIN_PASSWORD"] = get_input("LinkedIn password")
        
        use_ai = get_input("Enable AI?", "n", options=["y", "n"])
        env_config["USE_AI"] = "true" if use_ai == "y" else "false"
        
        if use_ai == "y":
            env_config["AI_PROVIDER"] = get_input("Provider", "openai",
                options=["openai", "deepseek", "gemini"])
            env_config["LLM_API_URL"] = get_input("API URL", "https://api.openai.com/v1/")
            env_config["LLM_API_KEY"] = get_input("API Key")
            env_config["LLM_MODEL"] = get_input("Model", "gpt-4o-mini")
            env_config["LLM_SPEC"] = get_input("Spec", "openai")
            env_config["STREAM_OUTPUT"] = "false"
        else:
            env_config["AI_PROVIDER"] = "openai"
            env_config["LLM_API_URL"] = "https://api.openai.com/v1/"
            env_config["LLM_API_KEY"] = ""
            env_config["LLM_MODEL"] = "gpt-4o-mini"
            env_config["LLM_SPEC"] = "openai"
            env_config["STREAM_OUTPUT"] = "false"
        
        env_config["DEFAULT_RESUME_PATH"] = get_input("Resume path", "resumes/resume.pdf")
        
        save_env_file(env_config, env_file)
    
    # ==========================================
    # Job Search
    # ==========================================
    print_header("Job Search")
    
    terms = get_input("Job titles (comma-separated)", 
                      "Software Engineer, Python Developer")
    search_config["search_terms"] = [s.strip() for s in terms.split(",")]
    search_config["search_location"] = get_input("Location", "United States")
    search_config["switch_number"] = get_input("Apps per search term", "30")
    search_config["randomize_search_order"] = get_input("Randomize order?", "False",
        options=["True", "False"])
    
    search_config["sort_by"] = get_input("Sort by", "",
        options=["", "Most recent", "Most relevant"])
    search_config["date_posted"] = get_input("Date posted", "Past month",
        options=["Any time", "Past month", "Past week", "Past 24 hours"])
    search_config["salary"] = get_input("Min salary filter", "",
        options=["", "$60,000+", "$80,000+", "$100,000+", "$120,000+"])
    search_config["easy_apply_only"] = get_input("Easy Apply only?", "True",
        options=["True", "False"])
    
    exp = get_input("Experience level (comma-sep)", "")
    search_config["experience_level"] = [s.strip() for s in exp.split(",") if s.strip()] if exp else []
    
    jt = get_input("Job type (comma-sep)", "Full-time")
    search_config["job_type"] = [s.strip() for s in jt.split(",") if s.strip()] if jt else []
    
    loc = get_input("Work location (comma-sep)", "Remote, Hybrid")
    search_config["on_site"] = [s.strip() for s in loc.split(",") if s.strip()] if loc else []
    
    bad = get_input("Bad words to skip", "")
    search_config["bad_words"] = [s.strip() for s in bad.split(",") if s.strip()] if bad else []
    
    avoid = get_input("Companies to avoid", "Crossover")
    search_config["about_company_bad_words"] = [s.strip() for s in avoid.split(",") if s.strip()] if avoid else []
    
    search_config["security_clearance"] = get_input("Have clearance?", "False",
        options=["True", "False"])
    search_config["did_masters"] = get_input("Have Master's?", "False",
        options=["True", "False"])
    
    # ==========================================
    # Profile Text
    # ==========================================
    print_header("Profile Text")
    
    text_config["linkedin_headline"] = get_input("LinkedIn headline", "")
    text_config["linkedin_summary"] = get_input("Summary (or Enter to skip)", "")
    text_config["cover_letter"] = get_input("Cover letter (or Enter to skip)", "")
    text_config["user_information_all"] = get_input("Additional info for AI", "")
    
    # ==========================================
    # Settings
    # ==========================================
    print_header("Bot Settings")
    
    settings_config["click_gap"] = get_input("Click delay (seconds)", "1")
    settings_config["run_in_background"] = get_input("Run headless?", "False",
        options=["True", "False"])
    settings_config["stealth_mode"] = get_input("Stealth mode?", "True",
        options=["True", "False"])
    settings_config["pause_before_submit"] = get_input("Pause before submit?", "True",
        options=["True", "False"])
    settings_config["pause_at_failed_question"] = get_input("Pause on failed questions?", "True",
        options=["True", "False"])
    
    # Save config.py
    save_config_file(search_config, text_config, settings_config, config_file)
    
    # Create directories
    (base_path / "logs" / "screenshots").mkdir(parents=True, exist_ok=True)
    (base_path / "all excels").mkdir(parents=True, exist_ok=True)
    (base_path / "resumes").mkdir(parents=True, exist_ok=True)
    
    # Done
    print_header("Setup Complete! 🎉")
    print("To run the bot:\n")
    print("  source venv/bin/activate")
    print("  python runAiBot.py\n")
    print("Files created:")
    print(f"  • .env - Personal info (edit directly for changes)")
    print(f"  • config.py - Search & bot settings\n")


if __name__ == "__main__":
    try:
        run_setup()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled.")
        sys.exit(0)
