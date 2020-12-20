import datetime as dt


class Record:
    '''
    The class required for the records.
    '''
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if self.date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(self.date, '%d.%m.%Y').date()


class Calculator:
    '''
    The class to which new entries are added.
    Which accepts a calorie/money limit.
    And calculates the amount spent during this period.
    '''
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return sum(record_i.amount
                   for record_i in self.records
                   if (record_i.date == dt.date.today()))

    def get_week_stats(self):
        return sum(record_n.amount
                   for record_n in self.records
                   if (record_n.date >= dt.date.today() - dt.timedelta(days=7)
                       and (record_n.date <= dt.date.today())))


class CashCalculator(Calculator):
    '''
    Money calculator.
    Calculates the money spent
    and compares it with the limit for today.
    '''
    USD_RATE = 60.0
    EURO_RATE = 70.0
    dictionary_rates = {
        'rub': (1, 'руб'),
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'Euro')
        }

    def get_today_cash_remained(self, currency):
        cash_rate, cash_name = self.dictionary_rates[currency]
        cash_today = self.limit - self.get_today_stats()
        remain = round((cash_today)/cash_rate, 2)
        if cash_today > 0:
            return f'На сегодня осталось {remain} {cash_name}'
        elif cash_today < 0:
            return f'Денег нет, держись: твой долг - {abs(remain)} {cash_name}'
        return 'Денег нет, держись'


class CaloriesCalculator(Calculator):
    '''
    Calorie calculator.
    Calculates the calories consumed
    and compares it with the limit for today.
    '''
    def get_calories_remained(self):
        if self.limit > self.get_today_stats() > 0:
            calories_remained = self.limit - self.get_today_stats()
            return ('Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {calories_remained} кКал')
        return 'Хватит есть!'
