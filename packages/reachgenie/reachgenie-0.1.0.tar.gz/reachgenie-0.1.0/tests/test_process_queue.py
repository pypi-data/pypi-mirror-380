#!/usr/bin/env python3
import asyncio
import logging
from src.scripts.process_email_queues import main

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("email_queue_test")

if __name__ == "__main__":
    logger.info("Starting email queue processing test (without cronlock)")
    asyncio.run(main())
    logger.info("Email queue processing completed") 