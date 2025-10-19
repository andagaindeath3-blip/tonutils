import typing as t

from .get_methods import (
    JettonMasterGetMethods,
    JettonWalletGetMethods,
)
from .master import (
    BaseJettonMaster,
    JettonMasterStandard,
    JettonMasterStablecoin,
    JettonMasterStablecoinV2,
)
from .wallet import (
    BaseJettonWallet,
    JettonWalletStandard,
    JettonWalletStablecoin,
    JettonWalletStablecoinV2,
)

JettonMasterLike = t.Union[
    BaseJettonMaster,
    JettonMasterStandard,
    JettonMasterStablecoin,
    JettonMasterStablecoinV2,
]
JettonWalletLike = t.Union[
    BaseJettonWallet,
    JettonWalletStandard,
    JettonWalletStablecoin,
    JettonWalletStablecoinV2,
]

__all__ = [
    "JettonMasterGetMethods",
    "JettonWalletGetMethods",
    "JettonMasterStandard",
    "JettonMasterStablecoin",
    "JettonMasterStablecoinV2",
    "JettonWalletStandard",
    "JettonWalletStablecoin",
    "JettonWalletStablecoinV2",
]
