class Solution:

    def encode(self, strs: List[str]) -> str:
       encoded_str = ""
       for s in strs:
            encoded_str += f"{len(s)}#{s}"
       return encoded_str

    def decode(self, s: str) -> List[str]:

        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded_strs.append(word)
            i = j + 1 + length

        return decoded_strs
