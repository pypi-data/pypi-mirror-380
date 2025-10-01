from typing import Optional

from internals.chat_completer import ChatCompleter
from internals.prompt_loader import PromptLoader
from internals.user import User
from internals.message import Message
from internals.status import Status


class System:
    def __init__(self):
        self.prompt_loader = PromptLoader()
        self.chat_completer = ChatCompleter()
        self.users: dict[str, User] = {}
        self.philosophers: list[str] = []
        self.logged_in_user: Optional[User] = None

    def signup(self, username: str, password: str) -> Status:
        if self.logged_in_user:
            return Status.PERMISSION_DENIED
        elif self._find_user(username):
            return Status.BAD_REQUEST

        new_user = User(username, password)
        self.users[username] = new_user
        return Status.SUCCESS

    def login(self, username: str, password: str) -> Status:
        user = self._find_user(username)

        if self.logged_in_user:
            return Status.PERMISSION_DENIED
        elif not user:
            return Status.NOT_FOUND
        elif user.password != password:
            return Status.PERMISSION_DENIED

        self.logged_in_user = user
        return Status.SUCCESS

    def logout(self) -> Status:
        if not self.logged_in_user:
            return Status.PERMISSION_DENIED

        self.logged_in_user = None
        return Status.SUCCESS

    def new_chat(self, chat_name: str, philosopher: str) -> Status:
        if not self.logged_in_user:
            return Status.BAD_REQUEST

        return self.logged_in_user.new_chat(chat_name, philosopher)

    def select_chat(self, chat_name: str) -> tuple[Status, list[Message]]:
        if not self.logged_in_user:
            return Status.BAD_REQUEST

        return self.logged_in_user.select_chat(chat_name)

    def exit_chat(self) -> Status:
        if not self.logged_in_user:
            return Status.BAD_REQUEST

        return self.logged_in_user.exit_chat()

    def delete_chat(self, chat_name: str) -> Status:
        if not self.logged_in_user:
            return Status.BAD_REQUEST

        return self.logged_in_user.delete_chat(chat_name)

    def complete_chat(self, input_text: str) -> tuple[Status, Message, Message]:
        if not self.logged_in_user:
            return Status.BAD_REQUEST

        return self.logged_in_user.complete_chat(
            input_text, self.prompt_loader, self.chat_completer
        )

    def _find_user(self, username: str) -> Optional[User]:
        return self.users.get(username)
