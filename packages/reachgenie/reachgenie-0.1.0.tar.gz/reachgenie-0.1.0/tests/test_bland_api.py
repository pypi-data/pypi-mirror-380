import asyncio
import httpx
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_bland_api():
    # Load environment variables
    load_dotenv()
    
    # Get credentials from environment
    api_key = os.getenv("BLAND_API_KEY")
    secret_key = os.getenv("BLAND_SECRET_KEY")
    tool_id = os.getenv("BLAND_TOOL_ID")
    webhook_url = os.getenv("WEBHOOK_BASE_URL", "https://outbound-ai-sdr-imgd.onrender.com")
    
    # Log configuration
    logger.info(f"API Key exists: {bool(api_key)}")
    if api_key:
        logger.info(f"API Key starts with: {api_key[:8]}...")
    
    logger.info(f"Secret Key exists: {bool(secret_key)}")
    if secret_key:
        logger.info(f"Secret Key starts with: {secret_key[:8]}...")
    
    logger.info(f"Tool ID exists: {bool(tool_id)}")
    if tool_id:
        logger.info(f"Tool ID: {tool_id}")
    
    # Prepare the request payload
    script = """
    You are Alex, an AI sales representative for XYZ Company. 
    This is a test call to verify the API is working correctly.
    Please identify yourself as a test call and hang up quickly.
    """
    
    phone_number = "+4915151633365"  # Replace with a valid test phone number
    
    request_data = {
        "bland_secret_key": secret_key,
        "company_uuid": "test-company-uuid",
        "call_log_id": "test-call-log-id"
    }
    
    payload = {
        "phone_number": phone_number,
        "task": script,
        "voice": "Florian",
        "language": "en",
        "background_track": "none",
        "temperature": 0.7,
        "model": "enhanced",
        "tools": [tool_id] if tool_id else [], 
        "request_data": request_data,
        "webhook": f"{webhook_url}/api/calls/webhook",
        "analysis_prompt": "Determine if this was a test call (yes/no)",
        "analysis_schema": {
            "test_call": "string"
        },
        "record": True,
        "dry_run": True  # Set to True to test the API without making an actual call
    }
    
    logger.info(f"Request payload (redacted): {payload}")
    
    # Make the API call
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://api.bland.ai/v1/calls",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json=payload,
                timeout=30.0
            )
            
            logger.info(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                logger.info(f"Success! Result: {result}")
                return result
            else:
                logger.error(f"API Error: {response.text}")
                return None
                
        except Exception as e:
            logger.error(f"Exception: {str(e)}")
            return None

if __name__ == "__main__":
    asyncio.run(test_bland_api()) 