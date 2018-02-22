\name{Kendall-package}
\alias{Kendall-package}
\docType{package}
\title{
Kendall correlation and trend tests.
}
\description{
Compute Kendall's rank correlation and various trend tests.
}

\details{

\tabular{ll}{
Package: \tab Kendall\cr
Type: \tab Package\cr
Version: \tab 2.2\cr
Date: \tab 2011-05-16\cr
License: \tab GPL (>= 2)\cr
LazyLoad: \tab yes\cr
}

If you just want to compute Kendall's tau or its signficance level,
the base function \code{cor} and \code{cor.test} are recommended.
The purpose of this package is to implement the Mann-Kendall test,
the seasonal Mann-Kendall trend test as well as computing the 
Kendall score.	 See documentation for Mann-Kendall on using
the block bootstrap to deal with autocorrelation.
}

\author{
A. I. McLeod

Maintainer: aimcleod@uwo.ca
}

\references{ 
Hipel, K.W. and McLeod, A.I., (1994).
Time Series Modelling of Water Resources and Environmental Systems.
}

\keyword{ts}

\keyword{package}

\seealso{
\code{\link{cor}}, 
\code{\link{cor.test}}, 
\code{\link{print.Kendall}}, 
\code{\link{summary.Kendall}},
\code{\link{MannKendall}},
\code{\link{SeasonalMannKendall}}
}

\examples{
library(boot)
data(PrecipGL)
MKtau<-function(z) MannKendall(z)$tau
tsboot(PrecipGL, MKtau, R=500, l=5, sim="fixed")
}
