#loading library Kendall
library(Kendall)
setwd(getwd())
#reading contents from csv file
csv <- read.table('ptdf.csv',header = TRUE,sep = ",")
#producing summary of results
summary(Kendall(csv$PageRank,csv$TFIDF))
