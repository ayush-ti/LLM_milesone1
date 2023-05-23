# Bring in deps
import openai
import os 
from apikey import apikey 
os.environ['OPENAI_API_KEY'] = apikey
# Set up your OpenAI API key
openai.api_key = apikey

# Define the student's interest and topic
interest = "Harry Potter"
topic = "first 20 elements of the periodic table"

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




# interest = "Harry Potter"
# topic = "first 20 elements of the periodic table"


# Acronym 1: Generate acronyms on the topic of first 20 elements of the periodic table from using characters or places from Harry Potter.

# 1. Hg = Hogwarts Gold
# 2. He = Hog's Head Express
# 3. Li = Lockhart's Law
# 6. C - Cedric's Carbon
# 7. N - Neville's Nitrogen
# 8. O - Order Of The Phoenix Oxygen
# 9. F - Flitwick's Fluorine
# 10. Ne - Nagini's Neon
# 11. Na - Neville's Sodium
# 12. Mg - Malfoy Manor's Magnesium
# 13. Al - Albus' Aluminum
# 14. Si - Sirius' Silicon
# 15. P - Potter's Phosphorus
# 16. S - Slytherin's Sulfur
# 17. Cl - Crabbe's Chlorine
# 18. Ar - Aragog's Argon
# 19. K - Dumbledore's Potassium
# 20. Ca - Chamber of Secrets' Calcium