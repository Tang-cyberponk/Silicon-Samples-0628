# Step 1: Configure the API and file paths

# Import the tools required for subsequent API calls and data processing
import os                  # Handle file paths and environment variables
import pandas as pd        # Process tabular data, including Excel files
from openai import OpenAI  # Create the large language model API client


# ============================================================
# 1. API and input/output file configuration
# ============================================================

MODEL = "deepseek-v4-flash"  # Name of the large language model to be used
TEMPERATURE = 1.0            # Controls the randomness and diversity of responses
ENCODING = "utf-8-sig"       # File encoding

# Use the folder in which the current script is executed as the base directory
# for locating input and output files
BASE_DIR = os.getcwd()

# Input file: original human-sample data
# The file name may be changed as needed
INPUT_FILE = os.path.join(BASE_DIR, "human_sample_data.xlsx")

# Output file: generated silicon-sample data
# The file name may be changed as needed
LLM_OUTPUT_FILE = os.path.join(BASE_DIR, "silicon_sample_data.xlsx")

# The API key serves as the credential for accessing the model API.
API_KEY = "Enter your API key here"

# Create the API client
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com",  # API endpoint
)
```
