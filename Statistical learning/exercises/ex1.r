---
title: "Statistical learning rec ex 2"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## R Markdown

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:

```{r cars}
summary(cars)
```

## Including Plots

You can also embed plots, for example:

```{r pressure, echo=FALSE}
plot(pressure)
```

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.


problem 1)
a real life application of classification would be for example handwritten digit recognition. in which the predictors would be a picture or spesifically the pixels of said picture. and the response would be an identifer ie {1,2,3,4,5,6,7,8,9} the goal is then inference.

problem 2)
regression would be useful to find a feature in a data set. for example estimating a value based on sample data. the predictors would then be the sample data and the response would be the regression coefficients. the goal is usually prediction but it depends on the use case.

problem 3)
a) 
To minimize the test data we need to strike a balance between flexibility and rigidity, as the rigid methods will introduce more bias while the flexible methods introduce more variance.

b)
a small variance exculdes an overfit, if the system is overfitted the variance will dominate, but if the system is underfitted or appropriately fitted the variance will remain small.

c)
over fitting is when we ajust our model after the random noise inherent in the sample data. while under fitting is being to rigid so we dont catch the features of the data.

Bias variance trade off:

E([y-\hat{f}(x)]²)=Var(\epsilon)+ var(\hat{f})+ E[y-\hat{f}]²

an overfitted system is flexible enuogh to allow us to get very close to the sample data, thus the bias value will be very small, but between points the estimate will vary wildly, thus introduceint a lot of variance.
The underfitted system is not flexible enught to accomodate all the changes in the sample data and will thus have a large bias but in turn doesnt change as radically as the over fitted system and thus will have a low variance.





Problem 4)


```{r}
library(ISLR)
library(GGally)
library(ggplot2)
data(Auto)

ranges  <- sapply(Auto[1:8],range)
ranges
means <- sapply(Auto[1:8],mean)
sds <- sapply(Auto[1:8], sd)
reducedAuto <- Auto[-c(10:85),]
redrange <- sapply(reducedAuto[1:8],range)
redmeans <- sapply(reducedAuto[1:8],mean)
redsds <- sapply(reducedAuto[1:8],sd)
ggpairs(Auto,1:8,title="Auto data")

ggplot(Auto, aes(name , mpg))+geom_boxplot()+theme_minimal()


```
the dimensons of the data are 392x9 ie 392 obeservations of 9 variables.
```{r}
ggplot(Auto, aes(x=variable, mpg)) + geom_boxplot(aes(x= as.factor(cylinders)))  + theme_minimal()

```
number of cylinders seems to have an effect, the effect is not linear

```{r}
ggplot(Auto, aes(x=variable, mpg))+geom_boxplot(aes(as.factor(x=horsepower)))
```
horsepower seems to be almost linearly correlated

```{r}
quant= c(1,3,4,5,6,7)
covmat=cov(Auto[,quant])
covtocor =function(covmat)
{
  cormat = covmat
  cormat
  covmat
  for (row in 1:nrow(covmat))
  {
    for (col in 1:ncol(covmat))
    {
      cormat[row, col] = covmat[row, col] / sqrt(covmat[row, row] * covmat[col, col])
    }
  }
  return(cormat)
}

cormat1 = covtocor(covmat)
cormat2 = cor(Auto[,quant])
diff=cormat1-cormat2
```
all values in the difference is within machine epsilon or very close





Problem 5)
```{r}
library(MASS)
y1 =mvrnorm(1000,c(2,3),matrix(c(1, 0, 0, 1),nrow=2,ncol=2))
y2 =mvrnorm(1000,c(2,3),matrix(c(1, 0, 0, 5),nrow=2,ncol=2))
y3 =mvrnorm(1000,c(2,3),matrix(c(1, 2, 2, 5),nrow=2,ncol=2))
y4 =mvrnorm(1000,c(2,3),matrix(c(1, -2, -2, 5),nrow=2,ncol=2))
df=data.frame(y1,y2,y3,y4)
ggplot(df,aes(y1[,1],y1[,2]))+geom_point()
ggplot(df,aes(y2[,1],y2[,2]))+geom_point()
ggplot(df,aes(y3[,1],y3[,2]))+geom_point()
ggplot(df,aes(y4[,1],y4[,2]))+geom_point()





```



```{r}
library(ggplot2)
library(ggpubr)
set.seed(2)  # to reproduce
M = 100  # repeated samplings, x fixed 
nord = 20  # order of polynoms
x = seq(from = -2, to = 4, by = 0.1)
truefunc = function(x) {
    return(x^2)
}
true_y = truefunc(x)
error = matrix(rnorm(length(x) * M, mean = 0, sd = 2), nrow = M, byrow = TRUE)
error
ymat = matrix(rep(true_y, M), byrow = T, nrow = M) + error
predalmrray = array(NA, dim = c(M, length(x), nord))
for (i in 1:M) {
    for (j in 1:nord) {
        predarray[i, , j] = predict(lm(ymat[i, ] ~ poly(x, j, raw = TRUE)))
    }
}
# M matrices of size length(x) times nord first, only look at
# variablity in the M fits and plot M curves where we had 1 for
# plotting need to stack the matrices underneath eachother and make
# new variable 'rep'
stackmat = NULL
for (i in 1:M) {
    stackmat = rbind(stackmat, cbind(x, rep(i, length(x)), predarray[i, 
        , ]))
}
# dim(stackmat)
colnames(stackmat) = c("x", "rep", paste("poly", 1:20, sep = ""))
sdf = as.data.frame(stackmat)  #NB have poly1-20 now - but first only use 1,2,20
# to add true curve using stat_function - easiest solution
true_x = x
yrange = range(apply(sdf, 2, range)[, 3:22])
p1 = ggplot(data = sdf, aes(x = x, y = poly1, group = rep, colour = rep)) + 
    scale_y_continuous(limits = yrange) + geom_line()
p1 = p1 + stat_function(fun = truefunc, lwd = 1.3, colour = "black") + 
    ggtitle("poly1")
p2 = ggplot(data = sdf, aes(x = x, y = poly2, group = rep, colour = rep)) + 
    scale_y_continuous(limits = yrange) + geom_line()
p2 = p2 + stat_function(fun = truefunc, lwd = 1.3, colour = "black") + 
    ggtitle("poly2")
p10 = ggplot(data = sdf, aes(x = x, y = poly10, group = rep, colour = rep)) + 
    scale_y_continuous(limits = yrange) + geom_line()
p10 = p10 + stat_function(fun = truefunc, lwd = 1.3, colour = "black") + 
    ggtitle("poly10")
p20 = ggplot(data = sdf, aes(x = x, y = poly20, group = rep, colour = rep)) + 
    scale_y_continuous(limits = yrange) + geom_line()
p20 = p20 + stat_function(fun = truefunc, lwd = 1.3, colour = "black") + 
    ggtitle("poly20")
ggarrange(p1, p2, p10, p20)

```

