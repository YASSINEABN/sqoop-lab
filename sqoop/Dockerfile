FROM openjdk:8-jdk-slim

LABEL maintainer="sqoop-hadoop-demo"

# Set environment variables
ENV SQOOP_VERSION=1.4.7
ENV HADOOP_VERSION=3.3.4
ENV SQOOP_HOME=/opt/sqoop
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$SQOOP_HOME/bin

# Install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    curl \
    ssh \
    rsync \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Download and install Hadoop (needed for Sqoop)
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz && \
    rm hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} ${HADOOP_HOME}

# Download and install Sqoop
RUN wget https://archive.apache.org/dist/sqoop/${SQOOP_VERSION}/sqoop-${SQOOP_VERSION}.bin__hadoop-2.6.0.tar.gz && \
    tar -xzf sqoop-${SQOOP_VERSION}.bin__hadoop-2.6.0.tar.gz && \
    rm sqoop-${SQOOP_VERSION}.bin__hadoop-2.6.0.tar.gz && \
    mv sqoop-${SQOOP_VERSION}.bin__hadoop-2.6.0 ${SQOOP_HOME}

# Download and install MySQL connector
RUN wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.28/mysql-connector-java-8.0.28.jar && \
    mv mysql-connector-java-8.0.28.jar ${SQOOP_HOME}/lib/

# Download and install commons-lang for Sqoop
RUN wget https://repo1.maven.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.jar && \
    mv commons-lang-2.6.jar ${SQOOP_HOME}/lib/

# Copy Hadoop configuration files
COPY hadoop-conf/* ${HADOOP_HOME}/etc/hadoop/

# Copy Sqoop environment file
COPY sqoop-env.sh ${SQOOP_HOME}/conf/

# Copy the import script
COPY import-data.sh /

# Make scripts executable
RUN chmod +x /import-data.sh

# Set the working directory
WORKDIR /

# Command to run when container starts
CMD ["/import-data.sh"]
