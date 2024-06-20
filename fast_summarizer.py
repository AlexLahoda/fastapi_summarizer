from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


OPEN_API_KEY = 'KEY'
prompt_template = """Write a concise summary of the following:


{text}


CONSCISE SUMMARY IN THE ORIGIN LANGUAGE: """


prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

app = FastAPI()
llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct", api_key= OPEN_API_KEY)

chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt, verbose=True)

class SummarizeRequest(BaseModel):
    text: str


@app.post("/summarize")
async def summarize(request: SummarizeRequest):
    text = request.text
    if not text:
        return {"error": "No text"}
    document = Document(page_content=text)
    result = chain.invoke({'input_documents': [document]})['output_text']

    return {"summary": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)