import fractions
import speedtest as st
import datetime

def frac(x):
    if x.numerator == 0 or x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"

def speedtest():
    s = st.Speedtest()
    down = round(s.download()/1048576,3)
    up = round(s.upload()/1048576,3)
    print(f"Download Speed: {down} Mbps")
    print(f"Upload Speed: {up} Mbps")

def checkspeedtest():
    s = st.Speedtest()
    down = round(s.download()/1048576,3)
    if down > 30:
        up = round(s.upload()/1048576,3)
        if up > 30:
            print(f"Download Speed: {down} Mbps")
            print(f"Upload Speed: {up} Mbps")
        else:
            raise ValueError("Not enough Speed (<30Mbps)")
    else:
        raise ValueError("Not enough Speed (<30Mbps)")
    
class dateandtime:
    def now(self):
        print(datetime.datetime.now())
    def time(self):
        print(datetime.datetime.now().time())
    def date(self):
        print(datetime.datetime.now().date())