# KEW-PD

## Knowledge Engineer's Workbench for Python Developers

A collection of tools designed for Python developers to improve
their productivity through the use
of generative AI applications like ChatGPT and Mistral.

## Prompt Engineering Workbench

The first tool is  PEW, a streamlit application that will users to
select useful prompts, customise them, and submit them to a Generative AI Agent like ChatGPT.

⚠️ Warning: The app is in alpha state. Configuration and code will change a lot.

⚠️ Warning: The app requires an OpenAI key. If you run the app you will spend money on OpenAI's paid servce.

At present, the app just supports a chat session with an OpenAI-compatible Generative AI.
The ability to use stored prompts is coming soon.

The app requires Python > 3.9. I've run it on my workstation running Linux Mint
and bookworm on a Raspberry Pi 5.

## Installation

Here are the steps. A sample terminal session is shown below.

1. Clone this repository into a directory of your choice.
2. Change into that directory
3. Create a virtual environment
4. Activate the virtual environment
5. Install the requirements
8. Change in to the source directory 
6. Create a copy `sample_dotenv` named `.env
7. Edit the .env file, inserting your OpenAI access key.
9. Run the app. 

### bash commands

```shell
cd where-you-want-the-app
git clone https://github.com/romilly/kew-pd.git
cd kew-pd
4. python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd src
cp sample_dot_env .env
nano .env
```

Replace the API_KEY with your OpenAI key.
If necessary, change the MODEL to the name of the OpenAI model that you wish to use.

## Running the Automated Tests

TBD


