# Money and calories calculator

The project contains two calculators: for calculating money and calories. There is no front end.
# Money calculator, functions:
Saves a new expense record.
Counts how much money was spent today.
Determines how much more money can be spent today in rubles, dollars or euros.
* Modify: it is possible to create a dictionary for any currency.
Counts how much money was spent in the last 7 days.
# Calorie calculator, functions:
Saves a new meal record
Counts how many calories you have eaten today
Determines how many more calories you can / need to get today
Counts how many calories you got in the last 7 days
Calculators have many overlapping functions: they know how to store some kind of records (about food or money, but in fact - numbers and dates), know the daily limit (how much money can be spent per day or how many calories you can get) and summarize records for specific dates ...
All this common functionality is in the parent Calculator class.

To make it easier to create records, a separate Record class has been created.
