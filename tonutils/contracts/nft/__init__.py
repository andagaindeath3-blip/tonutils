import typing as t

from .collection import (
    BaseNFTCollection,
    NFTCollectionEditable,
    NFTCollectionStandard,
)
from .get_methods import (
    NFTCollectionGetMethods,
    NFTItemGetMethods,
)
from .item import (
    BaseNFTItem,
    NFTItemEditable,
    NFTItemSoulbound,
    NFTItemStandard,
)

NFTCollectionLike = t.Union[
    BaseNFTCollection,
    NFTCollectionEditable,
    NFTCollectionStandard,
]
NFTItemLike = t.Union[
    BaseNFTItem,
    NFTItemEditable,
    NFTItemSoulbound,
    NFTItemStandard,
]

__all__ = [
    "BaseNFTCollection",
    "BaseNFTItem",
    "NFTCollectionLike",
    "NFTItemLike",
    "NFTCollectionGetMethods",
    "NFTItemGetMethods",
    "NFTCollectionEditable",
    "NFTCollectionStandard",
    "NFTItemEditable",
    "NFTItemSoulbound",
    "NFTItemStandard",
]
