# Bring in deps
import openai
import os 
from apikey import apikey 
os.environ['OPENAI_API_KEY'] = apikey
# Set up your OpenAI API key
openai.api_key = apikey

# Define the student's interest and topic
interest = "Harry Potter"
topic = "Indian prime minister since 1945"

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



# Acronym 1: Generate acronyms on the topic of Indian prime minister since 1945 from using characters or places from Harry Potter.

# 1. PMOI (Prime Minister Of India)
# 2. NMA (Narendra Modi Administration)
# 3. MGN (Manmohan Singh Government)
# 4. JKS (Jawaharlal Nehru Kingdom's Society)
# 5. RCM (Rajiv Gandhi's Council of Ministers)
# 6. AVB (Atal Bihari Vajpayee Bureau)
# 7. IKH (Indira Gandhi's Hogwarts)
# 8. LSF (Lal Bahadur Shastri Foundation)
# 9. JAJ (Jawaharlal Azkaban Jail)
# 10. PDP (P.V. Narsimha Rao's Department of Politics)

