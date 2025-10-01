import asyncio
import sys
import os
import logging
import uuid
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add the directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.services.email_service import EmailService
from src.services.company_personalization_service import CompanyPersonalizationService
from src.database import get_company_by_id

async def test_specific_invite_email():
    """Test the personalized company invite email for a specific company and user"""
    # Company and user details
    company_id = "51ecaaa5-04ae-4405-a732-b3c7f9be5eff"
    recipient_name = "Ali Shaheen"
    recipient_email = "ashaheen@workhub.ai"
    inviter_name = "Test User"
    
    # Create a fake invite token
    invite_token = f"test-token-{datetime.now().timestamp()}"
    invite_link = f"https://reachgenie.leanai.ventures/invite?token={invite_token}"
    
    logger.info(f"Testing personalized invite email for {recipient_name} ({recipient_email})")
    
    try:
        # Get company details
        company = await get_company_by_id(uuid.UUID(company_id))
        if not company:
            logger.error(f"Company with ID {company_id} not found")
            return
            
        company_name = company["name"]
        logger.info(f"Found company: {company_name}")
        
        # Create personalization service
        personalization_service = CompanyPersonalizationService()
        
        # Get company information (using name and website if available)
        logger.info(f"Getting company information for {company_name}")
        company_info = await personalization_service.get_company_info(
            company_name=company_name,
            website=company.get("website")
        )
        logger.info(f"Company info obtained")
        
        # Generate value proposition
        logger.info("Generating personalized value proposition")
        value_proposition = await personalization_service.generate_personalized_value_proposition(company_info)
        logger.info(f"Value proposition generated: {len(value_proposition)} characters")
        
        # Generate engagement tips
        logger.info("Generating personalized engagement tips")
        engagement_tips = await personalization_service.generate_engagement_tips(company_info)
        logger.info(f"Generated {len(engagement_tips)} engagement tips")
        
        # Use the template directly to generate the HTML content
        from src.templates.email_templates import get_invite_template
        html_content = get_invite_template(
            company_name=company_name,
            invite_link=invite_link,
            inviter_name=inviter_name,
            recipient_name=recipient_name,
            value_proposition=value_proposition,
            engagement_tips=engagement_tips
        )
        
        # Save the result to a file
        output_file = f"personalized_invite_email_{company_name.replace(' ', '_')}.html"
        with open(output_file, "w") as f:
            f.write(f"Subject: Invitation to join {company_name} on ReachGenie\n\n")
            f.write("To: " + recipient_email + "\n\n")
            f.write(html_content)
        
        logger.info(f"Invite email preview saved to {output_file}")
        logger.info("To view the HTML file, open it in a web browser")
        
        # Actually send the email
        logger.info(f"Sending real email to {recipient_email}...")
        email_service = EmailService()
        response = await email_service.send_email(
            to_email=recipient_email,
            subject=f"Invitation to join {company_name} on ReachGenie",
            html_content=html_content
        )
        
        logger.info(f"Email sent successfully! Response status: {response.get('status', 'unknown')}")
        
    except Exception as e:
        logger.error(f"Error testing invite email: {str(e)}")
        logger.exception(e)

if __name__ == "__main__":
    asyncio.run(test_specific_invite_email()) 