class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for i in range(len(strs)):
            ret.append(chr(len(strs[i])))
            ret.append(strs[i])
        return ''.join(ret)

    def decode(self, s: str) -> List[str]:
        ptr = 0
        strs = []
        while ptr < len(s):
            length = ord(s[ptr])
            curr = []
            for j in range(ptr + 1, ptr + length + 1):
                curr.append(s[j])
            strs.append(''.join(curr))
            ptr += length + 1
        return strs
