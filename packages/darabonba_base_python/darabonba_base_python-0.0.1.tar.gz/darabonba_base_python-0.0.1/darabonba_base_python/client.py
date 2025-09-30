# -*- coding: utf-8 -*-
import hashlib
import os
import datetime


class Client:
    """
    客户端工具类，提供时间格式转换、随机数生成和签名生成功能
    """

    def __init__(self):
        pass

    @staticmethod
    def time_rfc3339() -> str:
        """
        生成RFC3339格式的当前时间字符串
        @return: RFC3339格式的时间字符串
        """
        # 获取当前UTC时间并格式化为RFC3339格式
        now = datetime.datetime.now(datetime.timezone.utc)
        # 格式化为带'Z'后缀的形式，符合RFC3339标准
        return now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-4] + "Z"

    @staticmethod
    def generate_nonce() -> str:
        """
        生成16位随机Nonce
        @return: 16位十六进制随机字符串
        """
        # 生成8字节随机数据，转换为16位十六进制字符串
        random_bytes = os.urandom(8)
        return random_bytes.hex()

    @staticmethod
    def generate_signature(
            body: str,
            nonce: str,
            secret_key: str,
            timestamp: str,
            uri: str,
    ) -> str:
        """
        生成请求签名
        @return: 签名字符串
        @description 按照指定规则生成MD5签名
        """
        parts = []

        # 如果body不为空，添加到参数列表
        if body:
            parts.append(f"body={body}")

        # 添加其他必要参数
        parts.extend([
            f"nonce={nonce}",
            f"secretKey={secret_key}",
            f"timestamp={timestamp}",
            f"url={uri}",
        ])

        # 拼接参数并生成MD5哈希
        sign_str = "&".join(parts)
        md5_hash = hashlib.md5(sign_str.encode('utf-8'))
        return md5_hash.hexdigest()
