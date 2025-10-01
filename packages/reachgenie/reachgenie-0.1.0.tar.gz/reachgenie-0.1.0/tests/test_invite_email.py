import asyncio
import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add the directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.services.email_service import EmailService
from src.services.company_personalization_service import CompanyPersonalizationService

async def test_invite_email():
    """Test the personalized company invite email"""
    invite_link = "https://reachgenie.leanai.ventures/invite?token=test-token-12345"
    company_name = "Coeus Solutions"
    inviter_name = "John Smith"
    recipient_name = "Jane Doe"
    
    logger.info(f"Testing personalized invite email for {recipient_name} from {inviter_name} at {company_name}")
    
    try:
        # Create personalization service
        personalization_service = CompanyPersonalizationService()
        
        # Get company information
        logger.info(f"Getting company information for {company_name}")
        company_info = await personalization_service.get_company_info(company_name)
        logger.info(f"Company info: {company_info}")
        
        # Generate value proposition
        logger.info("Generating personalized value proposition")
        value_proposition = await personalization_service.generate_personalized_value_proposition(company_info)
        logger.info(f"Value proposition generated: {len(value_proposition)} characters")
        
        # Generate engagement tips
        logger.info("Generating personalized engagement tips")
        engagement_tips = await personalization_service.generate_engagement_tips(company_info)
        logger.info(f"Generated {len(engagement_tips)} engagement tips")
        
        # Create the email service
        email_service = EmailService()
        
        # Use the template directly to avoid sending an actual email
        from src.templates.email_templates import get_invite_template
        html_content = get_invite_template(
            company_name=company_name,
            invite_link=invite_link,
            inviter_name=inviter_name,
            recipient_name=recipient_name,
            value_proposition=value_proposition,
            engagement_tips=engagement_tips
        )
        
        # Print the result
        print("Subject: Invitation to join Acme Corporation on ReachGenie")
        print("\n")
        print(html_content)
        
        # Save the result to a file
        with open("personalized_invite_email_preview.html", "w") as f:
            f.write(f"Subject: Invitation to join {company_name} on ReachGenie\n\n")
            f.write(html_content)
        
        logger.info("Invite email preview saved to personalized_invite_email_preview.html")
        
    except Exception as e:
        logger.error(f"Error testing invite email: {str(e)}")
        logger.exception(e)

if __name__ == "__main__":
    asyncio.run(test_invite_email()) 