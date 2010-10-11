f <- function(ndice) {floor(runif(ndice) * 6 + 1)}

g <- function(rollcount,dice=4)
{
    accumulator <- 0
    for(i in 1:rollcount)
        accumulator = accumulator + sum(sort(f(dice))[(dice-3):dice])
    return(accumulator/rollcount)
}
