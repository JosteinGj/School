
library(ggplot2)
n = 10
p = 0.2
probs = dbinom(0:10, n, p)
df =data.frame(x = 0:10, y = probs)
pl <- ggplot(data = df,aes(x = x, y = y)) + geom_bar(stat = "identity")+ theme_minimal()
pl
