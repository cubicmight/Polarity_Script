import openai
import argparse

# Set up OpenAI API credentials
openai.api_key = "put a key here"

# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--polarity", required=True, type=int, help="The political polarity value (-10 to 10)")
parser.add_argument("--keywords", required=True, type=str, help="Keywords for generating the political argument")
args = parser.parse_args()

# Define the model and parameters
model_engine = "EleutherAI/gpt-neo-2.7B"
temperature = 0.7
max_tokens = 256

# Generate the political argument
prompt = f"Generate a statement given a political polarity value (-10 is extremely liberal and positive 10 is " \
         f"extremely conservative) and keywords. Use rhetoric from the speeches in this dataset: " \
         f"https://data.stanford.edu/congress_text. The political polarity is {args.polarity} and the keywords are {args.keywords}."
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].text)
