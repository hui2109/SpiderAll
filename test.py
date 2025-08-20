from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5  # 这玩意是用来加密的
import base64

# 加密
s = "我特别爱你"

# 先加载公钥
with open('public_key.pem', mode="rb") as f:
    pub_key = RSA.import_key(f.read())  # 导入公钥

# 得到的rsa_key只能用来加密!
# 创建RSA加密器
rsa_cipher = PKCS1_v1_5.new(key=pub_key)

# 进行加密 (原文及密文都是字节层面的)
result = rsa_cipher.encrypt(s.encode("utf-8"))
print(base64.b64encode(result).decode())
# cCSZEpL+F8v4mZQz3EpqYjiHCGiDBbt0Fg8/qvcarugrfXfEKxBvggBV+i7u4G8lzz8LZtlWTd1XzagD6kpjYuuZ1Ij226tW+Qf4WQeX3V+0ItpIYsoPqYljGfyC8MZN7ZXdlDFUS7VgWTRvA9zim5XtZstUV5CdEmDhovX1ySjpY4Sr6DXhMRnzWkEnNp/BmK+eyPns+nPIFALWXfqn+gc1Z/4S9mRhrc7Af2vDPeNjcEei9REGH7Br2nN6b7oCn+h70+7mLbuHPWvKEXjJ6iI+0bptEKKsRusPVLsxqsjnhlAd4sHITg1bJw8ZEnhvsPJ+cWnAnCfuokhYu5PsEg==
