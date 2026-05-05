from langchain_openai import ChatOpenAI
from prompts.extract_prompt import extract_prompt

def get_extract_chain(llm=None):
    if llm is None:
        llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    return extract_prompt | llm