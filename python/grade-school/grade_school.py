from operator import itemgetter
class School:

    def __init__(self):

        self.data = {}


    def add_student(self, name, grade):

        self.data.setdefault(grade, [])
        self.data[grade].append(name)


    def roster(self):

        if self.data:
            sorted_data = dict(sorted(self.data.items(), key=itemgetter(0)))
            all_students = []
            for students in sorted_data.values():
                students.sort()
                all_students += students
            return all_students
        return []
            

    def grade(self, grade_number):
        
        try:
            aux = self.data[grade_number].copy()
            aux.sort()
            return aux
        except KeyError:
            return []
