from typing import List
import os

API_ID: int = os.environ.get("API_ID")
API_HASH: str = os.environ.get("API_HASH")
TOKEN: str = os.environ.get("TOKEN")

log_chat: int = os.environ.get("log_chat")
sub_chat: str = os.environ.get("sub_chat")
sudoers: List[int] = os.environ.get("sudoers")
prefixs: List[str] = ["/", "!", ".", "$", "-"]

# notes

# 1. api_id & api_hash get from my.telegram.org
# 2. token fill with your bot_token get from @BotFather
# 3. log_chat fill with the chat id of a group that you should create for the bot logger
# 4. sub_chat fill with the channel username but don't include the '@' symbol
