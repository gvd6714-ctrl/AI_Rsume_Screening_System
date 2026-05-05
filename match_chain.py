from langchain_openai import ChatOpenAI
from prompts.match_prompt import match_prompt

def get_match_chain(llm=None):
    if llm is None:
        llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    return match_prompt | llm