import os
from config import AZURE_OPENAI_ENDPOINT
from azure.ai.agents import AgentsClient
from azure.identity import DefaultAzureCredential

print("Endpoint:", AZURE_OPENAI_ENDPOINT)
try:
    agents_client = AgentsClient(
        endpoint=AZURE_OPENAI_ENDPOINT,
        credential=DefaultAzureCredential()
    )
    print("AgentsClient initialized successfully!")
    print("Methods available:", [m for m in dir(agents_client) if not m.startswith('_')])
except Exception as e:
    print("Error initializing AgentsClient:", e)
