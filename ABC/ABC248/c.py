import math

class Solution:
    def DFS(self, res, tmp, nums, k, n, w, su, MAX):

        if su==n and k==len(tmp):
            res.append(tmp.copy())
            return
        elif su>n or len(tmp)>k or w> MAX:
            return
        for i in range(w,len(nums)):
            su+=nums[i]
            tmp.append(nums[i])
            self.DFS(res,tmp,nums,k,n,i+1,su,MAX)
            del tmp[-1]
            su-=nums[i]

    def combinationSum3(self, k, n, MAX):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res=[]
        tmp=[]
        su=0
        nums=[1,2,3,4,5,6,7,8,9]
        self.DFS(res,tmp,nums,k,n,0,su,MAX)
        return res

def main():
    n, m, k = map(int, input().split())
    ans = Solution()
    ans = ans.combinationSum3(k=n, n=k, MAX=m)
    print(ans)



"""
def comb(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

def main():
    n, m, k = map(int, input().split())
    M = 998244353

    res = comb(k+n, n)

    print(res % M)
"""


if __name__ == "__main__":
    main()