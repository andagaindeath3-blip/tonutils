import typing as t

from .liteserver import LiteserverClient
from .quicknode import QuicknodeClient
from .tatum import TatumClient
from .tonapi import TonapiClient
from .toncenter import ToncenterClient

ClientLike = t.Union[
    LiteserverClient,
    QuicknodeClient,
    TatumClient,
    ToncenterClient,
    TonapiClient,
]

__all__ = [
    "ClientLike",
    "LiteserverClient",
    "QuicknodeClient",
    "TatumClient",
    "TonapiClient",
    "ToncenterClient",
]
