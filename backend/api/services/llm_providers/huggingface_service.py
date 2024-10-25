# backend/api/services/llm_providers/huggingface_service.py

from langchain_huggingface import HuggingFaceEndpoint
import os

def get_huggingface_llm():
    huggingfacehub_api_token = os.getenv('HUGGINGFACE_API_KEY')
    return HuggingFaceEndpoint(
        repo_id='tiiuae/falcon-7b-instruct',
        huggingfacehub_api_token=huggingfacehub_api_token
    )
