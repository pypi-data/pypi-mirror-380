# -*- coding: utf-8 -*-
"""
@项目名称 : yhfin-data-agent
@文件名称 : encrypt.py
@创建人   : zhongbinjie
@创建时间 : 2025/9/23 15:43
@文件说明 : 
@企业名称 : 深圳市赢和信息技术有限公司
@Copyright:2025-2035, 深圳市赢和信息技术有限公司. All rights Reserved.
"""
import hashlib

from passlib.context import CryptContext


from passlib.context import CryptContext
from cryptography.fernet import Fernet
import os
from utils import sm4
import re

def generate_encryption_key(key_path: str = "secret.key", override: bool = False) -> None:
    """生成加密密钥并保存到文件"""
    if os.path.exists(key_path) and not override:
        print(f"Encryption key file {key_path} already exists. Set override=True to overwrite.")
        return
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"Encryption key generated and saved to {key_path}")


def load_encryption_key(key_path: str = "secret.key") -> bytes:
    """加载加密密钥"""
    if not os.path.exists(key_path):
        return None
    return open(key_path, "rb").read()


def encrypt_reversible(plaintext: str, key_path: str = "secret.key") -> str:
    """使用Fernet算法加密明文"""
    key = load_encryption_key(key_path)
    fernet = Fernet(key)
    return fernet.encrypt(plaintext.encode()).decode()


def decrypt_reversible(ciphertext: str, key_path: str = "secret.key") -> str:
    """使用Fernet算法解密密文"""
    key = load_encryption_key(key_path)
    fernet = Fernet(key)
    return fernet.decrypt(ciphertext.encode()).decode()


def encryption_password_or_decode(*, pwd: str, hashed_password: str = None):
    """
    哈希密码加密或解密
    :param pwd:
    :param hashed_password:
    :return:
    """
    encryption_pwd = CryptContext(
        schemes=["sha256_crypt", "md5_crypt", "des_crypt"]
    )

    def encryption_password():
        password = encryption_pwd.hash(pwd)
        return password

    def decode_password():
        password = encryption_pwd.verify(pwd, hashed_password)
        return password

    return decode_password() if hashed_password else encryption_password()


class SM4():
    """
    国产加密算法： sm4加解密
    """

    def __init__(self):
        self.gmsm4 = sm4.CryptSM4()  # 实例化

    def encryptSM4(self, value, encrypt_key=None):
        """
        sm4加密
        :param value: 待加密的字符串
        :param encrypt_key: sm4加密key(十六进制字符)
        :return: sm4加密后的十六进制字符
        """
        # Validate hex key
        if not encrypt_key:
            encrypt_key = load_encryption_key("secret.key")

        if isinstance(encrypt_key, bytes):
            encrypt_key = hashlib.md5(encrypt_key).hexdigest()
        elif not re.fullmatch(r'^[0-9a-fA-F]+$', encrypt_key):
            encrypt_key = hashlib.md5(encrypt_key.encode('utf-8')).hexdigest()

        gmsm4 = self.gmsm4
        gmsm4.set_key(bytes.fromhex(encrypt_key), sm4.SM4_ENCRYPT)  # 设置密钥，将十六进制字符Key转为十六进制字节
        data_str = str(value)
        encrypt_value = gmsm4.crypt_ecb(data_str.encode())  # ecb模式开始加密，encode():普通字符转为字节
        return encrypt_value.hex()  # 返回十六进制字符

    def decryptSM4(self, encrypt_value, decrypt_key=None):
        """
        sm4解密
        :param decrypt_key:sm4加密key(十六进制字符)
        :param encrypt_value: 待解密的十六进制字符
        :return: 原字符串
        """
        if not decrypt_key:
            decrypt_key = load_encryption_key("secret.key")

        if isinstance(decrypt_key, bytes):
            decrypt_key = hashlib.md5(decrypt_key).hexdigest()
        elif not re.fullmatch(r'^[0-9a-fA-F]+$', decrypt_key):
            decrypt_key = hashlib.md5(decrypt_key.encode('utf-8')).hexdigest()

        gmsm4 = self.gmsm4
        gmsm4.set_key(bytes.fromhex(decrypt_key), sm4.SM4_DECRYPT)  # 设置密钥，将十六进制字符Key转为十六进制字节
        decrypt_value = gmsm4.crypt_ecb(bytes.fromhex(encrypt_value))  # ecb模式开始解密。bytes.fromhex():十六进制字符转为十六进制字节
        return decrypt_value.decode()

def test():
    print()


if __name__ == '__main__':
    strData = "Dameng@123"  # 明文
    SM4 = SM4()
    print("原字符", strData)
    encData = SM4.encryptSM4(strData)  # 加密后的数据
    print("sm4加密结果", encData)

    decData = SM4.decryptSM4(encData)
    print("sm4解密结果", decData)  # 解密后的数据
    pass
