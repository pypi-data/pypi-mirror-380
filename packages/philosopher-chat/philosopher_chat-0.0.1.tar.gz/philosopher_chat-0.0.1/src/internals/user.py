from typing import Optional

from internals.chat import Chat
from internals.message import Message
from internals.status import Status


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.chats: dict[str, Chat] = {}
        self.selected_chat: Optional[Chat] = None

    def new_chat(self, chat_name: str, philosopher: str) -> Status:
        if self._find_chat(chat_name):
            return Status.BAD_REQUEST

        new_chat = Chat(chat_name, philosopher)
        self.chats[chat_name] = new_chat
        return Status.SUCCESS

    def select_chat(self, chat_name: str) -> tuple[Status, list[Message]]:
        chat = self._find_chat(chat_name)
        if not chat:
            return Status.NOT_FOUND, []

        self.selected_chat = chat
        return Status.SUCCESS, self.selected_chat.get_history()

    def exit_chat(self) -> Status:
        if not self.selected_chat:
            return Status.BAD_REQUEST

        self.selected_chat = None
        return Status.SUCCESS

    def delete_chat(self, chat_name: str) -> Status:
        chat = self._find_chat(chat_name)
        if not chat:
            return Status.NOT_FOUND

        if self.selected_chat == chat:
            self.selected_chat = None

        del self.chats[chat_name]
        return Status.SUCCESS

    def complete_chat(
        self, input_text: str, prompt_loader, chat_completer
    ) -> tuple[Status, Message, Message]:
        if not self.selected_chat:
            return Status.BAD_REQUEST

        return self.selected_chat.complete_chat(
            input_text, self.username, prompt_loader, chat_completer
        )

    def _find_chat(self, chat_name: str) -> Optional[Chat]:
        return self.chats.get(chat_name)
