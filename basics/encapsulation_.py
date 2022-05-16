class En:
    a = 10 # public
    _b = 20 # protected
    __c = 30 # private
    def disp(self):
        return self.a, self._b, self.__c

    def incre_(self, __o=1):
        return self.a + __o

# print(En.disp(En))

print(En.a)
print(En._b)
# print(En.__c)
print(dir(En))
print(En._En__c)
print(En.incre_(En))

