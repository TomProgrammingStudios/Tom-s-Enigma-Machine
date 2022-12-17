
class number_table:
    def __init__(self) -> None:
        self.char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.num_list = ['0 0', '0 1', '0 2', '0 3', '0 4', '0 5', '0 6', '0 7', '0 8', '0 9', '1 0', '1 1', '1 2', '1 3', '1 4', '1 5', '1 6', '1 7', '1 8', '1 9', '2 0', '2 1', '2 2', '2 3', '2 4', '2 5', '2 6']
        
    def cypher_number(self, num) -> int:
        try:
            index = self.char_list.index(num)
            return index + 1
        except:
            raise Warning("[Encoding Error] Character not in list.")

    def decypher_number(self, num) -> int:
        try:
            decoded = self.char_list[num -1]
            return decoded
        except:
            raise Warning("[Decoding Error] Character not in list.")
    
    def get_num(self, num) -> str:
        return self.num_list[num]

    def num_increase(self, num) -> int and str:
        return num + 1, self.get_num(num + 1)
    
    def num_decrease(self, num) -> int and str:
        return num - 1, self.get_num(num - 1)


class rotor:
    
    def __init__(self, register : int) -> None:
        self.reg = register
    
    def change_register(self, new_reg : int) -> None:
        self.reg = new_reg

    def register_1(self, num) -> int:
        register_table = [1, 6, 11, 16, 7, 8, 4, 13, 26, 19, 25, 10, 17, 5, 18, 20, 15, 22, 3, 14, 24, 2, 9, 21, 23, 12]        
        return register_table[num - 1]
    
    def register_2(self, num) -> int:
        register_table = [17, 4, 9, 10, 24, 2, 16, 21, 11, 6, 22, 8, 25, 20, 18, 13, 1, 26, 5, 14, 12, 19, 23, 3, 7, 15]
        return register_table[num - 1]
    
    def register_3(self, num) -> int:
        register_table = [21, 1, 2, 26, 3, 15, 6, 4, 9, 25, 11, 7, 16, 12, 8, 14, 13, 20, 22, 19, 24, 18, 17, 5, 10, 23]
        return register_table[num - 1]
    
    def register_4(self, num) -> int:
        register_table = [23, 9, 16, 22, 11, 21, 15, 26, 20, 4, 18, 7, 13, 19, 12, 25, 8, 24, 17, 10, 14, 5, 1, 3, 2, 6]
        return register_table[num - 1]
    
    def register_5(self, num) -> int:
        register_table = [19, 16, 21, 17, 14, 25, 7, 12, 20, 9, 24, 23, 5, 18, 13, 11, 2, 8, 15, 10, 6, 1, 4, 22, 3, 26]
        return register_table[num - 1]
    
    def encrypt(self, num : int, rotor_index : int) -> int:
        function_list = [self.register_1, self.register_2, self.register_3, self.register_4, self.register_5]
        num = num + rotor_index
        if num > 26:
            num = num - 26 
        return function_list[self.reg - 1](num)
        
    def reverse_encrypt(self, num : int, rotor_index : int) -> int:
        for item in range(38):
            if num == self.encrypt(item + 1, rotor_index):
                return item + 1
        raise Warning(f"Cannot reverse encrypt number {num}")


class reflector:
    def reflect(self, to_reflect : int) -> int:
        register_table = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        return register_table[to_reflect - 1]
        



