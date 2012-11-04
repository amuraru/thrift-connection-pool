export PATH=/opt/thrift-0-9/bin:$PATH
mvn clean package dependency:copy-dependencies
java -cp target/dependency/*:target/thrift-sample-1.0-SNAPSHOT.jar JavaServer
