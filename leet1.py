
nums= [3,2,4]
target = 6
def twosums(nums, target):
    solution = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                solution.append(i)
                solution.append(j)
                return solution 
    return []  

loesung=twosums(nums,target)
print(loesung)

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    solution.append((nums[i], nums[j]))
        return solution
"""


"""

solution ChatGPT:
def two_sum(nums, target):
    # Erstelle ein Dictionary, um Werte und ihre Indizes zu speichern
    num_dict = {}
    # Durchlaufe alle Elemente und ihre Indizes
    for index, num in enumerate(nums):
        # Berechne das benötigte Komplement, um das Ziel zu erreichen
        complement = target - num
        # Überprüfe, ob das Komplement bereits im Dictionary vorhanden ist
        if complement in num_dict:
            # Wenn ja, gibt die Indizes des aktuellen und des komplementären Wertes zurück
            return [num_dict[complement], index]
        # Speichere den aktuellen Wert und seinen Index im Dictionary
        num_dict[num] = index
    # Wenn keine Lösung gefunden wird (sollte laut Aufgabenstellung nicht vorkommen), gebe eine leere Liste zurück
    return []

# Beispielaufrufe
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]

nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))  # Output: [1, 2]

nums = [3, 3]
target = 6
print(two_sum(nums, target))  # Output: [0, 1]
"""