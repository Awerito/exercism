STUDENTS = [
        'Alice'  , 'Bob'    , 'Charlie' , 'David'   ,
        'Eve'    , 'Fred'   , 'Ginny'   , 'Harriet' ,
        'Ileana' , 'Joseph' , 'Kincaid' , 'Larry'
]

FLOWERS = {
        'G': 'Grass'  , 'R': 'Radishes' ,
        'C': 'Clover' , 'V': 'Violets'
}

class Garden:

    def __init__(self, diagram, students=STUDENTS):

        students.sort()
        self.students = students
        self.diagram = diagram.split()


    def plants(self, name):
        
        flowers = []
        index = self.students.index(name) * 2
        flowers.append(FLOWERS[self.diagram[0][index]])
        flowers.append(FLOWERS[self.diagram[0][index+1]])
        flowers.append(FLOWERS[self.diagram[1][index]])
        flowers.append(FLOWERS[self.diagram[1][index+1]])
        return flowers
