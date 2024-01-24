mydata = [
    (60,1),
    (40,2)
]

freq = lambda data : sum([ f for ( d, f ) in data ])

def mean( data, func = lambda x : x ):
    data = [(func(d),f) for (d,f) in data]
    print(data)
    summation = sum([ f * d for ( d, f ) in data ])
    return summation / freq( data )

def var( data, func = lambda x : x ):
    data = [(func(d),f) for (d,f) in data]
    avg = mean( data )
    vary = sum([ f * ( d - avg ) ** 2 for ( d, f ) in data ])
    return vary / freq( data )

def foo(x): return 0.95*x-1

if __name__ == "__main__":
    print(mean(mydata,foo))
    print(var(mydata,foo))