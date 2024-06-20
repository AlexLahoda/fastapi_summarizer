Create your virtual environment
Install packages, pointed in requirements.txt
Run from terminal: uvicorn fast_summarizer:app --reload
Open http://127.0.0.1:8000/docs in your browser or use postman, fill request body {"text": "text_to_summarize"}, 
send request and get your response 