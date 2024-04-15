def convert(num,to_num,from_num):
	sys={"bin":2,"oct":8,"dec":10,"hex":16}
	base=sys[to_num]
	int_num=int(num)
	float_num=num%1
	int_part=""
	float_part=""
	while int_num!=0:
		int_part=str(int_num%base)+int_part
		int_num=int_num//base
	while float_num!=0.0 and len(str(float_part))<16:
		temp=float_num*base
		float_part+=str(int(temp))
		float_num=temp%1

	return str(int_part)+"."+str(float_part)

#print(convert(100,"bin"))

def convert(num,to_num,from_num="dec"):
    num_sys={"bin":bin,"oct":oct,"dec":int,"hex":hex}
    if from_num=="dec":
        return (str(num_sys[to_num](num)))
    elif from_num=="hex"
#a=convert(1234,"oct")
#print(a,type(a))

