setwd("/Users/mantioco/Documents/Data Science/DS lab")

data <- read.csv("analisi-di-mercato-sum-grouped.csv")

data_time <- read.csv("analisi-di-mercato-time1.csv")



summary(data_time)

head(data)
str(data)
summary(data)


hist(data$time1, main=" ", ylab="Frequency", xlab="Time 1 sum", xlim = c(0,200), breaks = seq(min(data$time1), max(data$time1), by = 10))
q <- quantile(data$time1, c(0.25, 0.75))
abline( v = c(mean(data$time1),q[1], q[2]),
        col = c("red", "green", "green"))


hist(data$time2,main=" ", ylab="Frequency", xlab="Time 2 sum", xlim = c(0,200), breaks = seq(min(data$time2), max(data$time2), by = 10))
q <- quantile(data$time2, c(0.25, 0.75))
abline( v = c(mean(data$time2),q[1], q[2]),
        col = c("red", "green", "green"))

hist(data$length,main=" ", ylab="Frequency", xlab="Length sum", xlim = c(0,200), breaks = seq(min(data$length), max(data$length), by = 10))
q <- quantile(data$length, c(0.25, 0.75))
abline( v = c(mean(data$length),q[1], q[2]),
        col = c("red", "green", "green"))

hist(data$categories1, main=" ", ylab="Frequency", xlab="Categories1 sum")
q <- quantile(data$categories1, c(0.25, 0.75))
abline( v = c(mean(data$categories1),q[1], q[2]),
        col = c("red", "green", "green"))

hist(data$categories2, main=" ", ylab="Frequency", xlab="Categories2 sum")
q <- quantile(data$categories2, c(0.25, 0.75))
abline( v = c(mean(data$categories2),q[1], q[2]),
        col = c("red", "green", "green"))


hist(data$categories3, main=" ", ylab="Frequency", xlab="Categories3 sum")
q <- quantile(data$categories3, c(0.25, 0.75))
abline( v = c(mean(data$categories3),q[1], q[2]),
        col = c("red", "green", "green"))



hist(data$sentiments1)
hist(sum$feelings1)


par(mfrow=c(1, 2))
hist(data_time$time1_workday_morning, col = "blue",  main=" Time 1  morning ", ylab="Frequency", xlab=" Workday ", 
     xlim = c(0,200), breaks = seq(min(data_time$time1_workday_morning), max(data_time$time1_workday_morning), by = 10))
hist(data_time$time1_weekend_morning, col = "green",  main=" ", ylab="Frequency", xlab=" Weekend ", 
     xlim = c(0,200), breaks = seq(min(data_time$time1_weekend_morning), max(data_time$time1_weekend_morning), by = 10))


par(mfrow=c(1, 2))
hist(data_time$time1_workday_afternoon, col = "blue",  main=" Time 1 afternoon", ylab="Frequency", xlab=" Workday", 
     xlim = c(0,200), breaks = seq(min(data_time$time1_workday_afternoon), max(data_time$time1_workday_afternoon), by = 10))
hist(data_time$time1_weekend_afternoon, col = "green",  main=" ", ylab="Frequency", xlab=" Weekend ", 
     xlim = c(0,200),breaks = seq(min(data_time$time1_weekend_afternoon), max(data_time$time1_weekend_afternoon), by = 10))


par(mfrow=c(1, 2))
hist(data_time$time1_workday_evening, col = "blue",  main="Time 1 evening ", ylab="Frequency", xlab=" Workday ", 
     xlim = c(0,200), breaks = seq(min(data_time$time1_workday_evening), max(data_time$time1_workday_evening), by = 10))
hist(data_time$time1_weekend_evening, col = "green",  main=" ", ylab="Frequency", xlab=" Weekend ", 
     xlim = c(0,200), breaks = seq(min(data_time$time1_weekend_evening), max(data_time$time1_weekend_evening), by = 10))

par(mfrow=c(1, 2))
hist(data_time$time1_workday_night, col = "blue",  main=" Time 1 night", ylab="Frequency", xlab=" Workday ", 
     xlim = c(0,200), breaks = seq(min(data_time$time1_workday_night), max(data_time$time1_workday_night), by = 10))
hist(data_time$time1_weekend_night, col = "green",  main=" ", ylab="Frequency", xlab=" Weekend", 
     xlim = c(0,200), breaks = seq(min(data_time$time1_weekend_night), max(data_time$time1_weekend_night), by = 10) )

