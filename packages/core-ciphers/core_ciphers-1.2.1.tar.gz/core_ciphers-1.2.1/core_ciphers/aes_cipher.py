# -*- coding: utf-8 -*-

"""
The AESCipher class implements the ICipher interface and
provides AES encryption/decryption functionality supporting
multiple cipher modes.
"""

from binascii import hexlify, unhexlify
from typing import Any, Dict, Optional, Tuple

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from .base import ICipher


class AESCipher(ICipher):
    """
    Cipher that use AES (Advanced Encryption Standard) method with MODE_GCM

    This symmetric/reversible key encryption block clipper is equipped
    to handle 128-bit blocks, using keys sized at 128, 192, and 256
    bits.

    This block chipper is especially recognized for protecting data at rest,
    and it's widely regarded as the most secure symmetric key encryption cipher
    yet invented.

    AES Cipher Modes
    The cipher modes are required for a usual AES implementation. An incorrect
    implementation or application of modes may severely compromise the AES
    algorithm security. There are multiple chipper modes are available
    in AES, Some highly used AES cipher modes as follows:

      - ECB mode: Electronic Code Book mode
      - CBC mode: Cipher Block Chaining mode
      - CFB mode: Cipher Feedback mode
      - OFB mode: Output FeedBack mode
      - CTR mode: Counter mode
      - GCM mode: Galois/Counter mode

    CBC mode: Cipher Block Chaining mode
    In CBC the mode, every encryption of the same plaintext should result
    in a different ciphertext. The CBC mode does this with an initialization
    vector. The vector has the same size as the block that is encrypted.

    Problems in (CBC mode)
    One of the major problems an error of one plaintext block will affect all
    the following blocks. At the same time, Cipher Block Chaining mode(CBC) is
    vulnerable to multiple attack types:
      - Chosen Plaintext Attack(CPA)
      - Chosen Ciphertext Attack(CCA)
      - Padding oracle attacks

    AES-GCM instead of AES-CBC
    Both the AES-CBC and AES-GCM are able to secure your valuable data
    with a good implementation. but to prevent complex CBC attacks such
    as Chosen Plaintext Attack(CPA) and Chosen Ciphertext Attack(CCA)
    it is necessary to use Authenticated Encryption. So the best option
    is for that is GCM. AES-GCM is written in parallel which means throughput
    is significantly higher than AES-CBC by lowering encryption overheads.

    AES-GCM
    In simple terms, Galois Counter Mode (GCM) block clipper is a combination
    of Counter mode (CTR) and Authentication it’s faster and more secure with a
    better implementation for table-driven field operations. GCM has two
    operations, authenticated encryption and authenticated decryption.

    The GCM mode will accept pipelined and parallelized implementations
    and have minimal computational latency in order to be useful at high
    data rates. As a conclusion, we can choose the Galois Counter Mode (GCM)
    block clipper mode to achieve excellent security performance for
    data at rest.
    """

    def __init__(
        self,
        key: Optional[bytes] = None,
        mode: int = AES.MODE_GCM,
        encoding: str = "UTF-8",
        block_size: int = 16,
        authenticated_modes: Optional[Tuple[int, ...]] = None,
        padding_modes: Optional[Tuple[int, ...]] = None,
    ) -> None:
        """
        Initialize the AES cipher with encryption parameters.

        :param key:
            Encryption key as bytes. If None, a random key is generated
            (32 bytes for MODE_SIV, 16 bytes for other modes).

        :param mode: AES cipher mode (default: AES.MODE_GCM).
        :param encoding: Character encoding for string operations (default: "UTF-8").
        :param block_size: Block size for padding operations (default: 16 bytes).

        :param authenticated_modes:
            Tuple of AES modes that support authenticated encryption.
            Default: (MODE_GCM, MODE_EAX, MODE_CCM, MODE_SIV, MODE_OCB).

        :param padding_modes:
            Tuple of AES modes that require padding.
            Default: (MODE_ECB, MODE_CBC).
            Note: Stream cipher modes (CFB, OFB, CTR) and authenticated
            modes (GCM, EAX, CCM, SIV) do not require padding.
        """

        super().__init__(
            key=key,
            mode=mode,
            encoding=encoding,
        )

        self.block_size = block_size

        self.authenticated_modes = authenticated_modes or (
            AES.MODE_GCM,
            AES.MODE_EAX,
            AES.MODE_CCM,
            AES.MODE_SIV,
            AES.MODE_OCB,
        )

        self.padding_modes = padding_modes or (
            AES.MODE_ECB,
            AES.MODE_CBC,
        )

    def encrypt(self, data: str, *args, **kwargs) -> Dict:
        """
        Encrypts the provided string data using AES encryption.

        The method converts the input string to bytes, applies padding if required
        for the cipher mode, encrypts the data, and generates an authentication tag
        for authenticated encryption modes (GCM, EAX, CCM, SIV, OCB).

        :param data: The plaintext string to encrypt.

        :return:
            A dictionary containing hex-encoded encryption components:
              - ciphertext (str): The encrypted data.
              - tag (str, optional): Authentication tag for authenticated modes.
              - nonce (str, optional): Nonce used for encryption (for nonce-based modes).
              - iv (str, optional): Initialization vector (for IV-based modes).
        """

        data_bytes: bytes = bytes(data, encoding=self.encoding)
        cipher = AES.new(self.key, self.mode)  # type: ignore

        if self.mode in self.padding_modes:
            data_bytes = pad(data_bytes, self.block_size)

        ciphertext = cipher.encrypt(data_bytes)
        # Only generate tag for authenticated encryption modes
        tag = cipher.digest() if self.mode in self.authenticated_modes else None

        res = (
            ("ciphertext", ciphertext),
            ("tag", tag),
            ("nonce", getattr(cipher, "nonce", None)),
            ("iv", getattr(cipher, "iv", None)),
        )

        return {
            key: hexlify(value).decode(encoding=self.encoding)
            for key, value in res if value
        }

    def decrypt(self, data: Dict, *args, **kwargs) -> str:
        """
        Decrypts the encrypted data and returns the original plaintext string.

        The method processes a dictionary containing hex-encoded encryption components,
        converts them back to bytes, decrypts the ciphertext using the appropriate
        cipher mode, removes padding if necessary, and verifies the authentication
        tag for authenticated encryption modes.

        :param data:
            Dictionary containing hex-encoded encryption components:
              - ciphertext (str): The encrypted data to decrypt.
              - tag (str, optional): Authentication tag (required for authenticated modes).
              - nonce (str, optional): Nonce used during encryption.
              - iv (str, optional): Initialization vector used during encryption.

        :return: The decrypted plaintext string.
        """

        data_bytes: Dict[Any, Any] = {}
        for key, value in data.items():
            data_bytes[key] = unhexlify(value.encode(encoding=self.encoding))

        tag = data_bytes.get("tag")
        ciphertext = data_bytes.get("ciphertext")
        nonce, iv = data_bytes.get("nonce"), data_bytes.get("iv")

        cipher_args: Tuple[Any, ...] = (nonce or iv,) if self.mode != AES.MODE_ECB else ()
        cipher = AES.new(self.key, self.mode, *cipher_args)  # type: ignore

        res: bytes = cipher.decrypt(ciphertext)  # type: ignore
        if self.mode in self.padding_modes:
            res = unpad(res, self.block_size)

        # Only verify tag for authenticated encryption modes
        if self.mode in self.authenticated_modes:
            cipher.verify(tag)

        return res.decode(encoding=self.encoding)
