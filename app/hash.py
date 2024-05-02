import hashlib


def get_SHA1_limit(string_value):
    hash_value = hashlib.sha1(string_value.encode("UTF-8")).hexdigest().upper()
    return hash_value[:10]

def getSHA1(string_value):
    return hashlib.sha1(string_value.encode()).hexdigest()

def getSHA256(string_val):
    return hashlib.sha256(string_val.encode('utf-8')).hexdigest().upper()
    