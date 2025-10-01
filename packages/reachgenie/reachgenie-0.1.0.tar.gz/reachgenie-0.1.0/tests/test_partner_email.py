#!/usr/bin/env python3
import os
import sys
import asyncio
import logging
import json
from dotenv import load_dotenv
from uuid import uuid4

# Add the parent directory to the path so Python can find the src module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.partner_application_service import PartnerApplicationService
from src.services.perplexity_service import perplexity_service

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Set more verbose logging for the perplexity service
perplexity_logger = logging.getLogger('src.services.perplexity_service')
perplexity_logger.setLevel(logging.DEBUG)

# Load environment variables
load_dotenv()

async def test_company_info_fetch():
    """Test just the company info fetching"""
    company_name = "Coeus Solutions"
    website = "https://www.coeus-solutions.com"
    
    logger.info(f"Testing company info fetch for {company_name} ({website})")
    
    try:
        # Try direct fetch_company_info first
        logger.info("Trying fetch_company_info...")
        company_info = await perplexity_service.fetch_company_info(website)
        
        if company_info:
            logger.info("✅ Successfully fetched company info")
            logger.info(f"Company info: {json.dumps(company_info, indent=2)}")
        else:
            logger.warning("⚠️ fetch_company_info returned None")
            
            # Try get_company_insights as fallback
            logger.info("Trying get_company_insights...")
            insights = await perplexity_service.get_company_insights(
                company_name=company_name,
                company_website=website,
                company_description="IT company offering software development services"
            )
            
            if insights:
                logger.info("✅ Successfully got company insights")
                logger.info(f"Insights: {insights}")
            else:
                logger.error("❌ Both perplexity methods failed")
    except Exception as e:
        logger.error(f"Error testing company info fetch: {str(e)}")
        logger.exception(e)

async def test_partner_application_email():
    """
    Test the complete partner application email flow
    This includes:
    1. Company research via Perplexity API
    2. Personalized email generation via GPT-4o-mini with sales tips
    3. Email sending via Mailjet with specific sender and CC
    4. Nicely formatted HTML email with proper styling
    """
    # Test application data - using real values from your log
    test_application_data = {
        "id": str(uuid4()),
        "company_name": "zenloop",
        "contact_name": "Ali Shaheen",  # This is a full name
        "contact_email": "ali.shaheen@zenloop.com",  # Set this in your .env
        "website": "https://www.zenloop.com", 
        "partnership_type": "RESELLER",
        "company_size": "201-500",
        "industry": "Technology",
        "motivation": "Looking to sell to our ecommerce clients."
    }
    
    # Extract first name for testing
    first_name = test_application_data["contact_name"].split()[0]
    logger.info(f"Full name: {test_application_data['contact_name']} → First name: {first_name}")
    
    logger.info("=" * 80)
    logger.info(f"PERPLEXITY_API_KEY set: {'✅ YES' if os.getenv('PERPLEXITY_API_KEY') else '❌ NO'}")
    logger.info(f"OPENAI_API_KEY set: {'✅ YES' if os.getenv('OPENAI_API_KEY') else '❌ NO'}")
    logger.info(f"TEST_EMAIL set: {'✅ YES' if os.getenv('TEST_EMAIL') else '❌ NO'}")
    logger.info(f"MAILJET keys set: {'✅ YES' if os.getenv('MAILJET_API_KEY') and os.getenv('MAILJET_API_SECRET') else '❌ NO'}")
    logger.info("=" * 80)
    
    try:
        # First test just the company info fetching to isolate Perplexity issues
        await test_company_info_fetch()
        
        # Initialize the partner application service
        logger.info("Initializing PartnerApplicationService...")
        partner_service = PartnerApplicationService()
        
        # First, just generate the email content without sending (to check content)
        logger.info(f"Generating personalized email for {test_application_data['company_name']}...")
        email_content = await partner_service.generate_confirmation_email(test_application_data)
        
        logger.info(f"Email content generated with subject: {email_content['subject']}")
        logger.info("Email preview:")
        logger.info("-" * 80)
        logger.info(f"Subject: {email_content['subject']}")
        body_preview = email_content['body'][:500] + "..." if len(email_content['body']) > 500 else email_content['body']
        logger.info(f"Body: {body_preview}")
        logger.info("-" * 80)
        
        # Save the generated email to a file for manual review
        with open("partner_email_test_output.html", "w") as f:
            f.write(f"Subject: {email_content['subject']}\n\n")
            f.write(email_content["body"])
            logger.info("Email content saved to partner_email_test_output.html")
        
        # Now test the actual sending functionality using Mailjet
        if test_application_data["contact_email"]:
            logger.info(f"Sending email to {test_application_data['contact_email']} using Mailjet...")
            logger.info(f"From: Qudsia Piracha <qudsia@workhub.ai> with CC to ashaheen@workhub.ai")
            
            # Use the new method that handles both generation and sending
            success = await partner_service.send_confirmation_email(test_application_data)
            
            if success:
                logger.info(f"✅ Successfully sent email to {test_application_data['contact_email']}")
            else:
                logger.error(f"❌ Failed to send email to {test_application_data['contact_email']}")
        else:
            logger.info("No recipient email specified. Email not sent.")
            
    except Exception as e:
        logger.error(f"Error in partner application email test: {str(e)}")
        logger.exception(e)

if __name__ == "__main__":
    asyncio.run(test_partner_application_email()) 