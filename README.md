# tfidf-map-reduce

- Problem : Find the most common words in the emails
- Dataset : This email dataset is publicly available on data.world, file
size is 25 MB with 22 columns containing all the required
columns such as email subject, body, to, from, attachments
and timestamp with enough complexity to continue with this
assignment.
This famous/infamous dataset was released by the US state
department at the time of the US election roughly 7 years
ago 
- Clinton emails dataset
https://data.world/briangriffey/clinton-emails/workspace/file?filename=Emails.csv



## Tech stack

EMR cluster.
- Filesystem : hadoop
- Fileformat : parquet, avro
- AWS cloudformation Iaas
- Versions: Hue 4.11, EMR 6.14, Hadoop 3.3.3, pig 0.17, hive 3.1.3, Zeppelin 0.10.1; 
- Nodes: 1 primary and 1 core node
- Compute : Spark streaming, mapreduce
- Data engineering : AWS Ethena, Glue transformation, Pig-latin, Hive
- Visulization : Apache Hue board (Used Apache HUE to visualise the data with better UI, but in order to connect HUE to web browser, performed SSH tunnelling)
