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
2 %in% x
6 %in% x
x[2]
x[2] = 10
x[3:4] = 0
x[-2] = 1
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
sort(x) == x[order(x)]
sample(1:10)
sample(1:10, replace = T)
  
