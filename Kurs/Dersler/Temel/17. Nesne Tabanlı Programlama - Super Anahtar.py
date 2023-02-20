"""
Super anahtar kelimesi özellikle override ettiğimiz bir metodun içinde aynı zamanda miras aldığımız
ir metodu kullanmak istersek kullanılabilir.
Yani super en genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan kullanmamızı sağlar.
"""


class Worker():
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def worker_info(self):
        print(f"""
        Name: {self.name}
        Salary: {self.salary}
        Department: {self.department}
        """)

    def chanching_department(self, new_department):
        self.department = new_department


class Manager(Worker):
    def __init__(self, name, salary, department, nmbofmanaged):
        super().__init__(name, salary,
                         department)  # burada override ettik ama yine de workerdaki init'i kullanmak isteyebilirim
        self.nmbofmanaged = nmbofmanaged

    def worker_info(self):
        print(f"""
        Name: {self.name}
        Salary: {self.salary}
        Department: {self.department}
        Number of Managed: {self.nmbofmanaged}""")

    def change_salary(self, newsalary):
        self.salary = newsalary


manager1 = Manager("Ali Çiçekçioğlu", 3000, "IT", 5)  # ilk 3 değer worker'dan, nmbofmanaged ise Manager'dan çekildi.
