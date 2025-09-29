class LLMWrapperError(Exception):
    pass

class DatabaseError(LLMWrapperError):
    pass

class APIError(LLMWrapperError):
    pass

class TokenizationError(LLMWrapperError):
    pass

class ProviderError(LLMWrapperError):
    pass

class ConfigurationError(LLMWrapperError):
    pass

class RateLimitError(LLMWrapperError):
    pass

class ValidationError(LLMWrapperError):
    pass