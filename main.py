nums = [10, 20, 30]
# nums_bak = nums
nums_bak = nums.copy()
nums[0] = 100

# どちらも100,20,30が表示される コピーメソッドを使わない
print(nums)
print(nums_bak)