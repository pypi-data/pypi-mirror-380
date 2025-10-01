from openai import AsyncOpenAI
import asyncio
import os

async def test_openai():
    try:
        client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        print('Making API call...')
        response = await client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'user', 'content': 'Say hello'}]
        )
        print('Success! Response:', response.choices[0].message.content)
    except Exception as e:
        print('Error type:', type(e).__name__)
        print('Error:', str(e))
        if hasattr(e, 'response'):
            print('Response status:', e.response.status_code if hasattr(e.response, 'status_code') else 'N/A')
            print('Response body:', e.response.text if hasattr(e.response, 'text') else 'N/A')

if __name__ == '__main__':
    asyncio.run(test_openai()) 