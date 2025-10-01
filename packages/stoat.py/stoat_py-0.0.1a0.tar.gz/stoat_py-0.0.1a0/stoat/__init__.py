"""
Stoat API Wrapper
~~~~~~~~~~~~~~~~~

A basic wrapper for the Stoat API.

:copyright: (c) 2025-present MCausc78
:license: MIT, see LICENSE for more details.

"""

__title__ = 'stoat.py'
__author__ = 'MCausc78'
__license__ = 'MIT'
__copyright__ = 'Copyright 2025-present MCausc78'
__version__ = '0.0.1a'

import requests
import typing

def send_message(channel_id: str, content: typing.Optional[str] = None, *, token: str, bot: bool = False, **kwargs: typing.Any) -> dict:
    url = 'https://api.revolt.chat/0.8/channels/{}/messages'.format(channel_id)
    headers = {
        'X-Bot-Token' if bot else 'X-Session-Token': token,
    }
    payload = {'content': content, **kwargs}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code >= 400:
        raise RuntimeError(f'{response.status_code}: {response.text}')
    return response.json()

class _VersionInfo(typing.NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: typing.Literal['alpha', 'beta', 'candidate', 'final']
    serial: int


version_info: typing.Final[_VersionInfo] = _VersionInfo(
    major=0,
    minor=0,
    micro=1,
    releaselevel='alpha',
    serial=0,
)

