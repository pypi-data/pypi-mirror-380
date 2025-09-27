import requests
import urllib.parse
from dataclasses import dataclass
from typing import Optional

__version__ = "1.0.0"
__all__ = ['pair', 'CraftResult', 'InfCraftError']

@dataclass
class CraftResult:
    name: str
    emoji: str

class InfCraftError(Exception):
    pass

def pair(element1: str, element2: str, timeout: int = 10) -> Optional[CraftResult]:
    encoded_element1 = urllib.parse.quote(element1)
    encoded_element2 = urllib.parse.quote(element2)
    
    url = f"https://infiniteback.org/pair?first={encoded_element1}&second={encoded_element2}"
    
    headers = {
        'User-Agent': f'infcraft/{__version__}',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        data = response.json()
        
        if "result" not in data or "emoji" not in data:
            raise InfCraftError("Invalid response format from API")
            
        return CraftResult(name=data["result"], emoji=data["emoji"])

    except requests.exceptions.HTTPError as http_err:
        raise InfCraftError(f"HTTP error occurred: {http_err}") from http_err
    except requests.exceptions.RequestException as req_err:
        raise InfCraftError(f"Request error occurred: {req_err}") from req_err
    except ValueError:
        raise InfCraftError("Failed to decode JSON from the response")
