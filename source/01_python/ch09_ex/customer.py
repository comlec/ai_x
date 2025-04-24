class Customer:
    '고객데이터와 as_dic(), to_list_style(txt백업시), __str__()'
    def __init__(self, name, phone, email, age, grade, etc):
        self.name = name
        self.phone = phone
        self.email = email
        self.age  = age
        self.grade = grade
        self.etc = etc
    def as_dic(self):
        return {"name":self.name, 
                "phone":self.phone, 
                "email":self.email,
                "age":self.age, 
                "grade":self.grade, 
                "etc":self.etc}
    def to_list_style(self):
        # return "홍길동, 010-9999-9999, a@a.com, 30, 3, 까칠해"
#         return "{}, {}, {}, {}, {}, {}".format(self.name, self.phone, self.email,
#                                               self.age, self.grade, self.etc)
        temp = [self.name, 
                self.phone, 
                self.email, 
                str(self.age), 
                str(self.grade), 
                self.etc]
        return ', '.join(temp)
    def __str__(self):
        # return "  *** 홍길동, 010-9999-9999, a@a.com, 30, 까칠해"
        return "{:>5}\t{:3}\t{:13}\t{:15}\t{:3}\t{}".format('*'*self.grade,
                       self.name, self.phone, self.email, self.age, self.etc)