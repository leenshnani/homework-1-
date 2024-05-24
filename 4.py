class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number  # رقم الحساب
        self.account_holder = account_holder  # صاحب الحساب
        self.balance = 0.0  # الرصيد المبدئي مصفر

    def deposit(self, amount):
        self.balance += amount  # زيادة الرصيد بقيمة المبلغ المودع

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount  # خصم المبلغ المسحوب من الرصيد
        else:
            print("رصيد غير كافٍ.")

    def get_balance(self):
        return self.balance  # إرجاع الرصيد


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate  # نسبة الفائدة

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100  # حساب المبلغ المستحق كفائدة بناءً على نسبة الفائدة
        self.balance += interest  # زيادة الرصيد بقيمة المبلغ المستحق كفائدة

    def print(self):
        print("الرصيد الحالي:", self.balance)
        print("نسبة الفائدة:", self.interest_rate)


# إنشاء نموذج من فئة BankAccount
bank_acc = BankAccount("2971", "لين شناني")

# إيداع 1000 دولار
bank_acc.deposit(1000)
print("الرصيد الحالي:", bank_acc.get_balance())

# سحب 500 دولار
bank_acc.withdraw(500)
print("الرصيد الحالي:", bank_acc.get_balance())

# إنشاء نموذج من فئة SavingsAccount
savings_acc = SavingsAccount("2222", "احمد محمد", 5)

# إيداع 2000 دولار
savings_acc.deposit(2000)
print("الرصيد الحالي ونسبة الفائدة قبل تطبيق الفائدة:")
savings_acc.print()

# تطبيق الفائدة
savings_acc.apply_interest()
print("الرصيد الحالي ونسبة الفائدة بعد تطبيق الفائدة:")
savings_acc.print()
