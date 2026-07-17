class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        def gcd(a,b):
            while(b>0):
                temp=b
                b=a%b
                a=temp
            return a
        gcdP=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                gcdP.append(gcd(nums[i],nums[j]))
        gcdP.sort()
        a=[]
        for i in range(len(queries)):
            a.append(gcdP[queries[i]])
        return a

        """

        max_num = max(nums)

        # Frequency array
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1

        # Count numbers divisible by each divisor
        divisible = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            for multiple in range(d, max_num + 1, d):
                divisible[d] += freq[multiple]

        # Count pairs with gcd exactly d
        gcd_count = [0] * (max_num + 1)

        for d in range(max_num, 0, -1):
            cnt = divisible[d]
            pairs = cnt * (cnt - 1) // 2

            for multiple in range(2 * d, max_num + 1, d):
                pairs -= gcd_count[multiple]

            gcd_count[d] = pairs

        # Prefix sums
        prefix = []
        values = []
        total = 0

        for d in range(1, max_num + 1):
            if gcd_count[d] > 0:
                total += gcd_count[d]
                prefix.append(total)
                values.append(d)

        # Answer queries using binary search
        ans = []

        for q in queries:
            target = q + 1

            left = 0
            right = len(prefix) - 1

            while left <= right:
                mid = (left + right) // 2

                if prefix[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            ans.append(values[left])

        return ans
        