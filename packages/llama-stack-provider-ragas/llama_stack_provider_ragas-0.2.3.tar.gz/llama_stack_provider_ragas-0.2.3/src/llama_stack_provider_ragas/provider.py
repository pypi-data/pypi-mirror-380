# remote is the default provider
from .remote.provider import get_provider_spec
from .remote import get_adapter_impl

__all__ = ["get_provider_spec", "get_adapter_impl"]
