class date:
    def __init__(self,h,b,t):
        self.d=h
        self.m=b
        self.y=t
def day(D):
        return D.d
def month(D):
        return D.m
def year(D):
        return D.y
def IsKabisat(a) :
    return (a%4==0) and ((a%100!=0) or (a//400==0))


def NextNDay(D,N):
    if N==0:
        return (day(D),month(D),year(D))
    else :
        if month(D)==1 or month(D)==3 or month(D)==5 or month(D)==7 or month(D)==8 or month(D)==10 :
            if day(D)<31:
                return NextNDay(date(day(D)+1,month(D),year(D)),N-1)
            else :
                return NextNDay(date(1,month(D)+1,year(D)),N-1)

        elif month(D)==2 :
            if day(D)<28 :
                return NextNDay(date(day(D)+1,month(D),year(D)),N-1)
            elif day(D)+N==28 and IsKabisat(year(D)):
                return NextNDay(date(day(D)+1,month(D),year(D)),N-1)
            else :
                return NextNDay(date(1,month(D)+1,year(D)),N-1)

        elif month(D)==4 or month(D)==6 or month(D)==9 or month(D)==11:
            if day(D)<30:
                return NextNDay(date(day(D)+1,month(D),year(D)),N-1)
            else :
                return NextNDay(date(1,month(D)+1,year(D)),N-1)

        elif month(D)==12:
            if day(D)<31:
                return NextNDay(date(day(D)+1,month(D),year(D)),N-1)
            else :
                return NextNDay(date(1,1,year(D)+1),N-1)

        
D=date(1,1,1990)
print(NextNDay(D,365))

