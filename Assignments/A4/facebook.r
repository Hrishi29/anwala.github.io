setwd(getwd())
#getting values from csvfile
csv <- read.table('friendscount.csv',header = TRUE,sep = ",")

#sorting the values in ascending orders
y <- sort(csv$FRIENDCOUNT)

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
plot(y, xlab="Friends", ylab="FriendsCount", col = "blue", type = "l")
title(main = "Facebook Friendship Paradox")

#setting up the text
text(10, 98, "x", col = 'red', cex=0.8)
text(55.5, result.mean, "x", col = 'red', cex = 0.8) # mean
text(41, result.median, "x", col = 'red', cex = 0.8) # median
text(57, result.sd, "x", col = 'red', cex = 0.8) # standard deviation
text(41, 300, "Median: 397", cex = 0.8)
text(62, 450, "Mean: 558.3176", cex = 0.8)
text(66, 620, "SD: 571.784", cex = 0.8)
text(24, 40, "Alexander's friends: 98", cex = 0.8)