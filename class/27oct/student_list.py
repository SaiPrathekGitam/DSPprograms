class Student:
    def __init__(self, rno, name, marks):
            self.rno = rno
            self.name = name
            self.marks = marks
            self.next = None

def print_list(t):
    print('The Student Details are :')
    while(t):
        print(' Roll Number :',t.rno, 'Name :', t.name, 'Marks: ',t.marks)
        t = t.next

head = None
for i in range(2):
    r = int(input('Enter Roll Number : '))
    n = input('Enter Name : ')
    m= list(map(int, input('Enter Marks In 3 Subjects : ').split()))
    if head == None:
        head = s = Student(r, n, m)
    else:
        s.next = Student(r, n, m)
        s = s.next

print_list(head)