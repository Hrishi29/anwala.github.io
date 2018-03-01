setwd(getwd())
#reading data from csv 
csv <- read.table('following.csv',header = TRUE,sep = ",")

#sort values in ascending order
y <- sort(csv$FollowingCount)

#calculating mean
result.mean <- mean(y)
print(result.mean)

#calculating median
result.median <- median(y)
print(result.median)

#calculating standard deviation
result.sd <- sd(y)
print(result.sd)

#plotting the graph
plot(y, xlab="Following", ylab="FollowingCount", col = "blue",xlim=c(0, 80), type = "l")
title(main = "Twitter Following Paradox")

#setting up the text
text(10, 76, "x", col = 'red', cex=0.8)
text(56, result.mean, "x", col = 'red', cex = 0.8) # mean
text(38, result.median, "x", col = 'red', cex = 0.8) # median
text(61.7, result.sd, "x", col = 'red', cex = 0.8) # standard deviation
text(38, 900, "Median: 480.5", cex = 0.8)
text(56, 600, "Mean: 1032.158", cex = 0.8)
text(70, 1449, "SD: 1549.282", cex = 0.8)
text(10, 400, "AN Following: 76", cex = 0.8)