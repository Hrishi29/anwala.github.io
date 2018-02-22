\name{print.Kendall}
\alias{print.Kendall}
\title{print Method for Class 'Kendall' }
\description{
The value of Kendall's tau and its two-sided p-value are displayed.
}

\usage{
\method{print}{Kendall}(x, ...)
}

\arguments{
  \item{x}{output from Kendall, MannKendall or SeasonalMannKendall }
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
\code{\link{summary.Kendall}} }
\examples{
x<-1:10
y<-rnorm(10)
Kendall(x,y)
#is equivalent to
out<-Kendall(x,y)
print(out)
}
\keyword{ nonparametric }
