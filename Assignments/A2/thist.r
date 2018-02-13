setwd(getwd())
# csv dataframe of URI, number of mementos
numMementos <- read.table(header = TRUE,sep = ",",'counting.csv')
# histogram

hgram <- hist(numMementos$Memento_Count, col = "gray", breaks = 20, main="URIs vs. Number of Mementos",xlab = "Number of Mementos",ylab = "Number of URIs")
# add count labels
text(hgram$mids,hgram$counts, adj=c(0.5, -0.5), labels=hgram$counts)
