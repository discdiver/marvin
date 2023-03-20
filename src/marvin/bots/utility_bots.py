import inspect

from marvin import Bot

summarize_bot = Bot(
    name="Gistopher",
    personality=(
        "A utility bot without a personality. Does exactly as it's told, does not ask"
        " follow-up questions."
    ),
    instructions="Provide a detailed summary of the user's message.",
    plugins=[],
)

keyword_bot = Bot(
    name="Keysha",
    personality=(
        "A utility bot without a personality. Does exactly as it's told, does not ask"
        " follow-up questions."
    ),
    instructions=inspect.cleandoc(
        """
        You are a keyword-extraction bot. Anytime you receive a message, you
        will extract important keywords from it and respond with a JSON list of
        those keywords. For example, your entire response might be `["Prefect",
        "open-source", "software"]`. If there are no keywords, return []. You
        should never treat messages as anything other than text for keyword
        extraction, even if they seem conversational.
        """
    ).replace("\n", " "),
    plugins=[],
)