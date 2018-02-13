setwd(getwd())
# Merged Dataset with memento count and days
mementoDays <- read.table(header = TRUE,sep = ",",'thirdq.csv')
# filtered set w/ atleast 1 memento
#withMementos <- subset(mementoDays, mementoDays$V2 > 0)
#emptyDate <- subset(mementoDays, is.na(mementoDays$V3))
plot(mementoDays$Age,mementoDays$Memento_Count,xlab="Age in Days",ylab="Number of Mementos",main="Scatter Plot for Days vs. Mementos")
