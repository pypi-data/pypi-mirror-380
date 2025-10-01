from typing import Dict, Optional
from ..controllers.screen import ScreenController
from ..controllers.keyboard import KeyboardController
from ..controllers.clipboard import ClipboardController
from ..controllers.powershell import PowerShellController
from ..controllers.mouse import MouseController
from ..controllers.files import FilesController
from ..utils.request import request


class Space:
    """
    Represents a remote Space.
    Provides controllers and lifecycle methods.
    """

    def __init__(self, base_url: str, api_key: str, space_id: str):
        self.base_url = base_url
        self.api_key = api_key
        self.space_id = space_id

        # Controllers
        self.Screen = ScreenController(self)
        self.Keyboard = KeyboardController(self)
        self.Clipboard = ClipboardController(self)
        self.PowerShell = PowerShellController(self)
        self.Mouse = MouseController(self)
        self.Files = FilesController(self)

   
    async def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        files: Optional[Dict] = None,
        response_type: str = "json"
    ):
        
        url = f"{self.base_url}/v1/spaces/{self.space_id}{endpoint}"
        headers = {"x-api-key": self.api_key}
    
        return await request(
            url,
            method,
            headers=headers,
            data=data,
            files=files,
            response_type=response_type
        )

    async def status(self):
        return await self._request("POST", "/status")

    async def start(self):
        return await self._request("POST", "/start")

    async def stop(self):
        return await self._request("POST", "/stop")

    async def restart(self):
        return await self._request("POST", "/restart")
