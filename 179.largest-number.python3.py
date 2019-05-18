#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (24.46%)
# Total Accepted:    109.1K
# Total Submissions: 446K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#
class Solution:
    def largestNumber(self, nums):
        def help(inp):


            lis=[]
            lix=[]
            dic={}
            sortlis=[]
            m = max(inp)
            m = str(m)
            l = len(m)
            ix = []
            ix1 = []
            res = []
            a = set()
            inp.sort()
            array = []
            for i in inp:
                diff = l - len(str(i))
                ip = i
                if diff > 0:
                    i = i * (pow(10, diff))

                ix.append([i, ip])
            for i in range(len(ix)):
                ix1.append(ix[i][0])
            ix1.sort()
            # print(ix1, ix)
            for k in ix1:
                for i in range(len(ix)):
                    if k == ix[i][0]:
                        res.append(ix[i][1])
                        ix[i][0] = sys.maxsize
            lix=res
            lis=lix
            lis.reverse()
            rlis = lis[:]
            lis.reverse()

            # lis.reverse()
            print(lis)

            for i in range(len(lis)):
                lis[i]=str(lis[i])
            # lis.reverse()
            # print(lis,"this is input lis",end=",")
            for i in range(1,len(inp),1):
                # print(lis, "this is loop lis")

                x= lis[i-1]+lis[i]
                y= lis[i]+lis[i-1]
                ix,iy=int(x),int(y)
                if ix>iy:
                    lis[i]=x
                else:
                    lis[i]=y

            for i in range(len(rlis)):
                rlis[i]=str(rlis[i])
            # rlis.reverse()
            # print(rlis, "this is input rlis", end=",")
            for i in range(1, len(inp), 1):
                # print(rlis, "this is loop rlis")

                x = rlis[i - 1] + rlis[i]
                y = rlis[i] + rlis[i - 1]
                ix, iy = int(x), int(y)
                if ix > iy:
                    rlis[i] = x
                else:
                    rlis[i] = y
            # print(lis[-1],"lis last",op)
            a=int(rlis[-1])
            b=int(lis[-1])
            maxx=max(a,b)
            maxx=str(maxx)
            
            return maxx
        return help(nums)