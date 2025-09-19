import openai
import os

# Load environment variables from .env file (for local development)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, using system environment variables
    pass

# Initialize the OpenAI client with your API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set. Please check your .env file or system environment variables.")

client = openai.OpenAI(api_key=api_key)

# Read job posting and resume from files
with open('job_posting.txt', 'r',) as f:
    job_text = f.read()

with open('resume.txt', 'r') as f:
    ll_text = f.read()

prompt = f"""

Vergleiche den Lebenslauf mit der Jobanzeige:
Jobanzeige:
{job_text}
Lebenslauf:
{ll_text}

Gib eine Bewertung von 1 bis 10, wie gut der Lebenslauf zur Jobanzeige passt. Gib nur die Zahl zurück.

"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)
print(response.choices[0].message.content)