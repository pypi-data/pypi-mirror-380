import asyncio
import json
from typing import Any, Callable

import pytest
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.chat.chat_completion import Choice
from openai.types.completion_usage import (
    CompletionTokensDetails,
    CompletionUsage,
    PromptTokensDetails,
)

from cleanlab_tlm.internal.constants import _TLM_DEFAULT_MODEL
from cleanlab_tlm.internal.types import TLMQualityPreset
from cleanlab_tlm.tlm import TLMScore
from cleanlab_tlm.utils.chat_completions import TLMChatCompletion
from tests.conftest import make_text_unique
from tests.constants import TEST_PROMPT, TEST_RESPONSE
from tests.openai_compat import ChatCompletionMessageToolCall, Function
from tests.test_get_trustworthiness_score import is_trustworthiness_score_json_format

test_prompt = make_text_unique(TEST_PROMPT)
test_response = make_text_unique(TEST_RESPONSE)


def _run_score_sync_or_async(
    tlm_chat: TLMChatCompletion,
    response: ChatCompletion,
    is_async: bool,
    **openai_kwargs: Any,
) -> TLMScore:
    """Runs either sync or async score method based on is_async parameter."""
    if is_async:
        return asyncio.run(tlm_chat.score_async(response=response, **openai_kwargs))
    return tlm_chat.score(response=response, **openai_kwargs)


def test_get_model_name() -> None:
    tlm = TLMChatCompletion()
    model_name = tlm.get_model_name()

    assert model_name == tlm._options["model"]
    assert model_name == _TLM_DEFAULT_MODEL


@pytest.mark.parametrize(
    "quality_preset",
    ["base", "low", "medium", "high", "best"],
)
@pytest.mark.parametrize("is_async", [False, True], ids=["sync", "async"])
def test_tlm_chat_completion_score(quality_preset: TLMQualityPreset, is_async: bool) -> None:
    tlm_chat = TLMChatCompletion(quality_preset=quality_preset)
    openai_kwargs = {
        "model": "gpt-4.1-mini",
        "messages": [{"role": "user", "content": test_prompt}],
    }
    response = ChatCompletion(
        id="test",
        choices=[
            Choice(
                index=0,
                message=ChatCompletionMessage(role="assistant", content=test_response),
                finish_reason="stop",
            )
        ],
        created=1234567890,
        model="test-model",
        object="chat.completion",
    )

    score = _run_score_sync_or_async(tlm_chat, response, is_async, **openai_kwargs)

    assert score is not None
    assert is_trustworthiness_score_json_format(score)


@pytest.mark.parametrize("is_async", [False, True], ids=["sync", "async"])
def test_tlm_chat_completion_score_with_options(is_async: bool) -> None:
    tlm_chat = TLMChatCompletion(options={"log": ["explanation", "perplexity"]})
    openai_kwargs = {
        "model": "gpt-4.1-mini",
        "messages": [{"role": "user", "content": test_prompt}],
    }
    response = ChatCompletion(
        id="test",
        choices=[
            Choice(
                index=0,
                message=ChatCompletionMessage(role="assistant", content=test_response),
                finish_reason="stop",
            )
        ],
        created=1234567890,
        model="test-model",
        object="chat.completion",
    )

    score = _run_score_sync_or_async(tlm_chat, response, is_async, **openai_kwargs)

    assert score is not None
    assert is_trustworthiness_score_json_format(score)


@pytest.mark.parametrize("is_async", [False, True], ids=["sync", "async"])
def test_tlm_chat_completion_score_with_tools(is_async: bool) -> None:
    tlm_chat = TLMChatCompletion()
    openai_kwargs = {
        "model": "gpt-4.1-mini",
        "messages": [{"role": "user", "content": test_prompt}],
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "search",
                    "description": "Search the web for information",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query",
                            }
                        },
                        "required": ["query"],
                    },
                },
            }
        ],
    }
    response = ChatCompletion(
        id="test",
        choices=[
            Choice(
                index=0,
                message=ChatCompletionMessage(role="assistant", content=test_response),
                finish_reason="stop",
            )
        ],
        created=1234567890,
        model="test-model",
        object="chat.completion",
    )

    score = _run_score_sync_or_async(tlm_chat, response, is_async, **openai_kwargs)

    assert score is not None
    assert is_trustworthiness_score_json_format(score)


@pytest.mark.parametrize("is_async", [False, True], ids=["sync", "async"])
def test_tlm_chat_completion_score_with_structured_output(is_async: bool) -> None:
    tlm_chat = TLMChatCompletion()
    openai_kwargs = {
        "model": "gpt-4.1-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
            },
            {"role": "user", "content": "how can I solve 8x + 7 = -23"},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "math_reasoning",
                "schema": {
                    "type": "object",
                    "properties": {
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "explanation": {"type": "string"},
                                    "output": {"type": "string"},
                                },
                                "required": ["explanation", "output"],
                                "additionalProperties": False,
                            },
                        },
                        "final_answer": {"type": "string"},
                    },
                    "required": ["steps", "final_answer"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        },
    }
    response = ChatCompletion(
        id="test",
        choices=[
            Choice(
                index=0,
                message=ChatCompletionMessage(
                    role="assistant",
                    content='{"steps":[{"explanation":"Start with the original equation: 8x + 7 = -23","output":"8x + 7 = -23"},{"explanation":"Subtract 7 from both sides to isolate the term with x on one side. This will give us: 8x = -23 - 7","output":"8x = -30"},{"explanation":"Now simplify the right side: -23 - 7 equals -30, so we have 8x = -30","output":"8x = -30"},{"explanation":"Next, divide both sides by 8 to solve for x. This gives us: x = -30 / 8","output":"x = -3.75"},{"explanation":"We can also simplify -30 / 8 by dividing both the numerator and the denominator by 2. This leads to: x = -15 / 4","output":"x = -15/4 (or -3.75 as a decimal)"}],"final_answer":"x = -15/4 or x = -3.75"}',
                ),
                finish_reason="stop",
            )
        ],
        usage=CompletionUsage(
            completion_tokens=50,
            completion_tokens_details=CompletionTokensDetails(
                accepted_prediction_tokens=0,
                audio_tokens=0,
                reasoning_tokens=0,
                rejected_prediction_tokens=0,
            ),
            prompt_tokens=50,
            prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0),
            total_tokens=100,
        ),
        created=1234567890,
        model="test-model",
        object="chat.completion",
    )

    score = _run_score_sync_or_async(tlm_chat, response, is_async, **openai_kwargs)

    assert score is not None
    assert is_trustworthiness_score_json_format(score)


@pytest.mark.parametrize("is_async", [False, True], ids=["sync", "async"])
def test_tlm_chat_completion_structured_output_per_field_scoring(is_async: bool) -> None:
    tlm_chat = TLMChatCompletion(options={"log": ["per_field_score"]})

    openai_kwargs = {
        "model": "gpt-4.1-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
            },
            {"role": "user", "content": "how can I solve 8x + 7 = -23"},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "math_reasoning",
                "schema": {
                    "type": "object",
                    "properties": {
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "explanation": {"type": "string"},
                                    "output": {"type": "string"},
                                },
                                "required": ["explanation", "output"],
                                "additionalProperties": False,
                            },
                        },
                        "final_answer": {"type": "string"},
                    },
                    "required": ["steps", "final_answer"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        },
    }
    response = ChatCompletion(
        id="test",
        choices=[
            Choice(
                index=0,
                message=ChatCompletionMessage(
                    role="assistant",
                    content='{"steps":[{"explanation":"Start with the original equation: 8x + 7 = -23","output":"8x + 7 = -23"},{"explanation":"Subtract 7 from both sides to isolate the term with x on one side. This will give us: 8x = -23 - 7","output":"8x = -30"},{"explanation":"Now simplify the right side: -23 - 7 equals -30, so we have 8x = -30","output":"8x = -30"},{"explanation":"Next, divide both sides by 8 to solve for x. This gives us: x = -30 / 8","output":"x = -3.75"},{"explanation":"We can also simplify -30 / 8 by dividing both the numerator and the denominator by 2. This leads to: x = -15 / 4","output":"x = -15/4 (or -3.75 as a decimal)"}],"final_answer":"x = -17/4"}',
                ),
                finish_reason="stop",
            )
        ],
        usage=CompletionUsage(
            completion_tokens=50,
            completion_tokens_details=CompletionTokensDetails(
                accepted_prediction_tokens=0,
                audio_tokens=0,
                reasoning_tokens=0,
                rejected_prediction_tokens=0,
            ),
            prompt_tokens=50,
            prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0),
            total_tokens=100,
        ),
        created=1234567890,
        model="test-model",
        object="chat.completion",
    )

    score = _run_score_sync_or_async(tlm_chat, response, is_async, **openai_kwargs)

    assert score is not None
    assert is_trustworthiness_score_json_format(score)

    # test per_field_score
    assert len(score["log"]["per_field_score"]) == 2  # noqa: PLR2004
    assert {"steps", "final_answer"} == set(score["log"]["per_field_score"].keys())
    assert "final_answer" in tlm_chat.get_untrustworthy_fields(response=response, tlm_result=score)


def test_tlm_chat_completion_score_invalid_response() -> None:
    tlm_chat = TLMChatCompletion()
    openai_kwargs = {
        "model": "gpt-4.1-mini",
        "messages": [{"role": "user", "content": test_prompt}],
    }
    invalid_response = {"invalid": "response"}

    with pytest.raises(TypeError, match="The response is not an OpenAI ChatCompletion object."):
        tlm_chat.score(response=invalid_response, **openai_kwargs)  # type: ignore


def test_tlm_chat_completion_score_missing_messages() -> None:
    tlm_chat = TLMChatCompletion()
    openai_kwargs = {
        "model": "gpt-4.1-mini",
        "messages": [{"role": "user", "content": test_prompt}],
    }
    response = ChatCompletion(
        id="test",
        choices=[
            Choice(
                index=0,
                message=ChatCompletionMessage(role="assistant", content=None),
                finish_reason="stop",
            )
        ],
        created=1234567890,
        model="test-model",
        object="chat.completion",
    )

    with pytest.raises(
        ValueError,
        match="The OpenAI ChatCompletion object does not contain a message content or tool calls.",
    ):
        tlm_chat.score(response=response, **openai_kwargs)


@pytest.mark.parametrize(
    "arguments, condition",  # noqa: PT006
    [
        (
            json.dumps({"query": "Capital of Germany"}),
            lambda score: score["trustworthiness_score"] < 0.5,  # noqa: PLR2004
        ),
        (
            json.dumps({"query": "Capital of France"}),
            lambda score: score["trustworthiness_score"] >= 0.8,  # noqa: PLR2004
        ),
    ],
    ids=["bad_arguments", "good_arguments"],
)
@pytest.mark.parametrize("is_async", [False, True], ids=["sync", "async"])
def test_tlm_chat_completion_score_tool_calls(
    arguments: str, condition: Callable[[TLMScore], bool], is_async: bool
) -> None:
    tlm_chat = TLMChatCompletion()

    openai_kwargs = {
        "model": "gpt-4.1-mini",
        "messages": [{"role": "user", "content": "What is the capital of France?"}],
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "search",
                    "description": "Search the web for information",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query",
                            }
                        },
                        "required": ["query"],
                    },
                },
            }
        ],
    }

    response = ChatCompletion(
        id="test",
        choices=[
            Choice(
                index=0,
                message=ChatCompletionMessage(
                    role="assistant",
                    content=None,
                    tool_calls=[
                        ChatCompletionMessageToolCall(
                            id="test",
                            function=Function(name="search", arguments=arguments),
                            type="function",
                        )
                    ],
                ),
                finish_reason="tool_calls",
            )
        ],
        created=1234567890,
        model="test-model",
        object="chat.completion",
    )

    score = _run_score_sync_or_async(tlm_chat, response, is_async, **openai_kwargs)

    assert score is not None
    assert condition(score)
    assert is_trustworthiness_score_json_format(score)
