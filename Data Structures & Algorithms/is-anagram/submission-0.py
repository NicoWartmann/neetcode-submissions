class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        for sc in s_list:
            if sc in t_list:
                t_list.remove(sc)
            else:
                return False
        return not bool(t_list)
