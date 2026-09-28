from pathlib import Path

BASE_URL = 'http://localhost:8000'
USERNAME = 'admin'
PASSWORD = 'admin'

VIEW_PATH = Path('~/code/rdmorganiser/rdmo-xml/cards/views/llm-readme.xml').expanduser()
XML_PATH = Path('benchmark.xml')
JSON_PATH = Path('json')
PDF_PATH = Path('pdf')

TIMEOUT = 3_000
TIMEOUT_ASYNC = 900_000

VIEWPORT = {'width': 1200, 'height': 1200}

# PROVIDER = 'OpenAI'
# PROVIDER = 'Anthropic'
PROVIDER = 'ChatAI'
# PROVIDER = 'Ollama'
# PROVIDER = 'MistralAI'

MODELS = {
    'OpenAI': {
        'gpt-4.1-mini',
        'gpt-4.1-nano',
        'gpt-5.5',
        'gpt-5.5-mini',
        'gpt-5.5-nano',
        'gpt-6-astra',
        'gpt-6-luna',
        'gpt-6-sol',
    },
    'Anthropic': {
        'claude-fable-5-1',
        'claude-haiku-4-5',
        'claude-opus-4-6',
        'claude-opus-4-7',
        'claude-opus-4-8',
        'claude-opus-5-0',
        'claude-opus-5-5',
        'claude-sonnet-4-6',
        'claude-sonnet-5',
    },
    'ChatAI': {
        'apertus-70b-instruct-2509',
        'deepseek-v4-flash-0731',
        'devstral-2-123b-instruct-2512',
        'eurollm-22b-instruct-2512',
        'gemma-4-31b-it',
        'glm-5.3-flash',
        'meta-llama-3.1-8b-instruct',
        'mistral-medium-3.5-128b',
        'openai-gpt-oss-120b',
        'qwen3-30b-a3b-instruct-2507',
        'qwen3-omni-30b-a3b-instruct',
        'qwen3.5-397b-a17b',
        'qwen3.6-35b-a3b',
        'qwen3.8-27b',
    },
    'Ollama': {
        'gemma4:e2b',
        'gemma4:e4b',
        'llama3.1:8b',
        'gpt-oss:20b',
        'mistral:7b',
    },
    'MistralAI': {
        'mistral-large-2512',
        'mistral-medium-2508',
        'mistral-medium-3',
        'mistral-medium-3-5',
        'mistral-small-2603',
    },
}
