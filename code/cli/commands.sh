# for cli connection
chmod 400 /home/cloudshell-user/labsuser.pem
ssh -i /home/cloudshell-user/labsuser.pem hadoop@ec2-34-229-116-159.compute-1.amazonaws.com

# for hue connection
ssh -i C:\Users\patel\Downloads\labsuser.pem -N -D 8157 hadoop@ec2-52-90-148-197.compute-1.amazonaws.com

# for pig operations hadoop
hadoop fs -put piginput/emails.csv /piginputtest
hadoop fs -put outputspam/spam10.csv /outputspam/
hadoop fs -put outputham/ham10.csv /outputham/

# to try the java version of tfidf (didn`t use, simply ignore these)
aws s3 cp s3://emails-6a3d13b0/java/TFIDF.java TFIDF.java
mkdir sourcejava    
javac TFIDF.java -cp $(hadoop classpath)
jar cf tf.jar TFIDF*.class
javac -cp /usr/lib/hadoop/:/usr/lib/hadoop-mapreduce/ sourcejava/tfidf.java -d build –Xlint
javac -classpath ${HADOOP_HOME}/hadoop-${HADOOP_VERSION}-core.jar -d sourcejava tfidf.java