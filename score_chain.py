from langchain_openai import ChatOpenAI
from prompts.score_prompt import score_prompt

def get_score_chain(llm=None):
    if llm is None:
        llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    return score_prompt | llm