# Copyright © 2025 GlacieTeam.All rights reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy
# of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0

from pathlib import Path
from typing import overload, List, Any, Optional
from rapidnbt._NBT.tag_type import TagType
from rapidnbt._NBT.compound_tag import CompoundTag
from rapidnbt._NBT.compound_tag_variant import CompoundTagVariant
from rapidnbt._NBT.nbt_compression_level import NbtCompressionLevel
from rapidnbt._NBT.nbt_compression_type import NbtCompressionType
from rapidnbt._NBT.nbt_file_format import NbtFileFormat
from rapidnbt._NBT.snbt_format import SnbtFormat

class NbtFile:
    """
    NBT file
    Use nbtio.open() to open a NBT file.
    """

    def __contains__(self, key: str) -> bool:
        """
        Check if key exists in the compound
        """

    def __delitem__(self, key: str) -> bool:
        """
        Remove key from the compound
        """

    def __enter__(self) -> NbtFile:
        """
        Enter context manager
        """

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """
        Exit context manager
        """

    def __getitem__(self, key: str) -> CompoundTagVariant:
        """
        Get value by key (no exception, auto create if not found)
        """

    def __iter__(self) -> List[str]:
        """
        Iterate over keys in the compound
        """

    def __len__(self) -> int:
        """
        Get number of key-value pairs
        """

    def __repr__(self) -> str:
        """
        Official string representation
        """

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Set value by key
        """

    def __str__(self) -> str:
        """
        String representation
        """

    def clear(self) -> None:
        """
        Remove all elements from the compound
        """

    @overload
    def contains(self, key: str) -> bool:
        """
        Check if key exists
        """

    @overload
    def contains(self, key: str, type: TagType) -> bool:
        """
        Check if key exists and value type is the specific type
        """

    def empty(self) -> bool:
        """
        Check if the compound is empty
        """

    def get(self, key: str) -> CompoundTagVariant:
        """
        Get tag by key
        Throw KeyError if not found
        """

    def items(self) -> list:
        """
        Get list of (key, value) pairs in the compound
        """

    def keys(self) -> list:
        """
        Get list of all keys in the compound
        """

    def merge(self, other: CompoundTag, merge_list: bool = False) -> None:
        """
        merge_list: If true, merge list contents instead of replacing
        """

    def pop(self, key: str) -> bool:
        """
        Remove key from the compound
        """

    def put(self, key: str, value: Any) -> None:
        """
        Put a value into the compound (automatically converted to appropriate tag type)
        """

    def rename(self, old_key: str, new_key: str) -> bool:
        """
        Rename a key in the compound
        """

    def save(self) -> None:
        """
        Save NBT to file
        """

    def set(self, key: str, value: Any) -> None:
        """
        Set value in the compound (automatically converted to appropriate tag type)
        """

    def size(self) -> int:
        """
        Get the size of the compound in file
        """

    def to_binary_nbt(self, little_endian: bool = True, header: bool = False) -> bytes:
        """
        Serialize to binary NBT format
        """

    def to_dict(self) -> dict:
        """
        Convert CompoundTag to a Python dictionary
        """

    def to_json(self, indent: int = 4) -> str:
        """
        Convert tag to JSON string
        """

    def to_network_nbt(self) -> bytes:
        """
        Serialize to Network NBT format (used in Minecraft networking)
        """

    def to_snbt(self, format: SnbtFormat = SnbtFormat, indent: int = 4) -> str:
        """
        Convert tag to SNBT string
        """

    def values(self) -> list:
        """
        Get list of all values in the compound
        """

    @property
    def compression_level(
        self,
    ) -> Optional[NbtCompressionLevel]:
        """
        File compression level
        """

    @compression_level.setter
    def compression_level(self, arg0: Optional[NbtCompressionLevel]) -> None:
        """
        File compression level
        """

    @property
    def compression_type(
        self,
    ) -> Optional[NbtCompressionType]:
        """
        File compression type
        """

    @compression_type.setter
    def compression_type(self, arg0: Optional[NbtCompressionType]) -> None:
        """
        File compression type
        """

    @property
    def file_data(self) -> CompoundTag:
        """
        File NBT data
        """

    @file_data.setter
    def file_data(self, arg0: CompoundTag) -> None:
        """
        File NBT data
        """

    @property
    def file_format(self) -> Optional[NbtFileFormat]:
        """
        Binary file format
        """

    @file_format.setter
    def file_format(self, arg0: Optional[NbtFileFormat]) -> None:
        """
        Binary file format
        """

    @property
    def file_path(self) -> Path:
        """
        File path
        """

    @property
    def is_snbt(self) -> bool:
        """
        File is Snbt File
        """

    @is_snbt.setter
    def is_snbt(self, arg0: bool) -> None:
        """
        File is Snbt File
        """

    @property
    def snbt_format(self) -> Optional[SnbtFormat]:
        """
        File Snbt format
        """

    @snbt_format.setter
    def snbt_format(self, arg0: Optional[SnbtFormat]) -> None:
        """
        File Snbt format
        """

    @property
    def snbt_indent(self) -> Optional[int]:
        """
        File Snbt indent
        """

    @snbt_indent.setter
    def snbt_indent(self, arg0: Optional[int]) -> None:
        """
        File Snbt indent
        """

    @property
    def value(self) -> dict:
        """
        Access the dict value of this file
        """

    @value.setter
    def value(self, arg1: dict) -> None:
        """
        Access the dict value of this file
        """
