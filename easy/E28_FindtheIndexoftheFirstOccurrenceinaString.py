class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        """     
        full_n = 0
        while(len(haystack) >= len(needle)):
            idx_n = 0
            start_i = -1
            for idx, i in enumerate(haystack):
                if(i == needle[idx_n]):
                    print(haystack, needle, idx, idx_n, i, needle[idx_n])
                    idx_n += 1
                    
                    # set start index
                    if(start_i == -1):
                        start_i = idx

                    # check if idx_n == len(needle) and reset
                    if(idx_n == len(needle)):
                        print(start_i, full_n)
                        return start_i + full_n
                else:
                    idx_n = 0
                    start_i = -1
            
            haystack = haystack[1:]
            full_n += 1    
        return -1
        """

        i1 = 0
        while(len(haystack) >= len(needle)):
            n1 = 0

            for idx, i in enumerate(needle):
                if(i == haystack[idx]):
                    n1 += 1
                    if(n1 == len(needle)):
                        return i1
                else:
                    break

            haystack = haystack[1:]
            i1 += 1
        return -1

haystack = "mississppi"
needle = "isspp"

print('Res:', Solution().strStr(haystack, needle))