import hashlib

def hash_pwd(passwd):
    '''MD5加密'''
    md5=hashlib.md5()
    md5.update(passwd.encode('utf-8'))
    return md5.hexdigest()