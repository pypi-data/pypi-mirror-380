from openai import OpenAI

from utils.globals import BASE_URL, API_KEY, MODEL_NAME
from internals.message import Message


class ChatCompleter:
    def __init__(self):
        self.client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

    def msg_to_dict(self, msg: Message) -> dict[str, str]:
        return {"role": msg.role, "content": msg.content}

    def complete_chat(self, messages: list[Message]) -> str:
        completion_messages = [self.msg_to_dict(msg) for msg in messages]

        completion = self.client.chat.completions.create(
            model=MODEL_NAME, messages=completion_messages
        )
        return completion.choices[0].message.content.strip()
