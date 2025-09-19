import openai
import os

# Initialize the OpenAI client with your API key
client = openai.OpenAI(
    api_key="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"
)

job_text = """



"""

ll_text = """


"""

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