setwd(getwd())
#reading data from csv 
csv <- read.table('followers.csv',header = TRUE,sep = ",")

#sort values in ascending order
y <- sort(csv$FollowersCount)

#calculating mean
result.mean <- mean(y)
print(result.mean)

#calculating median
result.median <- median(y)
print(result.median)

#calculating standard deviation
result.sd <- sd(y)
print(result.sd)

#plotting graph
plot(y, xlab="Followers", ylab="FollowersCount", col = "blue", type = "l")
title(main = "Twitter Followers Paradox")

#settting up text
text(65, 194, "x", col = 'red', cex=0.8)
text(175, result.mean, "x", col = 'red', cex = 0.8) # mean
text(82, result.median, "x", col = 'red', cex = 0.8) # median
text(188, result.sd, "x", col = 'red', cex = 0.8) # standard deviation
text(92, 6000, "Median: 274", cex = 0.8)
text(170, -50, "Mean: 2967.856", cex = 0.8)
text(165, 14353, "SD: 14353.86", cex = 0.8)
text(45, 6000, "AN's followers: 194", cex = 0.8)