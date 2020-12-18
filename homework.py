import datetime as dt


# For records
class Record:
    def __init__(self, amount, comment, date=None):
        # sum money|calories
        self.amount = amount
        # comments
        self.comment = comment
        self.date = date
        if self.date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(self.date, '%d.%m.%Y').date()


# Main Calc
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    # Total cash spent today:
    def get_today_stats(self):
        return sum(r_i.amount
                   for r_i in self.records
                   if (r_i.date == dt.date.today()))

    # Total cash spent week:
    def get_week_stats(self):
        return sum(r_num.amount
                   for r_num in self.records
                   if (r_num.date >= dt.date.today() - dt.timedelta(days=7)
                       and (r_num.date <= dt.date.today())))


# Money calc:
class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0
    dictionary_rates = {
        'rub': (1, 'руб'),
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'Euro')
        }

    def get_today_cash_remained(self, currency):
        cash_today = self.limit - self.get_today_stats()
        if cash_today > 0:
            return f'На сегодня осталось {round((cash_today)/self.dictionary_rates[currency][0], 2)} {self.dictionary_rates[currency][1]}'
        elif cash_today < 0:
            return f'Денег нет, держись: твой долг - {abs(round((cash_today)/self.dictionary_rates[currency][0], 2))} {self.dictionary_rates[currency][1]}'
        return 'Денег нет, держись'


# Calories calc:
class CaloriesCalculator(Calculator):
    # Calories were eaten today:
    def get_calories_remained(self):
        if self.limit > self.get_today_stats() > 0:
            calories_remained = self.limit - self.get_today_stats()
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал'
        return 'Хватит есть!'
