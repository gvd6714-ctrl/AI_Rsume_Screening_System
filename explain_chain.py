from langchain_openai import ChatOpenAI
from prompts.explain_prompt import explain_prompt

def get_explain_chain(llm=None):
    if llm is None:
        llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    return explain_prompt | llm