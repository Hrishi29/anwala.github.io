##loading library Kendall
library(Kendall)
setwd(getwd())
#reading contents from csv
csv <- read.table('alexa.csv',header = TRUE,sep = ",")
#summary for PR-TFIDF
summary(Kendall(csv$PageRank,csv$TFIDF))
#summary for TFIDF-Alexa
summary(Kendall(csv$TFIDF,csv$Alexa))
#summary for PR-Alexa
summary(Kendall(csv$PageRank,csv$Alexa))
