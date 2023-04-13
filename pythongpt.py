import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to create")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
#Set your environment variable. Name= OPENAI_API_KEY ; value= your api key
#It depends on terminal session, example for powershell:
#$Env:OPENAI_API_KEY = "YOUR API KEY"
api_key = os.getenv("OPENAI_API_KEY") 
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data ={
    "model": "text-davinci-003",
    "prompt": f"Write python script to {args.prompt}",
    "max_tokens": 500,
    "temperature": 0
}

responce = requests.post(api_endpoint, headers=request_headers, json=request_data)

if responce.status_code == 200:
    responce_text = responce.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(responce_text)
else:
    print(f"Request failed with status code: {str(responce.status_code)}")