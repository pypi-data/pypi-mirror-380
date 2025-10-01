import asyncio
import sys
import os

# Add the directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.services.email_service import EmailService
from src.templates.email_templates import get_company_addition_template

async def test_company_addition_email():
    company_name = "Acme Corporation"
    inviter_name = "John Smith"
    user_name = "Jane Doe"
    
    # Get the HTML template
    html_content = get_company_addition_template(user_name, company_name, inviter_name)
    
    # Print the result
    print("Subject: You've Been Added to Acme Corporation on ReachGenie")
    print("\n")
    print(html_content)

if __name__ == "__main__":
    asyncio.run(test_company_addition_email()) 