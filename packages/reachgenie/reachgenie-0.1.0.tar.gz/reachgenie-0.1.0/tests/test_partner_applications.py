#!/usr/bin/env python3
import os
import requests
import json
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8001")

def test_submit_partner_application():
    """
    Test the partner application submission endpoint
    """
    url = f"{API_BASE_URL}/api/partner-applications"
    
    # Test data for partner application
    payload = {
        "company_name": "Coeus Solutions ",
        "contact_name": "Ali Shaheen",
        "contact_email": "ashaheen@workhub.ai",
        "contact_phone": "+1-555-123-4567",
        "website": "https://www.coeus-solutions.com",
        "partnership_type": "RESELLER",
        "company_size": "11-50",
        "industry": "Technology",
        "current_solutions": "Currently using multiple CRM tools",
        "target_market": "SMB technology companies",
        "motivation": "Looking to expand product offerings for our clients",
        "additional_information": "We have a team of 5 sales reps"
    }
    
    try:
        # Make the POST request
        response = requests.post(url, json=payload)
        
        # Print the response
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {response.text}")
        
        # Check if the request was successful
        if response.status_code == 201:
            response_data = response.json()
            logger.info(f"Application submitted successfully! ID: {response_data.get('id')}")
            return response_data
        else:
            logger.error(f"Failed to submit application: {response.text}")
            return None
    except Exception as e:
        logger.error(f"Error submitting partner application: {str(e)}")
        return None

def test_get_partner_applications(auth_token):
    """
    Test the endpoint to list partner applications (admin only)
    """
    url = f"{API_BASE_URL}/api/admin/partner-applications"
    
    try:
        # Make the GET request with authentication
        response = requests.get(
            url, 
            headers={"Authorization": f"Bearer {auth_token}"}
        )
        
        # Print the response
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {json.dumps(response.json(), indent=2)}")
        
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        logger.error(f"Error getting partner applications: {str(e)}")
        return None

def test_get_partner_application_statistics(auth_token):
    """
    Test the endpoint to get partner application statistics (admin only)
    """
    url = f"{API_BASE_URL}/api/admin/partner-applications/statistics"
    
    try:
        # Make the GET request with authentication
        response = requests.get(
            url, 
            headers={"Authorization": f"Bearer {auth_token}"}
        )
        
        # Print the response
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response body: {json.dumps(response.json(), indent=2)}")
        
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        logger.error(f"Error getting partner application statistics: {str(e)}")
        return None

def get_auth_token():
    """
    Get authentication token for admin endpoints
    """
    url = f"{API_BASE_URL}/api/auth/login"
    
    # Get credentials from environment
    email = os.getenv("TEST_ADMIN_EMAIL")
    password = os.getenv("TEST_ADMIN_PASSWORD")
    
    if not email or not password:
        logger.error("Test admin credentials not found in environment variables")
        return None
    
    try:
        # Make the login request
        response = requests.post(
            url, 
            data={"username": email, "password": password}
        )
        
        if response.status_code == 200:
            token_data = response.json()
            return token_data.get("access_token")
        else:
            logger.error(f"Failed to get auth token: {response.text}")
            return None
    except Exception as e:
        logger.error(f"Error getting auth token: {str(e)}")
        return None

if __name__ == "__main__":
    # Test partner application submission (public endpoint)
    application = test_submit_partner_application()
    
    # If you want to test admin endpoints, uncomment these:
    # token = get_auth_token()
    # if token:
    #     applications = test_get_partner_applications(token)
    #     stats = test_get_partner_application_statistics(token) 