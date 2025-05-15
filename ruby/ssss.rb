require "pry"

p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"


def serial_average(str)
    
    rta = str.split("-")
    rta[0]+"-"+((rta[1].to_f+rta[2].to_f).fdiv(2.0)).round(2).to_s
end

p serial_average('002-10.00-20.00')


p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"
p "-----------"
def strike(str)
    "<strike>"+str.to_s+"</strike>"
end    

def mask_article(string, array)
    array.each{|x| string.gsub!(x,strike(x))}
    string
end

p strike("Meow!")
p mask_article("Hello World! This is crap!", ["crap"])

p "-------------------"
p "-------------------"
p "-------------------"


p mask_article("Decisively advantages nor expression unpleasing she led met", ["unpleasing"])
p mask_article("Joy fond many ham high seen this. ", ["fond", "ham"])


def prime? n
    # 1.upto(n).select{|x|  n%x == 0}.count == 1? true : false
    2.upto(n).select{|x|  n%x == 0}.count == 1? true : falsesdf
    
end

(1..10).each{|x| p "#{x}  #{prime?(x)}" }




