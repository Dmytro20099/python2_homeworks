import hashlib


# def encode_md5(value: str) -> str:
#     hash_ = hashlib.md5(value.encode()).hexdigest()
#     print(hash_)
#     return hash_
#
# encode_md5('hh')
# encode_md5('hh')


from passlib.context import CryptContext

context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def password_hash(value: str):
    hash_ = context.hash(value)
    print(hash_)
    return hash_


def veryfi(ii: str, hh: str) -> bool:
    result = context.verify(ii, hh)
    print(result)
    return result



pp = password_hash('44')
veryfi('44', pp)






















































































