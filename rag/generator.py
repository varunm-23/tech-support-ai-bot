import time
import requests

from config import API_URL, DEEPINFRA_API_KEY, MODEL_NAME
from rag.prompt import SYSTEM_PROMPT


class LLMGenerator:

    def generate(self, question, context):

        documentation = "\n\n".join(context)

        headers = {
            "Authorization": f"Bearer {DEEPINFRA_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": f"""
Use ONLY the documentation below.

Documentation:
{documentation}

Question:
{question}
"""
                }
            ],
            "temperature": 0,
            "max_tokens": 512
        }

        start = time.time()

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        latency = round(time.time() - start, 2)

        # Helpful error if API fails
        if response.status_code != 200:
            raise Exception(
                f"API Error {response.status_code}: {response.text}"
            )

        result = response.json()

        answer = result["choices"][0]["message"]["content"]

        return answer, latency



















# import time
# import requests

# from config import API_URL
# from config import DEEPINFRA_API_KEY
# from config import MODEL_NAME

# from rag.prompt import SYSTEM_PROMPT


# class LLMGenerator:

#     def generate(self, question, context):

#         headers = {
#             "Authorization": f"Bearer {DEEPINFRA_API_KEY}",
#             "Content-Type": "application/json"
#         }

#         prompt = "\n\n".join(context)

#         payload = {
#             "model": MODEL_NAME,
#             "messages": [
#                 {
#                     "role": "system",
#                     "content": SYSTEM_PROMPT
#                 },
#                 {
#                     "role": "user",
#                     "content":
#                         f"""Documentation:

# {prompt}

# Question:

# {question}
# """
#                 }
#             ],
#             "temperature": 0
#         }

#         start = time.time()

#         response = requests.post(
#             API_URL,
#             headers=headers,
#             json=payload,
#             timeout=60
#         )

#         latency = round(time.time() - start, 2)

#         response.raise_for_status()

#         answer = response.json()["choices"][0]["message"]["content"]

#         return answer, latency