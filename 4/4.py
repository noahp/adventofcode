import hashlib

if __name__ == '__main__':
    for x in xrange(1, 9999999):
        if hashlib.md5('ckczppom' + '%d'%x).digest().encode('hex').find('00000') == 0:
            print x
            print hashlib.md5('ckczppom' + '%d'%x).digest().encode('hex')
            break
