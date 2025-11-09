# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Start coding here
# Add as many cells as you like
conversation=[
    {"role": "system","content": "Parisian expert, delivering valuable insights into the city's iconic landmarks and hidden treasures.user friendly"}
]         
user_msgs = [ "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
            ]
# Loop over the user questions
for q in user_msgs:
    print("User: ", q)   
     # Create a dictionary for the user message from q and append to conversation
    user_dict = {"role": "user", "content": q}    
    conversation.append(user_dict)  
    # Create the API request
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=conversation,  
      max_completion_tokens=100,
      temperature=0.0
)  
# Append the assistant's converstion to messages
    assistant_dict = {"role": "assistant", "content": response.choices[0].message.content}
    conversation.append(assistant_dict)
    print("Assistant: ", response.choices[0].message.content, "\n")
