"""
Configuration Validator for LinkedIn Auto Job Applier

Validates all configuration values from config.py
"""

from config import (
    # Personals
    first_name, middle_name, last_name, phone_number, current_city,
    street, state, zipcode, country, ethnicity, gender, disability_status, veteran_status,
    # Questions
    default_resume_path, years_of_experience, require_visa, website, linkedIn,
    desired_salary, us_citizenship, linkedin_headline, notice_period, current_ctc,
    linkedin_summary, cover_letter, recent_employer, confidence_level,
    pause_before_submit, pause_at_failed_question, overwrite_previous_answers,
    # Search
    search_terms, search_location, switch_number, randomize_search_order,
    sort_by, date_posted, salary, easy_apply_only, experience_level, job_type, on_site,
    companies, location, industry, job_function, job_titles, benefits, commitments,
    under_10_applicants, in_your_network, fair_chance_employer, pause_after_filters,
    about_company_bad_words, about_company_good_words, bad_words, security_clearance,
    did_masters, current_experience,
    # Secrets
    username, password, use_AI, llm_api_url, llm_api_key, llm_model, ai_provider, stream_output,
    # Settings
    close_tabs, follow_companies, run_non_stop, alternate_sortby, cycle_date_posted,
    stop_date_cycle_at_24hr, generated_resume_path, file_name, failed_file_name,
    logs_folder_path, click_gap, run_in_background, disable_extensions, safe_mode,
    smooth_scroll, keep_screen_awake, stealth_mode, showAiErrorAlerts
)


def check_int(var: int, var_name: str, min_value: int = 0) -> bool:
    if not isinstance(var, int):
        raise TypeError(f'"{var_name}" must be an Integer, got "{var}" ({type(var).__name__})')
    if var < min_value:
        raise ValueError(f'"{var_name}" must be >= {min_value}, got {var}')
    return True


def check_boolean(var: bool, var_name: str) -> bool:
    if var not in (True, False):
        raise ValueError(f'"{var_name}" must be True or False, got "{var}"')
    return True


def check_string(var: str, var_name: str, options: list = None, min_length: int = 0) -> bool:
    if not isinstance(var, str):
        raise TypeError(f'"{var_name}" must be a string, got {type(var).__name__}')
    if min_length > 0 and len(var) < min_length:
        raise ValueError(f'"{var_name}" must be at least {min_length} characters')
    if options and var not in options:
        raise ValueError(f'"{var_name}" must be one of {options}, got "{var}"')
    return True


def check_list(var: list, var_name: str, options: list = None, min_length: int = 0) -> bool:
    if not isinstance(var, list):
        raise TypeError(f'"{var_name}" must be a list')
    if len(var) < min_length:
        raise ValueError(f'"{var_name}" must have at least {min_length} items')
    for element in var:
        if not isinstance(element, str):
            raise TypeError(f'All items in "{var_name}" must be strings')
        if options and element not in options:
            raise ValueError(f'"{element}" in "{var_name}" is not valid. Options: {options}')
    return True


def validate_config() -> None:
    """Validates all configuration values."""
    
    # Personal info (allow empty for manual login flow)
    check_string(first_name, "first_name")
    check_string(middle_name, "middle_name")
    check_string(last_name, "last_name")
    check_string(phone_number, "phone_number")
    check_string(current_city, "current_city")
    check_string(street, "street")
    check_string(state, "state")
    check_string(zipcode, "zipcode")
    check_string(country, "country")
    
    check_string(ethnicity, "ethnicity", 
                 ["Decline", "Hispanic/Latino", "American Indian or Alaska Native", 
                  "Asian", "Black or African American", 
                  "Native Hawaiian or Other Pacific Islander", "White", "Other", ""])
    check_string(gender, "gender", ["Male", "Female", "Other", "Decline", ""])
    check_string(disability_status, "disability_status", ["Yes", "No", "Decline", ""])
    check_string(veteran_status, "veteran_status", ["Yes", "No", "Decline", ""])
    
    # Questions
    check_string(default_resume_path, "default_resume_path")
    check_string(years_of_experience, "years_of_experience")
    check_string(require_visa, "require_visa", ["Yes", "No"])
    check_string(website, "website")
    check_string(linkedIn, "linkedIn")
    check_int(desired_salary, "desired_salary")
    check_int(notice_period, "notice_period")
    check_int(current_ctc, "current_ctc")
    check_string(linkedin_headline, "linkedin_headline")
    check_string(linkedin_summary, "linkedin_summary")
    check_string(cover_letter, "cover_letter")
    check_string(recent_employer, "recent_employer")
    check_string(confidence_level, "confidence_level")
    check_boolean(pause_before_submit, "pause_before_submit")
    check_boolean(pause_at_failed_question, "pause_at_failed_question")
    check_boolean(overwrite_previous_answers, "overwrite_previous_answers")
    
    # Search
    check_list(search_terms, "search_terms", min_length=1)
    check_string(search_location, "search_location")
    check_int(switch_number, "switch_number", 1)
    check_boolean(randomize_search_order, "randomize_search_order")
    check_string(sort_by, "sort_by", ["", "Most recent", "Most relevant"])
    check_string(date_posted, "date_posted", ["", "Any time", "Past month", "Past week", "Past 24 hours"])
    check_string(salary, "salary")
    check_boolean(easy_apply_only, "easy_apply_only")
    
    check_list(experience_level, "experience_level",
               ["Internship", "Entry level", "Associate", "Mid-Senior level", "Director", "Executive"])
    check_list(job_type, "job_type",
               ["Full-time", "Part-time", "Contract", "Temporary", "Volunteer", "Internship", "Other"])
    check_list(on_site, "on_site", ["On-site", "Remote", "Hybrid"])
    
    check_list(companies, "companies")
    check_list(location, "location")
    check_list(industry, "industry")
    check_list(job_function, "job_function")
    check_list(job_titles, "job_titles")
    check_list(benefits, "benefits")
    check_list(commitments, "commitments")
    
    check_boolean(under_10_applicants, "under_10_applicants")
    check_boolean(in_your_network, "in_your_network")
    check_boolean(fair_chance_employer, "fair_chance_employer")
    check_boolean(pause_after_filters, "pause_after_filters")
    
    check_list(about_company_bad_words, "about_company_bad_words")
    check_list(about_company_good_words, "about_company_good_words")
    check_list(bad_words, "bad_words")
    check_boolean(security_clearance, "security_clearance")
    check_boolean(did_masters, "did_masters")
    check_int(current_experience, "current_experience", -1)
    
    # Credentials (allow empty for manual login)
    check_string(username, "username")
    check_string(password, "password")
    check_boolean(use_AI, "use_AI")
    check_string(ai_provider, "ai_provider", ["openai", "deepseek", "gemini"])
    check_string(llm_api_url, "llm_api_url")
    check_string(llm_api_key, "llm_api_key")
    check_string(llm_model, "llm_model")
    check_boolean(stream_output, "stream_output")
    
    # Settings
    check_boolean(close_tabs, "close_tabs")
    check_boolean(follow_companies, "follow_companies")
    check_boolean(run_non_stop, "run_non_stop")
    check_boolean(alternate_sortby, "alternate_sortby")
    check_boolean(cycle_date_posted, "cycle_date_posted")
    check_boolean(stop_date_cycle_at_24hr, "stop_date_cycle_at_24hr")
    check_string(generated_resume_path, "generated_resume_path")
    check_string(file_name, "file_name")
    check_string(failed_file_name, "failed_file_name")
    check_string(logs_folder_path, "logs_folder_path")
    check_int(click_gap, "click_gap")
    check_boolean(run_in_background, "run_in_background")
    check_boolean(disable_extensions, "disable_extensions")
    check_boolean(safe_mode, "safe_mode")
    check_boolean(smooth_scroll, "smooth_scroll")
    check_boolean(keep_screen_awake, "keep_screen_awake")
    check_boolean(stealth_mode, "stealth_mode")
    check_boolean(showAiErrorAlerts, "showAiErrorAlerts")
