class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        input => two strings => s,t
        anagram => every character of s is the same as t regardless the order of it then it is anagram.
        output => boolean => True, False
        constraint more than 1 character, lowercase

        method #1
        - sort the string
        - for loop and check
        Time complexity => O(n log n)

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return s==t

        method #2
        - count the frequency of the s
        - compare it with t
        Time complexity => O(n)

        Note : different between
                - in count => in count.keys()
                - list => dictionary views
                - count.__contains__(key) => count.keys().__contains__

        count = {}
        for chars in s:
            # if the character is not in the dictionary then put that char into a key and the value would be 1
            if chars not in count:
                count[chars] = 1
                continue
            count[chars] += 1

        # compare the frequency of each character in t
        for chart in t:
            if chart in count:
                count[chart] -= 1

        # check if every value of the character is 0
        for value in count.values():
            if value != 0:
                return False
        return True
        """
