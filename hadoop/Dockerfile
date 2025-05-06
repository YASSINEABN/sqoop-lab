FROM openjdk:8-jdk-slim

LABEL maintainer="sqoop-hadoop-demo"

# Set environment variables
ENV JAVA_HOME=/usr/local/openjdk-8
ENV HADOOP_VERSION=3.3.4
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root

# Install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    curl \
    ssh \
    rsync \
    && rm -rf /var/lib/apt/lists/*

# Download and extract Hadoop
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz && \
    rm hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} ${HADOOP_HOME}

# Set up SSH for Hadoop
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

# Copy configuration files
COPY core-site.xml $HADOOP_CONF_DIR/
COPY hdfs-site.xml $HADOOP_CONF_DIR/
COPY mapred-site.xml $HADOOP_CONF_DIR/
COPY yarn-site.xml $HADOOP_CONF_DIR/
COPY hadoop-env.sh $HADOOP_CONF_DIR/
COPY start-hadoop.sh /

# Set the working directory
WORKDIR ${HADOOP_HOME}

# Format namenode and start Hadoop services
RUN chmod +x /start-hadoop.sh

# Expose HDFS ports
EXPOSE 9000 9870 8088

# Start Hadoop when container launches
CMD ["/start-hadoop.sh"]
