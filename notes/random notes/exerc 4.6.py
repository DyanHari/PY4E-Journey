def computepay(h, r):
    return h * r

hrs = input("Enter Hours:")
rate = input("Enter rate:")

hours = float(hrs)
rates = float(rate)

if hours > 40:
    p = computepay(hours, rates)
    otpay = computepay(hours - 40, rates - 5.25)
    gross = p + otpay
    print("Pay", gross)
else:
    p = computepay(hours, rates)
    print("Pay", p)


