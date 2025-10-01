from .models.space import Space

class Cybercafe:
    """
    Cybercafe client entrypoint.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.cybercafe.space"):
        if not api_key:
            raise ValueError("API key must be provided")
        self.api_key = api_key
        self.base_url = base_url

    def space(self, space_id: str) -> Space:
        """
        Create a Space instance by ID.
        """
        return Space(self.base_url, self.api_key, space_id)
