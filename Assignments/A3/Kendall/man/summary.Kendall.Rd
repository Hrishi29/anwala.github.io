\name{summary.Kendall}
\alias{summary.Kendall}
\title{summary Method for Class 'Kendall' }
\description{
In addition to
the value of Kendall's tau and its two-sided p-value are displayed,
the Kendall score, its variance and the value of the denominator
for Kendall tau are printed.
}

\usage{
\method{summary}{Kendall}(object, ...)
}

\arguments{
  \item{object}{output from Kendall, MannKendall or SeasonalMannKendall }
  \item{\dots}{any additional arguments}
}
\value{
 NULL
}

\author{ A.I. McLeod, aimcleod@uwo.ca }
\note{ If you want to use the output from Kendall or the other functions,
save the result as in res<-Kendall(x,y) and then select from res the
value(s) needed. }


\seealso{ \code{\link{summary.Kendall}}, \code{\link{Kendall}},
\code{\link{MannKendall}},\code{\link{SeasonalMannKendall}},
\code{\link{print.Kendall}} }
\examples{
x<-1:10
y<-rnorm(10)
out<-Kendall(x,y)
out
summary(out)
}
\keyword{ nonparametric }
