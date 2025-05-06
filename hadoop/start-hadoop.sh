#!/bin/bash

# Source Hadoop environment variables
. $HADOOP_CONF_DIR/hadoop-env.sh

# Set JAVA_HOME if not already set
export JAVA_HOME=${JAVA_HOME:-/usr/local/openjdk-8}

# Check and echo JAVA_HOME for debugging
echo "JAVA_HOME is set to: $JAVA_HOME"

# Set Hadoop user environment variables
export HDFS_NAMENODE_USER=root
export HDFS_DATANODE_USER=root
export HDFS_SECONDARYNAMENODE_USER=root
export YARN_RESOURCEMANAGER_USER=root
export YARN_NODEMANAGER_USER=root

# Create Hadoop data directories if they don't exist
mkdir -p /hadoop-data/namenode
mkdir -p /hadoop-data/datanode

# Format the namenode if it doesn't exist
if [ ! -d "/hadoop-data/namenode/current" ]; then
  $HADOOP_HOME/bin/hdfs namenode -format
fi

# Start SSH service
service ssh start

# Start HDFS
$HADOOP_HOME/sbin/start-dfs.sh

# Start YARN
$HADOOP_HOME/sbin/start-yarn.sh

# Create user directory in HDFS
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /user/root

# Keep container running
tail -f /dev/null
