import re, socket, time

month_to_number = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
                   'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
number_to_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                   8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

sock = socket.socket()
sock.connect(('neoannophobia.chal.imaginaryctf.org', 1337))
time.sleep(1)

while True:
    recv = sock.recv(1 << 16).decode()
    print(recv, end = '')
    try:
        date = re.findall(r'.+ \d+', recv)[-1]
    except:
        break
    month = month_to_number[date.split()[0]]
    day = int(date.split()[1])
    if day - month < 19:
        day = month + 19
    elif day - month == 19:
        month += 1
    else:
        month = day - 19
    answer = number_to_month[month] + f' {day}\n'
    sock.send(answer.encode())
    print(answer, end = '')
