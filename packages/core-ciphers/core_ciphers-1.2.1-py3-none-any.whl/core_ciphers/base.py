# -*- coding: utf-8 -*-

"""
Base cipher interface module.

This module provides the abstract base class for all cipher implementations
in the core_ciphers package.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class ICipher(ABC):
    """ Base class for all cypher implementations """

    def __init__(
        self,
        key: Optional[bytes] = None,
        mode: int = AES.MODE_GCM,
        encoding: str = "UTF-8",
    ) -> None:
        """
        Initialize the cipher with encryption parameters.

        :param key:
            Encryption key as bytes. If None, a random key is generated (32
            bytes for MODE_SIV, 16 bytes for other modes).

        :param mode: AES cipher mode (default: AES.MODE_GCM).
        :param encoding: Character encoding for string operations (default: "UTF-8").
        """

        if not key:
            key = get_random_bytes(32 if mode == AES.MODE_SIV else 16)

        self.key = key
        self.encoding = encoding
        self.mode = mode

    @abstractmethod
    def encrypt(self, data: Any, *args: Any, **kwargs: Any) -> Any:
        """
        Encrypt the data.

        :param data: The data to encrypt.
        :return: The encrypted data (implementation-specific format).
        """

    @abstractmethod
    def decrypt(self, data: Any, *args: Any, **kwargs: Any) -> Any:
        """
        Decrypt the data.

        :param data: The encrypted data to decrypt.
        :return: The decrypted data (implementation-specific format).
        """
