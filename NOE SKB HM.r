### combine all digital sales report from NOE

# setwd ("C:/Users/Ben/Google Drive/Console games/royalty report/royalty report from nintendo")
# setwd("C:/Users/Harry Samsung Laptop/Downloads/ben.liu's work/Console games/royalty report/royalty report from nintendo")


# search all csv in subfolders
homedir="C:/Users/Ben/Google Drive/Console games/royalty report/royalty report from nintendo"
# homedir="C:/Users/Harry Samsung Laptop/Downloads/ben.liu's work/Console games/royalty report/royalty report from nintendo"
filelocation=list.files(pattern=".CSV",path=homedir, recursive = T,full.names = T)

# check dim of all files
stat=do.call(rbind,lapply(filelocation,function(x) dim(read.csv(x,sep=";"))))
stat
print(paste0("total rows: ",sum(stat[,1]),"; total columns: ",max(stat[,2])))

# combine csv
library(plyr)
dat=do.call(rbind.fill,lapply(filelocation,function(x) read.csv(x,sep=";",strip.white=T)))
dat$Purchase.Date=as.Date(dat$Purchase.Date,format="%m/%d/%Y")

# summarise sales & revenue by country
by_country=dat[!is.na(dat$Country),c("Title","Country","Sales","Revenue.Amount.Curr.Euro")]

# convert abbreviated to full country names
library(countrycode)
by_country$Country=countrycode(by_country$Country,"iso2c","country.name")

library(reshape)
df=melt(by_country,id.vars=c("Title","Country"))
df=cast(df,Title+Country~variable,sum)


# visualise result by SKB performance
library(ggplot2)
df$Country=factor(df$Country,levels=arrange(df[df$Title %in% "SENRAN KAGURA Burst",],Sales)$Country)
df=df[!is.na(df$Country),]
# by units sold
ggplot(df,aes(x=Country,y=Sales,fill=Title))+geom_bar(position="dodge",stat="identity")+coord_flip()+labs(y="Total units sold",title="NOE digital sales (by Dec 2014)")
# by revenue (Euro)
library(scales)
ggplot(df,aes(x=Country,y=Revenue.Amount.Curr.Euro,fill=Title))+geom_bar(position="dodge",stat="identity")+coord_flip()+labs(y="Total revenue in Euro",title="NOE digital sales (by Dec 2014)")+scale_y_continuous(labels = comma)
