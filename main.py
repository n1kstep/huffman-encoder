class HuffmanEncoder:
    def __init__(self):
        self.str_to_encode = ''
        self.encoded_str = ''
        self.huff_table = {}

    def encode_string(self, string):
        class Tree:
            def __init__(self, left=None, right=None):
                self.left = left
                self.right = right

        def traver(built_tree, code=''):
            if type(built_tree.left) == Tree:
                code += '0'
                code = traver(built_tree.left, code)
            else:
                code += '0'
                self.huff_table[built_tree.left] = code
                code = code[:-1]
            if type(built_tree.right) == Tree:
                code += '1'
                code = traver(built_tree.right, code)
            else:
                code += '1'
                self.huff_table[built_tree.right] = code
                code = code[:-1]
            code = code[:-1]
            return code

        self.str_to_encode = string
        self.encoded_str = string

        dct = {}
        for letter in self.str_to_encode:
            if letter not in dct.keys():
                dct[letter] = self.str_to_encode.count(letter)

        dct = {key: val for key, val in sorted(dct.items(), key=lambda item: item[1])}
        flag = False
        if len(dct) == 1:
            flag = True
        while len(dct) != 1:
            k1 = list(dct.keys())[0]
            v1 = list(dct.values())[0]
            dct.pop(k1)

            k2 = list(dct.keys())[0]
            v2 = list(dct.values())[0]
            dct.pop(k2)

            tree = Tree(k1, k2)
            dct[tree] = v1 + v2
            dct = {key: val for key, val in sorted(dct.items(), key=lambda item: item[1])}

        if flag:
            self.huff_table[self.str_to_encode[:1]] = '0'
        else:
            traver(*list(dct.keys()))
        for letter in set(self.str_to_encode):
            self.encoded_str = self.encoded_str.replace(letter, self.huff_table[letter])

    def decode_string(self, huff_table, string):
        self.huff_table = huff_table
        self.encoded_str = string

        code = ''
        for letter in self.encoded_str:
            code += letter
            for key, val in self.huff_table.items():
                if code == val:
                    self.str_to_encode += key
                    code = ''
                    break

    def get_encoded(self):
        return self.encoded_str

    def get_decoded(self):
        return self.str_to_encode
