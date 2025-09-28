class BasePrompt:
    """Base class for prompts."""

    def __init__(self) -> None:
        pass

    def to_markdown(self) -> str:
        """Convert the prompt to a markdown string."""
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self) -> str:
        return self.to_markdown()

    def to_text(self) -> str:
        """Convert the prompt to a plain text string."""
        raise NotImplementedError("Subclasses must implement this method.")

    def to_dict(self) -> dict:
        """Convert the prompt to a dictionary."""
        raise NotImplementedError("Subclasses must implement this method.")

    def to_message_chain(self) -> list[dict[str, str]]:
        """Convert the prompt to a message chain."""
        raise NotImplementedError("Subclasses must implement this method.")
