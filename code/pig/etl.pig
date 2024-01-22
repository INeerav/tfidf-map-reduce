pig –useHCatalog
REGISTER /usr/lib/pig/piggybank.jar
DEFINE CSVLoader org.apache.pig.piggybank.storage.CSVLoader();
A = LOAD '/cleancsv' USING org.apache.pig.piggybank.storage.CSVExcelStorage(',','YES_MULTILINE','NOCHANGE','SKIP_INPUT_HEADER') AS ('id:chararray, docnumber:chararray, extractedsubject:chararray, extractedfrom:chararray, extractedbodytext:chararray');
B = FOREACH A GENERATE id,docnumber,extractedsubject,extractedfrom, REPLACE(REPLACE(REPLACE(REPLACE(REPLACE((REPLACE(extractedbodytext,'[\r\n]+','')),'<[^>]*>' , ' '),'[^a-zA-Z\\s\']+',' '),'(?=\\S*[\'])([a-zA-Z\'-]+)',''),'(?<![\\w\\-])\\w(?![\\w\\-])',''),'[ ]{2,}',' ') AS extractedbodytext;
C = FILTER B BY (docnumber is not null AND extractedbodytext is not null);
SPLIT C into spam_emails if (LOWER(extractedsubject) MATCHES '.*(please|if|urgent|alert|watch).*'), ham_emails if (LOWER(extractedsubject) MATCHES '.*(re|latest|fvv|imp|subscribe).*');
store spam_emails into '/user/hadoop/spamfiles' using PigStorage(',');
store ham_emails into '/user/hadoop/hamfiles' using PigStorage(',');
dump spam_emails;
STORE spam_emails INTO 'emails_db.spam_analysis' USING org.apache.hive.hcatalog.pig.HCatStorer();
dump ham_emails;
STORE ham_emails INTO 'emails_db.ham_analysis' USING org.apache.hive.hcatalog.pig.HCatStorer();