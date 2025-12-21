class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while counter < len(students):
            if sandwiches[0] == students[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0
            else:
                students.append(students.pop(0))
                counter = counter + 1
        return len(students)
