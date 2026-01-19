from langchain.tools import tool
from tools import query_medgemma, call_emergency


@tool
def ask_mental_health_agent(query: str) -> str:
    """
    Uses the AI mental health agent to answer questions related to mental health.
    """
    return query_medgemma(query)
   

@tool
def emergency_call_tool() -> None:
    """
    Place an emergency call to the safety helpline's phone number via Twilio.
    Use this only if the user expresses suicidal ideation, intent to self-harm,
    or describes a mental health emergency requiring immediate help.
    """
    call_emergency()
    
    
    
@tool
def find_nearby_therapists_by_location(location: str) -> str:
    """
    Finds and returns a list of licensed therapists near the specified location.

    Args:
        location (str): The name of the city or area in which the user is seeking therapy support.

    Returns:
        str: A newline-separated string containing therapist names and contact info.
    """
    return (
        f"Here are some therapists near {location}, {location}:\n"
        "- Dr. Ayesha Kapoor - +1 (555) 123-4567\n"
        "- Dr. James Patel - +1 (555) 987-6543\n"
        "- MindCare Counseling Center - +1 (555) 222-3333"
    )


#create an ai agent and link with backend

from langchain_huggingface import ChatHuggingFace

from langchain_community.agents import create_react_agent

from config import HUGGING_FACE_API

llm=ChatHuggingFace(model_name="gpt-4-medgemma", huggingfacehub_api_token=HUGGING_FACE_API, temperature=0.2)
graph=create_react_agent(llm,tool=[ask_mental_health_agent,emergency_call_tool,find_nearby_therapists_by_location],verbose=True)


SYSTEM_PROMPT = """
You are an AI engine supporting mental health conversations with warmth and vigilance.
You have access to three tools:

1. `ask_mental_health_specialist`: Use this tool to answer all emotional or psychological queries with therapeutic guidance.
2. `locate_therapist_tool`: Use this tool if the user asks about nearby therapists or if recommending local professional help would be beneficial.
3. `emergency_call_tool`: Use this immediately if the user expresses suicidal thoughts, self-harm intentions, or is in crisis.

Always take necessary action. Respond kindly, clearly, and supportively.
"""


if __name__ == "__main__":
    while True:
        user_input=input("user:")
        print(f"Input received: {user_input[:200]}...")  # Log first 200 characters of input
        inputs={"message":[{"system":SYSTEM_PROMPT},{"user":user_input}]}
        stream=graph.stream(inputs,stream="update")
        for s in stream:
            print(s)