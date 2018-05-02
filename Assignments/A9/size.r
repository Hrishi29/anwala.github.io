setwd(getwd())
# csv dataframe for number of mementos
prevMementos <- read.table(header = TRUE,sep = ",",'previousMC.csv')
numMementos <- read.table(header = TRUE,sep = ",",'counting.csv')

#calculating the difference
app <- numMementos-prevMementos
barplot(app$Memento_Count, main="Changes in Timemaps Overtime",xlab = "Timemaps",ylab = "Difference")
