from chat.completions import ChatCompletions, AsyncChatCompletions


class Chat:
    """Chat resource for CheckThat AI - provides access to chat completions."""

    def __init__(self, client):
        self.completions = ChatCompletions(client)


class AsyncChat:
    """Async Chat resource for CheckThat AI - provides async access to chat completions."""

    def __init__(self, client):
        self.completions = AsyncChatCompletions(client)
