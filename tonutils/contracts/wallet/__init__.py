import typing as t

from .base import BaseWallet
from .get_methods import WalletGetMethods
from .versions import (
    WalletHighloadV2,
    WalletHighloadV3R1,
    WalletPreprocessedV2,
    WalletV1R1,
    WalletV1R2,
    WalletV1R3,
    WalletV2R1,
    WalletV2R2,
    WalletV3R1,
    WalletV3R2,
    WalletV4R1,
    WalletV4R2,
    WalletV5Beta,
    WalletV5R1,
)

WalletLike = t.Union[
    BaseWallet,
    WalletHighloadV2,
    WalletHighloadV3R1,
    WalletPreprocessedV2,
    WalletV1R1,
    WalletV1R2,
    WalletV1R3,
    WalletV2R1,
    WalletV2R2,
    WalletV3R1,
    WalletV3R2,
    WalletV4R1,
    WalletV4R2,
    WalletV5Beta,
    WalletV5R1,
]

__all__ = [
    "BaseWallet",
    "WalletLike",
    "WalletGetMethods",
    "WalletHighloadV2",
    "WalletHighloadV3R1",
    "WalletPreprocessedV2",
    "WalletV1R1",
    "WalletV1R2",
    "WalletV1R3",
    "WalletV2R1",
    "WalletV2R2",
    "WalletV3R1",
    "WalletV3R2",
    "WalletV4R1",
    "WalletV4R2",
    "WalletV5Beta",
    "WalletV5R1",
    "get_methods",
]
