class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        counter = 0

        for read in range(len(chars)):
            counter += 1
            if read == len(chars) - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                if counter > 1:
                    for char in str(counter):
                        chars[write] = char
                        write += 1
                counter = 0

        return write