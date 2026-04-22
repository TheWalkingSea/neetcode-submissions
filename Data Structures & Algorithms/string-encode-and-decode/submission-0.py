class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += s
            encoded_string += '\0'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        return s.split('\0')[:-1]
