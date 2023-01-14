class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self.bucket = size * [None]


    def hash_key(self, key):
        # 'python'
        # convert each character in it's ascii form
        sum_hash = 0
        for char in key:
            sum_hash +=ord(char)

        primed = sum_hash * 11
        index = primed % self.size
        return index



if __name__ == '__main__':
    hash1 = Hashtable(30)
    print(hash1.hash_key('python'))
    print(hash1.bucket)
