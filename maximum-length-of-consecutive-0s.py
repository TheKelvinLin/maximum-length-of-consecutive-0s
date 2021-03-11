def maxZeros(nums):
    zeroLength = 0
    maxLength = 0
    times = 1
    for item in nums:
        if item == 0:
            zeroLength += 1
        if item == 1 or times == len(nums):
            if maxLength < zeroLength:
                maxLength = zeroLength
                zeroLength = 0

        times += 1

    print(maxLength)

maxZeros([1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # Get answer 5
maxZeros([1, 1, 1, 1, 1]) # Get answer 0
maxZeros([0, 0, 1, 0, 0]) # Get answer 2
