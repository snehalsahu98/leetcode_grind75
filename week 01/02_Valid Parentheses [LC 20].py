class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if s[i] == ')' and st[-1] == '(':
                    st.pop()
                elif s[i] == '}' and st[-1] == '{':
                    st.pop()
                elif s[i] == ']' and st[-1] == '[':
                    st.pop()
                else:
                    return False
            else:
                st.append(s[i])

        if len(st) == 0:
            return True
        else: 
            return False
        
