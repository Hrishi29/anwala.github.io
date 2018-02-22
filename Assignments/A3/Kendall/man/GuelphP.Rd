\name{GuelphP}
\alias{GuelphP}
\docType{data}
\title{Phosphorous Concentrations in Speed River, Monthly }
\description{
Monthly time series of phosphorous (P) concentrations in mg/l, Speed River, Guelph, Ontario,
1972.1-1977.1."  
}
\usage{data(GuelphP)}
\format{
  The format is:
 Time-Series [1:72] from 1972 to 1978: 0.47 0.51 0.35 0.19 0.33 NA 0.365 0.65 0.825 1 ...
 - attr(*, "title")= chr "Phosphorous Data,Speed River,Guelph,1972.1-1977.1"
}
\details{
See Hipel and McLeod (2005, pp.707-709 and p.986).  
Hipel and McLeod used intervention analysis to estimate the effect of a phosphorous
removal scheme. Intervention analysis was also used to estimate the missing values.
}
\source{
Hipel, K.W. and McLeod, A.I., (2005).
Time Series Modelling of Water Resources and Environmental Systems.
Electronic reprint of our book orginally published in 1994.
\url{http://www.stats.uwo.ca/faculty/aim/1994Book/}.

}

\examples{
data(GuelphP)
plot(GuelphP)
#replace missing values in the series with estimates obtained from Hipel and McLeod
# (2005, p. 986)
missingEst<-c(0.1524, 0.2144, 0.3064, 0.1342)
GuelphP2<-GuelphP
GuelphP2[is.na(GuelphP)]<-missingEst
}
\keyword{datasets}
