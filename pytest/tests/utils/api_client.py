import httpx
from typing import Dict, Any, Optional
import time

class SWAPIClient:

    BASE_URL = "https://swapi.info/api"

    def __init__(self, timeout: int = 30):
        self.client = httpx.Client(timeout=timeout, base_url=self.BASE_URL)

    def get_character(self, character_id: int) -> Dict[str, Any]:
        response = self.client.get(f"/people/{character_id}/")
        response.raise_for_status()
        return response.json()
    
    def get_resource(self, url:str) -> Dict[str, Any]:
        response = self.client.get(url)
        response.raise_for_status()
        return response.json()
    
    def measure_response_time(self, endpoint: str) -> float:
        start_time = time.time()
        self.client.get(endpoint)
        end_time = time.time()
        return end_time - start_time
    
    def close(self):
        self.client.close()

class SWAPIAsyncClient:

    BASE_URL = "https://swapi.info/api"

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    async def get_character(self, character_id: int) -> Dict[str, Any]:
        async with httpx.AsincClient(timeuot=self.timeout) as client:
            response = await client.get(f"{self.BASE_URL}/people/{character_id}/")
            response.raise_for_status()
            return response.json()
        