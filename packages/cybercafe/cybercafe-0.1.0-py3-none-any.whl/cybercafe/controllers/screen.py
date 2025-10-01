
class ScreenController:
    """
    ScreenController
    Handles screen operations.
    """

    def __init__(self, space):
        self.space = space

    async def screenshot(self) -> str:
        """
        Take a screenshot of the current space.

        Returns:
            str: Base64 encoded screenshot.

        Example:
            image = await space.Screen.screenshot()
            print(image)  # "data:image/png;base64,..."
        """
        response = await self.space._request("GET", "/screenshot")
        return response.get("image")
