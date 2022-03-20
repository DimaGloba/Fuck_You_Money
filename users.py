class Users:
    name = None
    monthly_income = None # доход
    monthly_expense = None # расход

    def __init__(self, name, monthly_income, monthly_expense):
        self.name = name
        self.monthly_income = monthly_income
        self.monthly_expense = monthly_expense

