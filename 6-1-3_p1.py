from employee import Employee

empno = input("従業員番号を入力してください=>")
name = input("氏名を入力してください=>")
dept = input("部署名を入力してください=>")

emp = Employee(empno, name, dept)
emp.disp_info()