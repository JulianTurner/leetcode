class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        valid_ips = []

        # IP BLOCK [1,2,3,4]
        current_blocks = []
        
        def ip_walker(block_nr: int, remaining_s: str):
            if len(remaining_s) == 0:
                return
            
            if block_nr == 4:
                if len(remaining_s) > 1 and remaining_s[0] == '0':
                    return
                    
                current_block_nr = int(remaining_s)
                if 0 <= current_block_nr <= 255:
                    current_blocks.append(remaining_s)
                    valid_ips.append('.'.join(current_blocks))
                    current_blocks.pop()
            else:
                if remaining_s[0] == '0':
                    current_blocks.append('0')
                    ip_walker(block_nr+1, remaining_s[1:])
                    current_blocks.pop()
                else:
                    for last_sliced_char_index in range(min(len(remaining_s), 3)):
                        block_str = remaining_s[:(last_sliced_char_index+1)]
                        block_int = int(block_str)
                        if 0 <= block_int <= 255:
                            current_blocks.append(block_str)
                            new_remaining_s = remaining_s[(last_sliced_char_index+1):]
                            ip_walker(block_nr+1, new_remaining_s) # recursive call
                            current_blocks.pop()

        ip_walker(1, s)
            
        return valid_ips


ex_s = "101023" 
print(Solution().restoreIpAddresses(ex_s)) # ["255.255.11.135","255.255.111.35"]