import os
from openai import OpenAI
from src.commons.utils import get_server_logger
from src.core.guardrails import get_guardrail_handler
from src.core.function_calling import (
    stellarIntentConfig,
    stellarIntentHandler,
    stellarFunctionConfig,
    stellarFunctionHandler,
)


# Define logger
logger = get_server_logger()


# Define the client
stellar_ENDPOINT = os.getenv("stellar_ENDPOINT", "https://api.fc.stellar.com/v1")
stellar_API_KEY = "EMPTY"
stellar_CLIENT = OpenAI(base_url=stellar_ENDPOINT, api_key=stellar_API_KEY)

# Define model names
stellar_INTENT_MODEL_ALIAS = "stellar-Intent"
stellar_FUNCTION_MODEL_ALIAS = "stellar-Function"
stellar_GUARD_MODEL_ALIAS = "stellarlaboratory/stellar-Guard"

# Define model handlers
handler_map = {
    "stellar-Intent": stellarIntentHandler(
        stellar_CLIENT, stellar_INTENT_MODEL_ALIAS, stellarIntentConfig
    ),
    "stellar-Function": stellarFunctionHandler(
        stellar_CLIENT, stellar_FUNCTION_MODEL_ALIAS, stellarFunctionConfig
    ),
    "stellar-Guard": get_guardrail_handler(stellar_GUARD_MODEL_ALIAS),
}
