hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h > 40:
    regpay = h * r
    otpay = (h - 40) * (r * 0.5)
    pay = regpay + otpay
    print(pay)
else:
    pay = h * r
    print(pay)
