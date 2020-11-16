import asyncio
from typing import List
import aiohttp
import logging
import re

log = logging.getLogger(__name__)


def text_to_matrix(text: str) -> List[List[int]]:
    """
    Converting the textual representation of a matrix

    Parameters
    ----------
    text : str
        Textual representation of the matrix

    Returns
    -------
    List[List[int]]
        Square matrix
    """
    matrix = []

    # get lines
    lines = re.findall(r'.+\|\n', text)
    if not lines:
        raise ValueError(f'Incorrect text format: could not find new lines\n{text}')

    # get numbers in lines
    for line in lines:
        numbers = re.findall(r'(?<= )\d+(?= )', line)

        if not numbers:
            raise ValueError(f'Incorrect text format: could not find values in lines\n{text}')

        numbers = list(map(int, numbers))
        matrix.append(numbers)

    return matrix


async def get_matrix(url: str) -> List[int]:
    """
    Get a square matrix (NxN) from a remote server and return it as List [int].

    List will contain the result of traversing the resulting matrix in a spiral: counterclockwise,
    starting from the upper left corner.

    Parameters
    ----------
    url : str
        URL with text matrix

    Returns
    -------
    List[int]
        List containing the result of traversing the resulting matrix in a spiral

    """
    result = []
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        try:
            async with session.get(url, timeout=7) as response:
                # check content-type
                if response.content_type not in ['text/plain']:
                    raise TypeError(f'Unsupported content-type "{response.content_type}" from {url}')

                # read text
                text = await response.text()

                # check: text is not empty
                if not text:
                    raise ValueError(f'Incorrect response: empty text')

                matrix = text_to_matrix(text)

                matrix = list(zip(*matrix))
                result.extend(matrix.pop(0))

                while matrix:
                    matrix = list(map(lambda x: x[::-1], matrix))
                    matrix = list(zip(*matrix))
                    result.extend(matrix.pop(0))
        except aiohttp.ClientConnectorError as e:
            log.error(f"Connection error: {e}")
        except aiohttp.ClientResponseError as e:
            log.error(f"Client response error: {e}")
        except asyncio.TimeoutError as e:
            log.error(f"Timeout error: {e}")
        except (TypeError, TypeError) as e:
            log.error(e)
        finally:
            await session.close()

    # Solution for bug https://github.com/aio-libs/aiohttp/issues/2039
    await asyncio.sleep(0.03)

    return result

