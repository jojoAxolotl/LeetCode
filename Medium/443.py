# 443. String Compression
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        """
        idea
        func _helper1 traslate int to List[str]
        func _helper2 add the repeatingChar and amount to char(List[str])
        """

        def _helper1(amount):
            '''
            constraint: amount > 0
            '''
            if amount // 10 == 0:
                return [str(amount % 10)]
            else:
                return _helper1(amount // 10) + [str(amount % 10)]
        
        def _helper2 (correctPtr, repeatingChar, amount):
            # If amount is 1, just add the character
            if amount == 1:
                chars[correctPtr] = repeatingChar
                correctPtr += 1
            else: # For amount > 1, replace with character and amount
                replaceList = [repeatingChar] + _helper1(amount)
                chars[correctPtr:correctPtr+len(replaceList)] = replaceList
                correctPtr += len(replaceList)
            return correctPtr
        
        repeatingChar = chars[0]
        amount = 0
        correctPtr = 0

        # Split chars into consecutive repeating characters
        for char in chars:
            if char == repeatingChar:
                amount += 1
            else:
                correctPtr = _helper2(correctPtr, repeatingChar, amount)
                repeatingChar = char
                amount = 1
        
        # Handle the last sequence of characters
        correctPtr = _helper2(correctPtr, repeatingChar, amount)
        
        # Trim the chars list to the new length and return the length
        # chars[:] = chars[:correctPtr]
        return correctPtr