import datetime as dt

#For records
class Record:


    def __init__(self, amount, comment, date = None ):
        self.amount = amount #sum money|calories
        self.comment = comment # comments
        self.date = date
        if self.date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(self.date, '%d.%m.%Y').date() 
        

#Main Calc
class Calculator:


    def __init__(self, limit):
        self.limit = limit
        self.records=[]
        print(f"Лимит на сегодня: {limit}")
    
    def add_record(self, record):
        self.records.append(record)#пустой список records для записей
    date_today = dt.date.today()  
    week = dt.timedelta(days=7)
    dates_week = date_today - week
    
    #Total cash spent today:
    def get_today_stats(self):
        return sum(r_i.amount 
            for r_i in self.records 
            if (r_i.date == self.date_today ))
    
    def get_week_stats(self):
        return sum(r_num.amount 
            for r_num in self.records 
            if (r_num.date >= self.dates_week 
            and (r_num.date <= self.date_today)))


#Money calc:
class CashCalculator(Calculator):


    USD_RATE=73.5
    EURO_RATE=89.5
    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            course=1
            value='руб'
        elif currency == 'usd':
            course = self.USD_RATE
            value='USD'
        elif currency == 'eur':
            course = self.EURO_RATE
            value='Euro'
        else:
            return 'Такая валюта не предусмотрена'
        if self.limit > self.get_today_stats():
            cash_remained = round(
                self.limit/course - self.get_today_stats()/course, 2
                )
            return f'На сегодня осталось {cash_remained} {value}'
        elif self.limit/course == self.get_today_stats()/course:
            return 'Денег нет, держись'
        else: 
            cash_remained = abs(round(
                self.limit/course - self.get_today_stats()/course, 2)
                )
            return f'Денег нет, держись: твой долг - {cash_remained} {value}'

#Calories Calc       
class CaloriesCalculator(Calculator):


    def __init__(self, limit):
        super().__init__(limit)
    #Calories were eaten today:

    def get_calories_remained(self):
        if self.limit > self.get_today_stats() > 0:
            calories_remained = self.limit - self.get_today_stats()
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал'
                
        else: 
            return 'Хватит есть!'