class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id: int) -> int:
        hashmap = {}
        for emp in employees:
            hashmap[emp.id] = emp
        return self.helper(hashmap[id], hashmap)

    def helper(self, employee, hashmap):
        val = employee.importance
        for i in employee.subordinates:
             val += self.helper(hashmap[i], hashmap)
        return val