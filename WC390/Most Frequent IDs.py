# 100258. Most Frequent IDs
class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        idCounts = {}  # Store id and its frequency
        ans = []  # Most frequent id's frequency in each step
        maxFreq = 0  # Max frequency seen so far
        maxIds = set()  # Set of IDs with the max frequency

        for idx in range(len(nums)):
            curId = nums[idx]
            curFreqChange = freq[idx]
            # Update the frequency of the current ID
            idCounts[curId] = idCounts.get(curId, 0) + curFreqChange

            # If the current ID is in maxIds or potentially becomes the new max
            if curId in maxIds or idCounts[curId] >= maxFreq:
                if idCounts[curId] > maxFreq:
                    # New maximum frequency found
                    maxFreq = idCounts[curId]
                    maxIds = {curId}
                elif idCounts[curId] == maxFreq:
                    # Current ID matches the max frequency, add to maxIds
                    maxIds.add(curId)
                else:
                    # Current ID's frequency is less than max and was part of maxIds
                    if idCounts[curId] < maxFreq:
                        maxIds.remove(curId)
                        if not maxIds:  # Need to find the new max if this was the only maxId
                            maxFreq = max(idCounts.values())
                            maxIds = {id for id, count in idCounts.items() if count == maxFreq}
            ans.append(maxFreq if maxIds else 0)

        return ans