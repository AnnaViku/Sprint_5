import random

def generate_email(first_name, last_name, cohort_number):
    return f"{first_name}_{last_name}_{cohort_number}_{random.randint(100, 999)}@example.com"

def generate_password(length=6):
    return 'a' * length  # Для тестирования используем простой пароль