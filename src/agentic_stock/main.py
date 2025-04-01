import os
from dotenv import load_dotenv
import panel as pn

load_dotenv()

pn.extension(design="material")

from crew import AgenticStock
from crew import chat_interface
import threading

from crewai.agents.agent_builder.base_agent_executor_mixin import CrewAgentExecutorMixin
import time

def custom_ask_human_input(self, message: str) -> str:
    global user_input
    
    # Send the agent's message to the chat interface
    chat_interface.send(message, user="Agent", respond=False)
    
    prompt = "Please provide your input: "
    chat_interface.send(prompt, user="System", respond=False)
    
    while user_input == None:
        time.sleep(1)
    
    human_comments = user_input
    user_input = None
    
    return human_comments

# Override both methods to capture all agent interactions
CrewAgentExecutorMixin._ask_human_input = custom_ask_human_input
CrewAgentExecutorMixin.ask_human = custom_ask_human_input

user_input = None
crew_started = False

def initiate_chat(message):
    global crew_started
    crew_started = True
    
    try:
        # Initialize crew with inputs
        inputs = {"Stock": message}
        crew = AgenticStock().crew()
        
        # Run the crew
        result = crew.kickoff(inputs=inputs)
        
        # Send final results back to chat
        chat_interface.send(result, user="Assistant", respond=False)
        
        # Send restart message
        chat_interface.send(
            "Type '/restart' to analyze another stock or continue with follow-up questions.",
            user="System",
            respond=False
        )
    except Exception as e:
        chat_interface.send(f"An error occurred: {e}", user="Assistant", respond=False)
    crew_started = False

def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    global crew_started
    global user_input

    if contents.lower().strip() == "/restart":
        crew_started = False
        chat_interface.send(
            "Welcome back! What Stock would you like me to research?",
            user="Assistant",
            respond=False
        )
        return

    if not crew_started:
        thread = threading.Thread(target=initiate_chat, args=(contents,))
        thread.start()
    else:
        user_input = contents

chat_interface.callback = callback 

# Send welcome message
chat_interface.send(
    "Welcome! I'm your AI Stock Research Assistant. What Stock would you like me to research?\n\nType '/restart' at any time to start a new analysis.",
    user="Assistant",
    respond=False
)

# Make it servable
chat_interface.servable()