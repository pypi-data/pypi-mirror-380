from __future__ import annotations

import os
import warnings
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Callable, Optional, Union, cast

from cleanlab_tlm.errors import ValidationError
from cleanlab_tlm.internal.constants import (
    _HIDDEN_REASONING_MODELS,
    _QUALITY_PRESETS_UNSUPPORTED_EXPLANATION_LOGGING,
    _QUALITY_PRESETS_W_CONSISTENCY_SAMPLES,
    _REASONING_EFFORT_UNSUPPORTED_EXPLANATION_LOGGING,
    _TLM_CONSTRAIN_OUTPUTS_KEY,
    _TLM_DEFAULT_MODEL,
    _TLM_MAX_TOKEN_RANGE,
    _VALID_TLM_MODELS,
    INVALID_SCORE_OPTIONS,
    TLM_NUM_CANDIDATE_RESPONSES_RANGE,
    TLM_NUM_CONSISTENCY_SAMPLES_RANGE,
    TLM_NUM_SELF_REFLECTIONS_RANGE,
    TLM_REASONING_EFFORT_VALUES,
    TLM_SIMILARITY_MEASURES,
    TLM_TASK_SUPPORTING_CONSTRAIN_OUTPUTS,
    TLM_VALID_GET_TRUSTWORTHINESS_SCORE_KWARGS,
    TLM_VALID_LOG_OPTIONS,
    TLM_VALID_PROMPT_KWARGS,
    VALID_RESPONSE_OPTIONS,
)
from cleanlab_tlm.internal.types import Task

if TYPE_CHECKING:
    from cleanlab_tlm.tlm import TLMOptions, TLMResponse, TLMScore
    from cleanlab_tlm.utils.rag import Eval, TrustworthyRAGResponse, TrustworthyRAGScore

SKIP_VALIDATE_TLM_OPTIONS: bool = os.environ.get("CLEANLAB_TLM_SKIP_VALIDATE_TLM_OPTIONS", "false").lower() == "true"


def validate_tlm_prompt(prompt: Union[str, Sequence[str]]) -> None:
    if isinstance(prompt, str):
        return

    if isinstance(prompt, Sequence) and any(not isinstance(p, str) for p in prompt):
        raise ValidationError(
            "Some items in prompt are of invalid types, all items in the prompt list must be of type str."
        )


def validate_tlm_prompt_response(prompt: Union[str, Sequence[str]], response: Union[str, Sequence[str]]) -> None:
    if isinstance(prompt, str):
        if not isinstance(response, str):
            raise ValidationError(
                "response type must match prompt type. "
                f"prompt was provided as str but response is of type {type(response)}"
            )

    elif isinstance(prompt, Sequence):
        # str is considered a Sequence, we want to explicitly check that response is not a string
        if not isinstance(response, Sequence) or isinstance(response, str):
            raise ValidationError(
                "response type must match prompt type. "
                f"prompt was provided as type {type(prompt)} but response is of type {type(response)}"
            )

        if len(prompt) != len(response):
            raise ValidationError("Length of the prompt and response lists must match.")

        if any(not isinstance(p, str) for p in prompt):
            raise ValidationError(
                "Some items in prompt are of invalid types, all items in the prompt list must be of type str."
            )
        if any(not isinstance(r, str) for r in response):
            raise ValidationError(
                "Some items in response are of invalid types, all items in the response list must be of type str."
            )


def validate_tlm_options(
    options: Any,
    support_custom_eval_criteria: bool = True,
    allow_custom_model: bool = False,
    valid_keys: Optional[set[str]] = None,
) -> None:
    if SKIP_VALIDATE_TLM_OPTIONS:
        return

    if not isinstance(options, dict):
        raise ValidationError(
            "options must be a TLMOptions object.\n"
            "See: https://help.cleanlab.ai/reference/python/tlm/#class-tlmoptions"
        )

    if valid_keys is None:
        # fallback to default TLM behavior if no valid_keys provided
        from cleanlab_tlm.tlm import TLMOptions

        valid_keys = set(TLMOptions.__annotations__.keys())

    invalid_keys = set(options.keys()) - valid_keys
    if invalid_keys:
        raise ValidationError(
            f"Invalid keys in options dictionary: {invalid_keys}.\n"
            "See https://help.cleanlab.ai/reference/python/tlm/#class-tlmoptions for valid options"
        )

    for option, val in options.items():
        if option == "max_tokens":
            if not isinstance(val, int):
                raise ValidationError(f"Invalid type {type(val)}, max_tokens must be an integer")

            model = options.get("model", _TLM_DEFAULT_MODEL)
            max_tokens_range = _TLM_MAX_TOKEN_RANGE.get(model, _TLM_MAX_TOKEN_RANGE["default"])
            if val < max_tokens_range[0] or val > max_tokens_range[1]:
                raise ValidationError(
                    f"Invalid value {val}, max_tokens for {model} must be in the range {max_tokens_range}"
                )

        elif option == "model":
            if not allow_custom_model and val not in _VALID_TLM_MODELS:
                raise ValidationError(f"{val} is not a supported model, valid models include: {_VALID_TLM_MODELS}")

        elif option == "num_candidate_responses":
            if not isinstance(val, int):
                raise ValidationError(f"Invalid type {type(val)}, num_candidate_responses must be an integer")

            if val < TLM_NUM_CANDIDATE_RESPONSES_RANGE[0] or val > TLM_NUM_CANDIDATE_RESPONSES_RANGE[1]:
                raise ValidationError(
                    f"Invalid value {val}, num_candidate_responses must be in the range {TLM_NUM_CANDIDATE_RESPONSES_RANGE}"
                )

        elif option == "num_consistency_samples":
            if not isinstance(val, int):
                raise ValidationError(f"Invalid type {type(val)}, num_consistency_samples must be an integer")

            if val < TLM_NUM_CONSISTENCY_SAMPLES_RANGE[0] or val > TLM_NUM_CONSISTENCY_SAMPLES_RANGE[1]:
                raise ValidationError(
                    f"Invalid value {val}, num_consistency_samples must be in the range {TLM_NUM_CONSISTENCY_SAMPLES_RANGE}"
                )

        elif option == "num_self_reflections":
            if not isinstance(val, int):
                raise ValidationError(f"Invalid type {type(val)}, num_self_reflections must be an integer")

            if val < TLM_NUM_SELF_REFLECTIONS_RANGE[0] or val > TLM_NUM_SELF_REFLECTIONS_RANGE[1]:
                raise ValidationError(
                    f"Invalid value {val}, num_self_reflections must be in the range {TLM_NUM_SELF_REFLECTIONS_RANGE}"
                )

        elif option == "use_self_reflection":
            if "num_self_reflections" in options:
                raise ValidationError(
                    "`use_self_reflection` and `num_self_reflections` cannot be specified together. "
                    "`use_self_reflection` is deprecated. Use `num_self_reflections` instead."
                )

            if not isinstance(val, bool):
                raise ValidationError(f"Invalid type {type(val)}, use_self_reflection must be a boolean")

            warnings.warn(
                "Deprecated method. Use `num_self_reflections` instead.",
                DeprecationWarning,
                stacklevel=2,
            )

        elif option == "similarity_measure":
            if val not in TLM_SIMILARITY_MEASURES:
                raise ValidationError(
                    f"Invalid value for similarity_measure: {val}, valid measures include: {TLM_SIMILARITY_MEASURES}"
                )

        elif option == "reasoning_effort":
            if val not in TLM_REASONING_EFFORT_VALUES:
                raise ValidationError(
                    f"Invalid value {val}, reasoning_effort must be one of {TLM_REASONING_EFFORT_VALUES}"
                )

        elif option == "log":
            if not isinstance(val, list):
                raise ValidationError(f"Invalid type {type(val)}, log must be a list of strings.")

            invalid_log_options = set(val) - TLM_VALID_LOG_OPTIONS
            if invalid_log_options:
                raise ValidationError(
                    f"Invalid options for log: {invalid_log_options}. Valid options include: {TLM_VALID_LOG_OPTIONS}"
                )

        elif option == "custom_eval_criteria":
            if not support_custom_eval_criteria:
                raise ValidationError("custom_eval_criteria is not supported for this class")

            if not isinstance(val, list):
                raise ValidationError(f"Invalid type {type(val)}, custom_eval_criteria must be a list of dictionaries.")

            supported_keys = {"name", "criteria"}

            for i, criteria in enumerate(val):
                if not isinstance(criteria, dict):
                    raise ValidationError(f"Item {i} in custom_eval_criteria is not a dictionary.")

                input_keys = set(criteria.keys())
                if input_keys != supported_keys:
                    missing = supported_keys - input_keys
                    extra = input_keys - supported_keys
                    if missing:
                        raise ValidationError(f"Missing required keys {missing} in custom_eval_criteria item {i}.")
                    if extra:
                        raise ValidationError(
                            f"Invalid keys {extra} found in custom_eval_criteria item {i}. Supported keys are: {supported_keys}."
                        )

                if not isinstance(criteria.get("name"), str):
                    raise ValidationError(f"'name' in custom_eval_criteria item {i} must be a string.")

                if not isinstance(criteria.get("criteria"), str):
                    raise ValidationError(f"'criteria' in custom_eval_criteria item {i} must be a string.")

        elif option == "disable_trustworthiness":
            if not isinstance(val, bool):
                raise ValidationError(f"Invalid type {type(val)}, disable_trustworthiness must be a boolean")
            if val and support_custom_eval_criteria and not options.get("custom_eval_criteria"):
                raise ValidationError("disable_trustworthiness is only supported when custom_eval_criteria is provided")

        elif option == "disable_persistence":
            if not isinstance(val, bool):
                raise ValidationError(f"Invalid type {type(val)}, disable_persistence must be a boolean")

        elif option == "model_provider":
            if not isinstance(val, dict):
                raise ValidationError(f"Invalid type {type(val)}, model_provider must be a dictionary")

            from cleanlab_tlm.utils.vpc.tlm import ModelProvider

            supported_model_provider_keys = set(ModelProvider.__annotations__.keys())

            invalid_keys = set(val.keys()) - supported_model_provider_keys
            if invalid_keys:
                raise ValidationError(
                    f"Invalid keys in model_provider: {invalid_keys}. Valid keys include: {supported_model_provider_keys}"
                )


def _validate_trustworthy_rag_options(options: Optional[TLMOptions], initialized_evals: list[Eval]) -> None:
    """To be used for ensuring TLMOptions are set correctly given other parameters to TrustworthyRAG

    options: TLMOptions
    initialized_evals: list[Eval]
        The evals field configured in TrustworthyRAG.__init__. Required to validate disable_trustworthiness option.
    """
    disable_trustworthiness = options and options.get("disable_trustworthiness", False)

    if disable_trustworthiness and not initialized_evals:
        raise ValidationError(
            "When disable_trustworthiness=True in TrustworthyRAG, at least one evaluation must be provided. "
            "Either provide evaluations via the 'evals' parameter or set disable_trustworthiness=False."
        )


def validate_logging(options: Optional[TLMOptions], quality_preset: str, subclass: str) -> None:
    """If user asks to log explanation, then either:
    ensure the specified TLM configuration supports this (return early), or otherwise raise informative error.

    subclass: str
        Either "TLM" or "TrustworthyRAG".
        Indicates which type of TLM subclass object we are validating, different types have different quality_preset -> base options mappings.
    """
    if not options:
        return
    if "log" not in options:
        return
    if "explanation" not in options["log"]:
        return

    # Otherwise ensure we're using TLM configuration that supports logging explanations:
    unsupported_error = ValueError(
        "Your TLM configuration does not support logged explanations.  "
        "Please remove 'explanation' from your specified `log`, and instead use the `get_explanation()` method after computing trust scores."
    )

    disable_trustworthiness = options.get("disable_trustworthiness", False)
    if disable_trustworthiness:
        raise unsupported_error

    model = options.get("model")
    num_consistency_samples = options.get("num_consistency_samples")
    reasoning_effort = options.get("reasoning_effort")

    num_self_reflections = options.get("num_self_reflections")
    use_self_reflection = options.get("use_self_reflection")
    if use_self_reflection is False:
        # use_self_reflection is deprecated, consolidating to one parameter
        num_self_reflections = 0

    if num_consistency_samples == 0 and num_self_reflections == 0:
        raise unsupported_error

    if (num_consistency_samples is not None) and (num_consistency_samples > 0):
        return
    if (
        (reasoning_effort is not None)
        and (reasoning_effort not in _REASONING_EFFORT_UNSUPPORTED_EXPLANATION_LOGGING)
        and (num_self_reflections is None or num_self_reflections > 0)
    ):
        return
    if (num_consistency_samples == 0) and (reasoning_effort in _REASONING_EFFORT_UNSUPPORTED_EXPLANATION_LOGGING):
        raise unsupported_error

    if model in _HIDDEN_REASONING_MODELS:
        raise unsupported_error

    # Otherwise we can assume relevant TLMOptions were left unspecified by user
    if subclass == "TLM":
        if quality_preset in _QUALITY_PRESETS_UNSUPPORTED_EXPLANATION_LOGGING:
            raise unsupported_error
        if quality_preset not in _QUALITY_PRESETS_W_CONSISTENCY_SAMPLES:
            if reasoning_effort in _REASONING_EFFORT_UNSUPPORTED_EXPLANATION_LOGGING:
                raise unsupported_error
            if num_self_reflections == 0 and num_consistency_samples is None:
                raise unsupported_error

    if subclass == "TrustworthyRAG":
        if quality_preset not in _QUALITY_PRESETS_W_CONSISTENCY_SAMPLES:
            raise unsupported_error
        if num_consistency_samples == 0:
            raise unsupported_error


def process_and_validate_kwargs_constrain_outputs(
    prompt: Union[str, Sequence[str]],
    task: Optional[Task],
    kwargs_dict: dict[str, Any],
    response: Optional[Union[str, Sequence[str]]] = None,
) -> None:
    constrain_outputs = kwargs_dict.get(_TLM_CONSTRAIN_OUTPUTS_KEY)
    if constrain_outputs is None:
        if task == Task.CLASSIFICATION:
            raise ValidationError("constrain_outputs must be provided for classification tasks")

        return

    if task not in TLM_TASK_SUPPORTING_CONSTRAIN_OUTPUTS:
        raise ValidationError("constrain_outputs is only supported for classification tasks")

    if isinstance(prompt, str):
        if not isinstance(constrain_outputs, list) or not all(isinstance(s, str) for s in constrain_outputs):
            raise ValidationError("constrain_outputs must be a list of strings")
    elif isinstance(prompt, Sequence):
        if not isinstance(constrain_outputs, list):
            raise ValidationError("constrain_outputs must be a list")

        # If it's a list of strings, repeat the list for each prompt
        if all(isinstance(co, str) for co in constrain_outputs):
            constrain_outputs = [constrain_outputs] * len(prompt)
        # Check if it's a list of lists of strings
        elif all(isinstance(co, list) and all(isinstance(s, str) for s in co) for co in constrain_outputs):
            pass
        else:
            raise ValidationError("constrain_outputs must be a list of strings or a list of lists of strings")

        if len(constrain_outputs) != len(prompt):
            raise ValidationError("constrain_outputs must have same length as prompt")

    # Check each response is one of its allowed constraint outputs
    if response is not None:
        if isinstance(response, str):
            if response not in constrain_outputs:
                raise ValidationError(
                    f"Response '{response}' must be one of the constraint outputs: {constrain_outputs}"
                )
        else:
            for i, (resp, constraints) in enumerate(zip(response, constrain_outputs)):
                if constraints is not None and resp not in constraints:
                    raise ValidationError(
                        f"Response '{resp}' at index {i} must be one of the constraint outputs: {constraints}"
                    )

    kwargs_dict[_TLM_CONSTRAIN_OUTPUTS_KEY] = constrain_outputs


def tlm_prompt_process_and_validate_kwargs(
    prompt: Union[str, Sequence[str]],
    task: Task,
    kwargs_dict: dict[str, Any],
) -> None:
    if not SKIP_VALIDATE_TLM_OPTIONS:
        supported_kwargs = TLM_VALID_PROMPT_KWARGS
        unsupported_kwargs = set(kwargs_dict.keys()) - supported_kwargs
        if unsupported_kwargs:
            raise ValidationError(
                f"Unsupported keyword arguments: {unsupported_kwargs}. "
                f"Supported keyword arguments are: {supported_kwargs}"
            )

    process_and_validate_kwargs_constrain_outputs(prompt=prompt, task=task, kwargs_dict=kwargs_dict)


def tlm_score_process_response_and_kwargs(
    prompt: Union[str, Sequence[str]],
    response: Union[str, Sequence[str]],
    task: Optional[Task],
    kwargs_dict: dict[str, Any],
) -> Union[dict[str, Any], list[dict[str, Any]]]:
    process_and_validate_kwargs_constrain_outputs(prompt=prompt, task=task, kwargs_dict=kwargs_dict, response=response)

    if not SKIP_VALIDATE_TLM_OPTIONS:
        invalid_kwargs = set(kwargs_dict.keys()) - TLM_VALID_GET_TRUSTWORTHINESS_SCORE_KWARGS
        if invalid_kwargs:
            raise ValidationError(
                f"Invalid kwargs provided: {invalid_kwargs}. Valid kwargs include: {TLM_VALID_LOG_OPTIONS}"
            )
        # checking validity/format of each input kwarg, each one might require a different format
        for key, val in kwargs_dict.items():
            if key == "perplexity":
                if isinstance(response, str):
                    if not (isinstance(val, (float, int))):
                        raise ValidationError(
                            f"Invalid type {type(val)}, perplexity should be a float when response is a str."
                        )
                    if val is not None and not 0 <= val <= 1:
                        raise ValidationError("Perplexity values must be between 0 and 1")
                elif isinstance(response, Sequence):
                    if not isinstance(val, Sequence):
                        raise ValidationError(
                            f"Invalid type {type(val)}, perplexity should be a sequence when response is a sequence"
                        )
                    if len(response) != len(val):
                        raise ValidationError("Length of the response and perplexity lists must match.")
                    for v in val:
                        if not (isinstance(v, (float, int))):
                            raise ValidationError(f"Invalid type {type(v)}, perplexity values must be a float")
                        if v is not None and not 0 <= v <= 1:
                            raise ValidationError("Perplexity values must be between 0 and 1")
                else:
                    raise ValidationError(f"Invalid type {type(response)}, response must be either a sequence or a str")
    # format responses and kwargs into the appropriate formats
    combined_response = {"response": response, **kwargs_dict}
    if isinstance(response, str):
        return combined_response
    # else, there are multiple responses
    # transpose the dict of lists -> list of dicts, same length as prompt/response sequence
    combined_response_keys = combined_response.keys()
    combined_response_values_transposed = zip(*combined_response.values())
    return [dict(zip(combined_response_keys, values)) for values in combined_response_values_transposed]


def tlm_explanation_format_tlm_result(
    tlm_result: Union[TLMResponse, Sequence[TLMResponse], TLMScore, Sequence[TLMScore]],
    response: Optional[Union[str, Sequence[str]]] = None,
) -> Union[dict[str, Any], list[dict[str, Any]]]:
    if isinstance(tlm_result, Sequence):
        if not all(isinstance(r, dict) for r in tlm_result):
            raise ValidationError("all items in the tlm_result sequence must be dicts")

        if not all("trustworthiness_score" in r for r in tlm_result):
            raise ValidationError("all items in the tlm_result sequence must contain a 'trustworthiness_score' key")

        # for .get_trustworthiness_score() cases, the response is passed in as a separate argument
        if not all("response" in r for r in tlm_result):
            if response is None:
                raise ValidationError(
                    "'response' is required if not provided in tlm_result, pass it in using the 'response' argument"
                )
            if not isinstance(response, Sequence) or isinstance(response, str):
                raise ValidationError("response must be a sequence when tlm_result is a sequence")
            if len(response) != len(tlm_result):
                raise ValidationError("response and score sequences must have the same length")
            if not all(isinstance(r, str) for r in response):
                raise ValidationError("all items in the response sequence must be strings")

            return [{"response": r, **tlm_result} for r, tlm_result in zip(response, tlm_result)]

        # for .prompt() cases, the response is provided in the tlm_result dict
        if response is not None:
            raise ValidationError(
                "response should only be provided once, either using the 'response' argument or in 'tlm_result'"
            )

        return cast(list[dict[str, Any]], tlm_result)

    if not isinstance(tlm_result, dict):
        raise ValidationError("tlm_result must be a dict or a sequence of dicts")

    if "trustworthiness_score" not in tlm_result:
        raise ValidationError("tlm_result must contain a 'trustworthiness' key")

    # the .get_trustworthiness_score() case
    if "response" not in tlm_result:
        if response is None:
            raise ValidationError(
                "'response' is required if not provided in tlm_result, pass it in using the 'response' argument"
            )
        if not isinstance(response, str):
            raise ValidationError("response must be a string when tlm_result is a dict")
        return {"response": response, **tlm_result}

    # the .prompt() case
    if response is not None:
        raise ValidationError(
            "response should only be provided once, either using the 'response' argument or in 'tlm_result'"
        )
    return cast(dict[str, Any], tlm_result)


def tlm_explanation_format_trustworthy_rag_result(
    tlm_result: Union[
        TrustworthyRAGResponse,
        Sequence[TrustworthyRAGResponse],
        TrustworthyRAGScore,
        Sequence[TrustworthyRAGScore],
    ],
    response: Optional[Union[str, Sequence[str]]] = None,
) -> Union[dict[str, Any], list[dict[str, Any]]]:
    if isinstance(tlm_result, Sequence):
        if not all(isinstance(r, dict) for r in tlm_result):
            raise ValidationError("all items in the tlm_result sequence must be dicts")

        if not all(
            "trustworthiness" in r
            and isinstance(r["trustworthiness"], dict)
            and "score" in r["trustworthiness"]
            and r["trustworthiness"]["score"] is not None
            for r in tlm_result
        ):
            raise ValidationError(
                "all items in the tlm_result sequence must contain a 'trustworthiness' dict with a non-None 'score' key"
            )

        # for .score() cases, the response is passed in as a separate argument
        if not all("response" in r for r in tlm_result):
            if response is None:
                raise ValidationError(
                    "'response' is required if not provided in tlm_result, pass it in using the 'response' argument"
                )
            if not isinstance(response, Sequence) or isinstance(response, str):
                raise ValidationError("response must be a sequence when tlm_result is a sequence")
            if len(response) != len(tlm_result):
                raise ValidationError("response and score sequences must have the same length")
            if not all(isinstance(r, str) for r in response):
                raise ValidationError("all items in the response sequence must be strings")

            return [
                {
                    "response": resp,
                    "trustworthiness_score": res["trustworthiness"]["score"],  # type: ignore
                    **{k: v for k, v in res["trustworthiness"].items() if k != "score"},  # type: ignore
                }
                for resp, res in zip(response, tlm_result)
            ]

        # for .generate() cases, the response is provided in the tlm_result dict
        if response is not None:
            raise ValidationError(
                "response should only be provided once, either using the 'response' argument or in 'tlm_result'"
            )

        return [
            {
                "response": res["response"],
                "trustworthiness_score": res["trustworthiness"]["score"],  # type: ignore
                **{k: v for k, v in res["trustworthiness"].items() if k != "score"},  # type: ignore
            }
            for res in tlm_result
        ]

    if not isinstance(tlm_result, dict):
        raise ValidationError("tlm_result must be a dict or a sequence of dicts")

    if (
        "trustworthiness" not in tlm_result
        or not isinstance(tlm_result["trustworthiness"], dict)
        or "score" not in tlm_result["trustworthiness"]
        or tlm_result["trustworthiness"]["score"] is None
    ):
        raise ValidationError("tlm_result must contain a 'trustworthiness' dict with a non-None 'score' key")

    # the .score() case
    if "response" not in tlm_result:
        if response is None:
            raise ValidationError(
                "'response' is required if not provided in tlm_result, pass it in using the 'response' argument"
            )
        if not isinstance(response, str):
            raise ValidationError("response must be a string when tlm_result is a dict")

        return {
            "response": response,
            "trustworthiness_score": tlm_result["trustworthiness"]["score"],
            **{k: v for k, v in tlm_result["trustworthiness"].items() if k != "score"},
        }

    # the .generate() case
    if response is not None:
        raise ValidationError(
            "response should only be provided once, either using the 'response' argument or in 'tlm_result'"
        )

    return {
        "response": tlm_result["response"],
        "trustworthiness_score": tlm_result["trustworthiness"]["score"],
        **{k: v for k, v in tlm_result["trustworthiness"].items() if k != "score"},
    }


def validate_tlm_lite_score_options(score_options: Any) -> None:
    invalid_score_keys = set(score_options.keys()).intersection(INVALID_SCORE_OPTIONS)
    if invalid_score_keys:
        raise ValidationError(
            f"Please remove these invalid keys from the `options` dictionary provided for TLMLite: {invalid_score_keys}.\n"
        )


def get_tlm_lite_response_options(score_options: Any, response_model: str) -> dict[str, Any]:
    response_options = {"model": response_model, "log": ["perplexity"]}
    if score_options is not None:
        for option_key in VALID_RESPONSE_OPTIONS:
            if option_key in score_options:
                response_options[option_key] = score_options[option_key]

    return response_options


def validate_rag_inputs(
    *,
    is_generate: bool,
    query: Union[str, Sequence[str]],
    context: Union[str, Sequence[str]],
    prompt: Optional[Union[str, Sequence[str]]] = None,
    form_prompt: Optional[Callable[[str, str], str]] = None,
    response: Optional[Union[str, Sequence[str]]] = None,
    evals: Optional[list[Any]] = None,
) -> Union[str, Sequence[str]]:
    """
    Validate inputs for TrustworthyRAG generate and score methods.

    This function validates that the inputs provided to TrustworthyRAG methods are valid and compatible.
    It checks for required parameters based on the method being called (generate or score),
    validates parameter types, ensures prompt formatting is handled correctly, and verifies
    that the necessary inputs for any evaluation objects are present.

    Args:
        is_generate (bool): Whether this validation is for a generate call or not.
        query (str | Sequence[str]): The user query (or multiple queries) to be answered.
        context (str | Sequence[str]): The context (or contexts) to use when answering the query.
        prompt (str | Sequence[str], optional): Optional prompt string (or prompts) to use instead of forming a prompt from query and context.
        form_prompt (Callable[[str, str], str], optional): Optional function to format the prompt based on query and context.
        response (str | Sequence[str], optional): Optional response (or responses) to score. Required when is_generate=False.
        evals (list[Any], optional): List of evaluation criteria to use.

    Returns:
        str | Sequence[str]: Formatted prompts if all validation checks pass.

    Raises:
        ValidationError: If any validation check fails (incompatible parameters, missing required inputs, etc.).
        NotImplementedError: If batch processing is attempted (sequences of inputs).
    """
    # Validate that prompt and form_prompt are not provided at the same time
    if prompt is not None and form_prompt is not None:
        raise ValidationError(
            "'prompt' and 'form_prompt' cannot be provided at the same time. Use either one, not both."
        )

    # Ensure consistent input formats - either all strings or all lists
    inputs_to_check = [("query", query), ("context", context), ("prompt", prompt)]
    if not is_generate:
        inputs_to_check.append(("response", response))

    # Filter out None values
    inputs_to_check = [(name, value) for name, value in inputs_to_check if value is not None]

    # Check if any input is a list (not a string)
    is_any_list = any(isinstance(value, Sequence) and not isinstance(value, str) for _, value in inputs_to_check)

    # Validate format consistency and length matching for list inputs
    if is_any_list:
        # All inputs should be lists
        string_inputs = [(name, value) for name, value in inputs_to_check if isinstance(value, str)]
        if string_inputs:
            raise ValidationError(
                f"Inconsistent input formats: {string_inputs[0][0]} is a string while other inputs are lists. "
                f"All inputs must be either strings or lists."
            )

        # All lists should have the same length
        list_lengths = [
            (name, len(value))
            for name, value in inputs_to_check
            if isinstance(value, Sequence) and not isinstance(value, str)
        ]
        if len({length for _, length in list_lengths}) > 1:
            lengths_str = ", ".join(f"{name}: {length}" for name, length in list_lengths)
            raise ValidationError(
                f"Input lists have different lengths: {lengths_str}. " f"All input lists must have the same length."
            )

    # Check for batch inputs - simplified by using a list of parameters to check
    batch_params = [(query, "query"), (context, "context"), (prompt, "prompt")]
    if not is_generate:
        batch_params.append((response, "response"))

    if query is None or context is None:
        raise ValidationError("Both 'query' and 'context' are required parameters")
    if not is_generate and response is None:
        raise ValidationError("'response' is a required parameter")

    # Format prompt if needed
    formatted_prompts: Union[str, Sequence[str]] = "" if prompt is None else prompt
    if prompt is None and form_prompt is not None:
        # Handle both single and batch cases for formatting
        if isinstance(query, str) and isinstance(context, str):
            formatted_prompts = form_prompt(query, context)
        elif (
            isinstance(query, Sequence)
            and isinstance(context, Sequence)
            and not isinstance(query, str)
            and not isinstance(context, str)
        ):
            if len(query) != len(context):
                raise ValidationError("'query' and 'context' sequences must have the same length for batch processing")
            formatted_prompts = [form_prompt(q, c) for q, c in zip(query, context)]
        else:
            raise ValidationError("'query' and 'context' must both be either strings or sequences of strings")

    # Validate parameter types - reuse the batch_params list
    for param_tuple in batch_params:
        param_value, param_name = param_tuple
        if param_value is not None:
            if isinstance(param_value, str):
                # String input is valid
                pass
            elif isinstance(param_value, Sequence) and not isinstance(param_value, str):
                # Check that all items in the sequence are strings
                if any(not isinstance(item, str) for item in param_value):
                    raise ValidationError(
                        f"All items in '{param_name}' must be of type string when providing a sequence"
                    )
            else:
                raise ValidationError(
                    f"'{param_name}' must be either a string or a sequence of strings, not {type(param_value)}"
                )

    # Validate inputs for evaluations - collect all missing inputs in one error message
    if evals:
        for eval_obj in evals:
            missing_inputs = []
            if eval_obj.query_identifier and query is None:
                missing_inputs.append("query")
            if eval_obj.context_identifier and context is None:
                missing_inputs.append("context")
            if not is_generate and eval_obj.response_identifier and response is None:
                missing_inputs.append("response")

            if missing_inputs:
                raise ValidationError(
                    f"Missing required input(s) {', '.join(missing_inputs)} for evaluation '{eval_obj.name}'"
                )

    return formatted_prompts
