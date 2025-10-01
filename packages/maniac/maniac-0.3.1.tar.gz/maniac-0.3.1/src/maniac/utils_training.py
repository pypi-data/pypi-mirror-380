from __future__ import annotations

from typing import Any, Dict, List, Tuple

from .types import (
    ChatMessage,
    ConvertedDatapoint,
    ManiacRequestError,
    RawCompletionDatapoint,
)


EXPECTED_FORMAT = (
    """
Expected dataset format:
[
  {
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is the capital of France?"},
      {"role": "assistant", "content": "Paris is the capital of France."}
    ],
    "metadata": { "domain": "geography" }
  },
  {
    "messages": [
      {"role": "user", "content": "What is 2+2?"},
      {"role": "assistant", "content": "4."}
    ]
  }
]

Supported message roles: system, user, assistant.
Each datapoint must have a non-empty "messages" array that ends with an "assistant" message.
Each message must include "role" and "content" (both strings).
"""
).strip()


def _assert_string(x: Any, label: str) -> None:
    if not isinstance(x, str):
        raise ManiacRequestError("validation_error", f"{label} must be a string")


def validate_and_convert_dataset(
    dataset: List[RawCompletionDatapoint],
) -> Tuple[List[ConvertedDatapoint], str | None]:
    if not isinstance(dataset, list) or len(dataset) == 0:
        raise ManiacRequestError("validation_error", "Cannot register empty dataset.")

    converted: List[ConvertedDatapoint] = []
    inferred_system_prompt: str | None = None
    seen_system_prompt: str | None = None
    saw_any_system = False

    for i, datapoint in enumerate(dataset):
        if not isinstance(datapoint, dict):
            raise ManiacRequestError(
                "validation_error",
                f"Datapoint at index {i} is not an object. Found: {type(datapoint).__name__}\n\n{EXPECTED_FORMAT}",
            )

        messages = datapoint.get("messages")
        if not isinstance(messages, list):
            raise ManiacRequestError(
                "validation_error",
                f'Datapoint at index {i} missing a "messages" array.\n\n{EXPECTED_FORMAT}',
            )
        if len(messages) == 0:
            raise ManiacRequestError(
                "validation_error",
                f"Messages list at index {i} is empty.\n\n{EXPECTED_FORMAT}",
            )

        for j, m in enumerate(messages):
            if not isinstance(m, dict):
                raise ManiacRequestError(
                    "validation_error",
                    f"Message {j} in datapoint {i} is not an object. Found: {type(m).__name__}\n\n{EXPECTED_FORMAT}",
                )
            if "role" not in m:
                raise ManiacRequestError(
                    "validation_error",
                    f'Message {j} in datapoint {i} missing "role" key.\n\n{EXPECTED_FORMAT}',
                )
            if "content" not in m:
                raise ManiacRequestError(
                    "validation_error",
                    f'Message {j} in datapoint {i} missing "content" key.\n\n{EXPECTED_FORMAT}',
                )

            _assert_string(m.get("role"), f"role in message {j} of datapoint {i}")
            _assert_string(m.get("content"), f"content in message {j} of datapoint {i}")

            if m["role"] not in ("system", "user", "assistant", "tool"):
                raise ManiacRequestError(
                    "validation_error",
                    f"Invalid role \"{m['role']}\" in message {j} of datapoint {i}. Supported roles: system, user, assistant.\n\n{EXPECTED_FORMAT}",
                )

        last = messages[-1]
        if last["role"] != "assistant":
            raise ManiacRequestError(
                "validation_error",
                f'Last message in datapoint {i} must be from "assistant".\n\n{EXPECTED_FORMAT}',
            )

        if messages[0].get("role") == "system":
            saw_any_system = True
            s = messages[0]["content"]
            if seen_system_prompt is None:
                seen_system_prompt = s
            elif seen_system_prompt != s:
                seen_system_prompt = None

        input_messages: List[ChatMessage] = messages[:-1]
        output_message: str = last["content"]

        extras: Dict[str, Any] = {k: v for k, v in datapoint.items() if k != "messages"}

        converted_datapoint: ConvertedDatapoint = {
            "input": input_messages,
            "output": output_message,
            "system_prompt": messages[0]["content"]
            if messages[0].get("role") == "system"
            else None,
        }
        if len(extras):
            converted_datapoint["additional_parameters"] = extras

        converted.append(converted_datapoint)

    inferred_system_prompt = seen_system_prompt if saw_any_system else None
    return converted, inferred_system_prompt
