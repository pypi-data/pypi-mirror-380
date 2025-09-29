MISTRAL_SUPPORTED_MODELS = [
    "mistral-small-",
    "mistral-medium-",
    "magistral-small-",
    "magistral-medium-",
    "codestral-",
    "mistral-ocr-",
]

OPENAI_SUPPORTED_MODELS = [
    "gpt-5",
    "gpt-5-mini",
    "gpt-5-nano",
    "gpt-oss-120b",
    "gpt-oss-20b",
    "gpt-vision-1",
    "gpt-4",
    "gpt-image-1",  # image generation model
    "gpt-image",    # future variants
    "dall-e-2",     # added DALL-E 2
    "dall-e-3",     # added DALL-E 3
]

ANTHROPIC_SUPPORTED_MODELS = [
    "claude-3-5-sonnet-",
    "claude-3-7-sonnet-",
    "claude-sonnet-4-",
    "claude-opus-4-1-",
    "claude-code",
]

DEEPSEEK_SUPPORTED_MODELS = [
    "deepseek-chat",
    "deepseek-coder",
]


def is_potentially_supported_model(model_name: str) -> bool:
    all_supported_models = (
        MISTRAL_SUPPORTED_MODELS
        + OPENAI_SUPPORTED_MODELS
        + ANTHROPIC_SUPPORTED_MODELS
        + DEEPSEEK_SUPPORTED_MODELS
    )
    return any(model_name.startswith(prefix) for prefix in all_supported_models)


def is_unsupported_model(model_name: str) -> bool:
    return not is_potentially_supported_model(model_name)
