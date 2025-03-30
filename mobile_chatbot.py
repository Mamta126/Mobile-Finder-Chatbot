import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
serpapi_api_key = os.getenv("SERPAPI_API_KEY")

# Streamlit UI Title
st.title("📱 Mobile Finder Chatbot")

# Check if API keys are available
if not openai_api_key or not serpapi_api_key:
    st.error("❌ Please set your OpenAI and SerpAPI keys in the environment variables.")
    st.stop()

# Initialize OpenAI model
llm = ChatOpenAI(temperature=0.5, model_name="gpt-4", openai_api_key=openai_api_key)

# SerpAPI tool for searching latest mobiles
search = SerpAPIWrapper(serpapi_api_key=serpapi_api_key)
tools = [
    Tool(
        name="Search Mobile Phones",
        func=search.run,
        description="Search for the latest mobile phones, including brands, models, features, and pricing."
    )
]

# Memory for conversation history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize LangChain agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)

def get_phone_details(user_query):
    """Fetch phone details dynamically based on user query."""
    
    try:
        raw_response = search.run(user_query)  # Directly search with user query
    except ValueError as e:
        return f"❌ SerpAPI Error: {str(e)}"

    # Format the response using OpenAI to structure details
    formatted_prompt = f"""
    You are a mobile tech expert. Summarize and enhance the following raw search results.
    
    **Guidelines:**
    - Extract details like display, camera, processor, and battery.
    - Include price and purchase links if available.
    - Format response in a neat bullet-point format.

    **Raw Data:**
    {raw_response}
    """
    
    formatted_response = llm.predict(formatted_prompt)
    return formatted_response

# Streamlit UI Input
user_query = st.text_input("🔍 Ask about any phone (e.g., 'Latest Samsung phones', 'iPhone 15 specs'):")

if st.button("Find Mobile"):
    with st.spinner("Fetching details..."):
        phone_details = get_phone_details(user_query)
        st.markdown(phone_details)
