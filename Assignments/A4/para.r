setwd(getwd())
csv <- read.table('friendscount.csv',header = TRUE,sep = ",")
x <- c(csv$FRIENDCOUNT)
result.mean <- mean(x)
print(result.mean)
result.median <- median(x)
print(result.median)
result.sd <- sd(x)
print(result.sd)
y <- sort(csv$FRIENDCOUNT)
plot(y, xlab="Friends", ylab="FriendsCount", xlim=c(0, 90), col = "blue", type = "l")

text(10, 98, "x", col = 'red', cex=0.8)
text(55.5, result.mean, "x", col = 'red', cex = 0.8) # mean
text(41, result.median, "x", col = 'red', cex = 0.8) # median
text(57, result.sd, "x", col = 'red', cex = 0.8) # standard deviation
text(41, 300, "Median: 397", cex = 0.8)
text(62, 450, "Mean: 558.3176", cex = 0.8)
text(66, 620, "SD: 571.784", cex = 0.8)
text(24, 40, "Alexander's friends: 98", cex = 0.8)