"""Prompt system for Marvin.

This module provides a flexible prompt system that supports:
1. Prompts defined as strings or paths to template files
2. Static type checking of prompt variables
3. Dynamic prompt creation from function docstrings and signatures
4. Serialization of prompts and their required attributes
"""

import inspect
import re
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, get_type_hints

from marvin.engine.llm import (
    AgentMessage,
    PydanticAIMessage,
    SystemMessage,
    UserMessage,
)
from marvin.utilities.jinja import jinja_env


@dataclass(kw_only=True)
class Template:
    """A template for generating prompts.

    Args:
        source: Either a string template or a Path to a template file

    """

    _dataclass_config = {"kw_only": True}

    source: str | Path

    def render(self, **kwargs: Any) -> str:
        """Render the template with variables."""
        render_kwargs = {
            k: v
            for k, v in self.__dict__.items()
            if k not in ["source", "_dataclass_config"]
        }

        if isinstance(self.source, Path):
            template = jinja_env.get_template(str(self.source))
        else:
            template = jinja_env.from_string(self.source)

        return template.render(**render_kwargs | kwargs)


@dataclass
class Prompt:
    """Base class for prompts.

    Prompts can be defined either as strings or paths to template files.
    Additional attributes can be added by subclassing and will be type-checked.
    """

    source: str | Path = field(
        metadata={
            "description": "The template source - either a string template or path to template file",
        },
    )
    _extra_fields: dict[str, Any] = field(default_factory=dict, repr=False)

    def __post_init__(self):
        if not self.source:
            raise ValueError("source must be provided")

    def __setattr__(self, name: str, value: Any) -> None:
        if name in ["source", "_extra_fields"]:
            super().__setattr__(name, value)
        else:
            self._extra_fields[name] = value

    def __getattr__(self, name: str) -> Any:
        if name in self._extra_fields:
            return self._extra_fields[name]
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{name}'")

    def _render_template(self, **kwargs: Any) -> str:
        """Render the template with variables."""
        # Get all fields except source
        render_kwargs = {
            **self._extra_fields,
        }

        template = Template(source=self.source)
        return template.render(**render_kwargs | kwargs)

    def _parse_messages(self, text: str) -> list[PydanticAIMessage]:
        """Parse text into messages with roles.

        The text can contain role markers in the format "ROLE:" or "role:".
        Supported roles are: system, user, assistant
        If no role is specified, defaults to user.

        Example:
            SYSTEM: You are a helpful assistant.
            USER: Hi!
            ASSISTANT: Hello! How can I help you?

        """
        # Split on role markers, keeping the marker
        pattern = re.compile(
            r"^(SYSTEM:|USER:|ASSISTANT:|system:|user:|assistant:)\s*",
            re.MULTILINE,
        )

        # Split text into chunks at role markers
        chunks: list[tuple[str, str]] = []
        last_end = 0

        for match in pattern.finditer(text):
            # If there's text before this marker, it's content without a role
            if match.start() > last_end:
                chunks.append(("user", text[last_end : match.start()].strip()))

            # Get the role from the marker
            role = match.group(1).lower().rstrip(":")

            # Find the end of this chunk (next role marker or end of text)
            next_match = pattern.search(text, match.end())
            end = next_match.start() if next_match else len(text)

            # Add the chunk with its role
            content = text[match.end() : end].strip()
            if content:
                chunks.append((role, content))

            last_end = end

        # If there's remaining text, treat it as user message
        if last_end < len(text):
            content = text[last_end:].strip()
            if content:
                chunks.append(("user", content))

        # Convert role/content pairs to appropriate Message types
        messages: list[PydanticAIMessage] = []
        for role, content in chunks:
            if role == "system":
                messages.append(SystemMessage(content))
            elif role == "user":
                messages.append(UserMessage(content))
            elif role == "assistant":
                messages.append(AgentMessage(content))
        return messages

    def to_messages(self, **kwargs: Any) -> list[PydanticAIMessage]:
        """Convert the prompt to a list of messages with roles.

        The template can contain role markers (SYSTEM:, USER:, ASSISTANT:) to
        indicate message roles. Text without a role marker is treated as a user
        message.

        Example template:
            '''
            SYSTEM: You are a helpful assistant.
            USER: Hi {{ name }}!
            ASSISTANT: Hello {{ name }}! How can I help you?
            '''
        """
        # First render the template
        text = self._render_template(**kwargs)

        # Then parse into messages
        return self._parse_messages(text)

    @classmethod
    def from_fn(cls, fn: Callable[..., Any]) -> type["Prompt"]:
        """Create a Prompt class from a function's docstring and signature.

        Args:
            fn: The function to create a prompt from. The function's docstring will
                be used as the template, and its signature will define the required
                attributes.

        Example:
            def greet(name: str, age: int):
                '''
                SYSTEM: You are a friendly assistant.
                USER: Hi {{ name }}, how old are you?
                ASSISTANT: I'm an AI, but you're {{ age }} years old!
                '''
                pass

            GreetPrompt = Prompt.from_fn(greet)
            prompt = GreetPrompt(name="Alice", age=30)
            messages = prompt.to_messages()

        """
        # Get function signature and docstring
        sig = inspect.signature(fn)
        hints = get_type_hints(fn)
        _template = inspect.getdoc(fn)
        if not _template:
            raise ValueError(f"Function {fn.__name__} must have a docstring")

        # Create the dynamic prompt class
        @dataclass
        class DynamicPrompt(cls):
            source: str | Path = field(default=_template)
            __qualname__ = f"{fn.__name__.title()}Prompt"  # Set the class name

            # Add the function parameters as fields
            for name, param in sig.parameters.items():
                default = param.default if param.default is not param.empty else None
                locals()[name] = field(
                    default=default,
                    metadata={"description": f"Parameter from function {fn.__name__}"},
                )
                if name in hints:
                    __annotations__[name] = hints[name]

        return DynamicPrompt
