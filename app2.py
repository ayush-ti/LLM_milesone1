# Bring in deps
import openai
import os 
from apikey import apikey 
os.environ['OPENAI_API_KEY'] = apikey
# Set up your OpenAI API key
openai.api_key = apikey

# Define the student's interest and topic
interest = "Harry Potter"
topic = "countries that share borders with India"

# Define the prompt for acronym generation
prompt = f"Generate acronyms on the topic of {topic} from using characters or places from {interest}."

# Make the API call to generate acronyms
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=500,
    temperature=1,
    n=1,
    stop=None,
    echo=True
)

# Process the response and extract the acronyms
acronyms = [choice['text'].strip() for choice in response.choices]

# Print the generated acronyms
for index, acronym in enumerate(acronyms):
    print(f"Acronym {index + 1}: {acronym}")



# Acronym 1: Generate acronyms on the topic of countries that share borders with India from using characters or places from Harry Potter.

# IWSG: India-Wizarding School of Goa; 
# UBBG: Uttar Pradesh-Beauxbatons Boarder Guard; 
# GBSP: Gujarat-Bicorn and Sphinx Park; 
# GSC: Gringotts-Sikkim Cooperation; 
# NVIK: Nepal-Valley of the Interminable Kingdom; 
# MCPH: Madhya Pradesh-Children's plotting hut; BAIP: Bangladesh-Assam's Allied Potters.

