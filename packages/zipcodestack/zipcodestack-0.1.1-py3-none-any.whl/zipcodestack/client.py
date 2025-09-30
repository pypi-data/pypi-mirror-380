from typing import Any, Dict, Iterable, Optional, Union

try:
    # The EverAPI base client is published as the "everapi" package
    from everapi import Client as EverApiClient
except Exception as import_error:  # pragma: no cover - import guard for clearer error
    raise RuntimeError(
        "The 'everapi' package is required. Install it with 'pip install everapi'."
    ) from import_error


class Client:
    """High-level Zipcodestack API client built on top of EverAPI's Python base client.

    This wrapper configures the base URL for Zipcodestack and exposes convenient
    methods for each endpoint.
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://api.zipcodestack.com/v1",
        timeout: Optional[float] = None,
    ) -> None:
        """Create a new Zipcodestack client.

        - api_key: Your Zipcodestack API key
        - base_url: Override the API base, primarily for testing
        - timeout: Optional request timeout forwarded to the base client
        """
        self._client = EverApiClient(api_key, base_url=base_url, timeout=timeout)

    def status(self) -> Dict[str, Any]:
        """Retrieve API status and quota information for the current API key."""
        return self._client.get("/status")

    def search(
        self,
        *,
        codes: Union[str, Iterable[str]],
        country: Optional[str] = None,
        **extra_params: Any,
    ) -> Dict[str, Any]:
        """Search postal/zip codes.

        - codes: One code or an iterable of codes. Iterables are joined by commas.
        - country: Optional ISO alpha-2 country code to scope the search
        - extra_params: Any additional query parameters accepted by the API
        """
        if isinstance(codes, (list, tuple, set)):
            joined_codes = ",".join(str(code) for code in codes)
        else:
            joined_codes = str(codes)

        params: Dict[str, Any] = {"codes": joined_codes}
        if country:
            params["country"] = country
        if extra_params:
            params.update(extra_params)

        return self._client.get("/search", params=params)

    def distance(
        self,
        *,
        code: str,
        compare: Union[str, Iterable[str]],
        country: Optional[str] = None,
        unit: Optional[str] = None,
        **extra_params: Any,
    ) -> Dict[str, Any]:
        """Calculate distance between postal/zip codes.

        - code: The origin postal code
        - compare: One or more destination codes. Iterables are joined by commas.
        - country: Optional ISO alpha-2 code
        - unit: Optional unit, e.g. 'km' or 'mi', if supported by the API
        - extra_params: Any additional query parameters accepted by the API
        """
        if isinstance(compare, (list, tuple, set)):
            joined_compare = ",".join(str(c) for c in compare)
        else:
            joined_compare = str(compare)

        params: Dict[str, Any] = {"code": str(code), "compare": joined_compare}
        if country:
            params["country"] = country
        if unit:
            params["unit"] = unit
        if extra_params:
            params.update(extra_params)

        return self._client.get("/distance", params=params)



