import os

DEVICE = os.getenv('DEVICE', default='cpu')
LLM_PORT = int(os.getenv('LLM_PORT', default=8001))

