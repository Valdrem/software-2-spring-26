from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<integer>')

def check(integer):

    integer = int(integer)
    initial_integer = int(integer)

    integer_array = []

    # loops initial integer as much times to test it by all possible divisions
    while integer > 0:
        integer_divided = initial_integer / integer
        integer = integer - 1
        integer_array.append(integer_divided)

    # checking the array list whether it contains more than 2 separate numbers that are integer
    full_numbers = [number for number in integer_array if number % 1 == 0]

    if initial_integer > 1 and len(full_numbers) < 3:
        answr = {
            "Number": initial_integer,
            "isPrime": True
        }
    else:
        answr = {
            "Number": initial_integer,
            "isPrime": False
        }

    return answr

app.run(use_reloader=True, host='127.0.0.1', port=3000)