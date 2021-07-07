import hashlib
class Tool():
    def decode(self,string):
        s = hashlib.sha256(string.encode()).hexdigest()
        return s
if __name__ == '__main__':
   t = Tool().decode('123456')
   print(t)
    # string = '123456'
    # p = hashlib.sha256(string.encode()).hexdigest()
    # print(p)