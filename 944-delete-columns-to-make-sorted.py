from typing import Iterator

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        def column_values(column_nr: int) -> Iterator[str]:
            for string in strs:
                yield string[column_nr]

        columns_to_delete = 0
        
        for col_index in range(0,len(strs[0])):
            print(col_index)
            current_letter = strs[0][col_index]
            for letter in column_values(col_index):
                if letter < current_letter:
                    columns_to_delete += 1
                    break
                
                current_letter = letter

        return columns_to_delete

example_strs = ["cba","daf","ghi"]
sol = Solution()
print('Solution: ', sol.minDeletionSize(example_strs))