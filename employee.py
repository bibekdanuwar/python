class Employee:
    def __init__(self, empno, name, dept):
        self.empno = empno
        self.name = name
        self.dept = dept

    def disp_info(self):
        print("従業員番号:" + self.empno)
        print("氏名:" + self.name)
        print("部署名:" + self.dept)