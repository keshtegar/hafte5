class Time:
    def __init__(self,h,m,s):
       self.h=h
       self.m=m
       self.s=s

    def show(self):
        print(self.h,":",self.m,":",self.s)

    def sum(self,t2):
        result=Time(None,None,None)
        result.h=self.h+t2.h
        result.m=self.m+t2.m
        result.s=self.s+t2.s
        if result.m>=60:
            result.m-=60
            result.m+=1
        if result.s>=60:
            result.s-=60
            result.s+=1
        return result
    def sub(self,t2):
        result=Time(None,None,None)
        result.h=self.h-t2.h
        result.m=self.m-t2.m
        result.s=self.s-t2.s
        if result.m<0:
            result.m+=60
            result.h-=1
        if result.s<0:
            result.s+=60
            result.m-=1
        return result
    def convert_time_to_srcond(self):
        convert=self.h*3600+self.m*60+self.s
        return convert
    def convert_second_to_time(self):     
        h=int(self/3600)  
        m=int((self-h*3600)/60)
        second=int((self-h*3600-m*60))
        return [h,m,s] 


time_1={"h":10,"m":20,"s":25}
print("Time_1 : " , time_1 ) 
time_1=Time(10,20,25)

time_2={"h":8,"m":30,"s":5}
print("Time_2 : ", time_2 ) 
time_2=Time(8,30,5)




s=time_1.sum(time_2)
sub=time_1.sub(time_2)
conv_timetos=time_1.convert_time_to_srcond()
conv_stotime=time_1.convert_second_to_time()
s.show()
sub.show()
print("Time Convert to Seconds:  \n" "Time Equal To= " , conv_timetos ,"Seconds" )
