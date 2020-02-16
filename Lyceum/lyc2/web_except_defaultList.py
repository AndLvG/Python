class DefaultList(list):
    def __init__(self, def_num):
        self.def_num = def_num
        self.data = []

    def __getitem__(self, ind):
        try:
            item = super(DefaultList, self).__getitem__(ind)
        except IndexError:
            item = self.def_num
        return item


# s = DefaultList(51)
# s.extend([1, 5, 7])

# indexes = [0, 2, 1000, -1]
# for i in indexes:
#     print(s[i], end=" ")
