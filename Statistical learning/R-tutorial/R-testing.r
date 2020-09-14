2 + 3
2 * 6
3 * 10^4 - 3 * 5^2
10^2 - 1
10^(2 - 1)
sqrt(9)
log(3, base = 10)
`?`(log)
log
log10(3)
log(3)
exp(34)
gamma(3)
factorial(5)
choose(10, 4)
1:4
c(1, 2, 3, 4)
seq(from = 1, to = 4, by = 1)
sum(1:5)
prod(1:5)
heights = c(192, 185, 174, 195, 173)
shoes = c(46, 43, 40, 45, 40)
ratio <-heights/shoes
ratio

x = c(1,2,3)
typeof(x)
y = c("a","b","c")
typeof(y)
u = c("1","2","3")
typeof(u)
v=as.numeric(u)
typeof(v)
z=c("red", 1, "yellow", 2)
typeof(z)

'?'(factor)
gender = factor(c("male","female","female","male"))

gender
sum (gender=="male")
table (gender)



x = 1:5
x = seq(from = 1, to = 5, length = 5)
x = c(1, 2, 3, 4, 5)
'?'("%in%")
3 %in% x
2 %in% x
6 %in% x
x[2]
x[2] = 10
x[3:4] = 0
x[-2] = 1
x[-3] = 3
x[c(1, 4)] = 4
x[x > 4] = 10
x
y = log(x)
z = exp(y)
z = z + y
y = x * y
z = y/x
a = t(x) %*% y # t(): transpose

min(x)
max(x)
sum(x)
mean(x)
var(x)
length(x)
sort(x)
order(x)
'?'(order)
sort(x) == x[order(x)]
sample(1:10)
sample(1:10, replace = T)
'?'(sample)

x=1:5
y=2
x-y
5*x
z=10:15
w=1:2
z-w

#Matrix operations 

A = matrix(1:6, nrow=3, ncol=2)
A
B = matrix(1:6, nrow=2, ncol=3,byrow=T)
B
A%*%B
B%*%A
A*t(B)
x1 = 1:3
x2 = c(3,6,6)
x3 = c(1,2,3)
A = cbind(x1, x2, x3)
A
B =rbind(x1,x2,x3)
B
dim(A)
nrow(A)
ncol(A)
apply(A,1,sum)
apply(A,2,sum)
sum(diag(A))
A=diag(1:3)
A
solve(A)
det(A)


# Plotting in R

x <- seq(-4,4,length=500)
y <- x^2-1
plot(x,y,type ="l", main ="myplot",xlab="x",ylab="y")
abline(v=3)
abline(h=5)
# learn ggplot2

# making a funciton
myfunc <-function(x,y)
{
  n <- c(length(x),length(y))
  m <- c(sum(x),sum(y))
  p <- m/n
  return(p)
}
a= 1:10
b=seq(from=0.1,to=1,length=10)
p=myfunc(x=a,y=b)

lett= c('a','b','c','d','f','g','h')

for (i in 1:length(lett))
{
  print("working with:")
  print(lett[i])
  if (lett[i]=='b')
  {
    print(lett[i])
  } 
  else if (lett[i]=='d)')
  {
    print(lett[i])
  } 
  else
  {
    print("not b nor d")
  }
}

# lists and dataframes

a=c('male','female','male','female')
b=matrix(c(1:6),ncol=2)
c=rnorm(100,mean=0,sd=1)
li=list(a=a,b=b,c=c)
li[1]
li[2]
li[3]
li
li$a
li[[2]][1,2]

Sick = c(0, 1, 1, 0, 0, 0, 1, 0)
Age = c(50, 15, 39, 35, 26, 20, 10, 69)
Sex = factor(c("male", "female", "female", "male", "male", "male", "female", 
               "male"))
df = data.frame(Sick = Sick, Age = Age, Sex = Sex)

df$Sick
df$Age
df$Sex
write.csv(df,file="testdata.csv",row.names = F)
getwd()
list.files()
mydf= read.csv(file="testdata.csv",header = T)
mydf
write.table(df,file="testtable.txt",sep="\t", row.names = F)
list.files()
mytable=read.table(file="testtable.txt",sep="/t",header=)
source("R-testing.r")
source("https://www.math.ntnu.no/emner/TMA4268/2019v/1Intro/RintroPartB.R", 
       echo = TRUE)

ds=rnorm(100)
boxplot(ds)
dev.copy2pdf(file="testplot.pdf")
pdf