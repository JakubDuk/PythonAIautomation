# PythonAIautomation
Python Script using OpenAI to generate Python automation scripts.

The script needs to be run with 2 arguments and an environment variable called OPENAI_API_KEY containing your API key.

1. Set the environment variable. For example in powershell run:
$Env:OPENAI_API_KEY = "your unick API Key"

2. Run the script using a prompt and file name arguments. For example in powershell run:
python3.10.exe .\pythongpt.py "print todays date" "date.py"

In this case, we are asking for python script that will print today's date and will be saved in to date.py file.

THING TO REMEMBER.
Some scripts generated will require libraries to be installed.
Some longer scripts might require biger token value.
You can change the response by changing the value of temperature, where 0 is "predictable" and 1 is "abstract".
Some scripts might have some leftovers of AI's Explenanion text at the beginning of the script. You might need to delete them.
Responses heavily depend on the prompt value, so some of them will be rubbish and some will need some changes to work correctly.
Experiment with OpenAI endpoint, model and prompt (line22) for different use cases.

HAVE FUN!
