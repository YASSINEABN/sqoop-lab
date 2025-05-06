# Sqoop-Hadoop Demo

A demonstration project showcasing data integration between MySQL, Hadoop, and Sqoop with a web-based visualization dashboard.

## Overview

This project demonstrates a complete data pipeline:
1. Data is stored in a MySQL database
2. Sqoop transfers the data from MySQL to Hadoop HDFS
3. A web application visualizes the data with interactive charts and tables

## Components

- **MySQL**: Stores sample employee data
- **Hadoop**: Distributed file system for data storage
- **Sqoop**: Data transfer tool to import data from MySQL to Hadoop
- **Flask Web App**: Data visualization dashboard

## Prerequisites

- Docker and Docker Compose
- 4GB+ of available RAM
- 10GB+ of free disk space

## Quick Start

1. Clone this repository:
   ```
   git clone [repository-url]
   cd sqoop-hadoop-demo
   ```

2. Build and start the containers:
   ```
   docker-compose build
   docker-compose up -d
   ```

3. Access the web dashboard:
   ```
   http://localhost:8080
   ```

## Project Structure

```
sqoop-hadoop-demo/
├── docker-compose.yml     # Docker Compose configuration
├── hadoop/                # Hadoop configuration
│   ├── Dockerfile         # Hadoop Docker image
│   ├── core-site.xml      # Hadoop core configuration
│   ├── hdfs-site.xml      # HDFS configuration
│   ├── mapred-site.xml    # MapReduce configuration
│   ├── yarn-site.xml      # YARN configuration
│   ├── hadoop-env.sh      # Hadoop environment variables
│   └── start-hadoop.sh    # Hadoop startup script
├── mysql/                 # MySQL configuration
│   ├── Dockerfile         # MySQL Docker image
│   └── init/              # MySQL initialization scripts
│       ├── 01-create-tables.sql  # Create database tables
│       └── 02-insert-data.sql    # Insert sample data
├── sqoop/                 # Sqoop configuration
│   ├── Dockerfile         # Sqoop Docker image
│   ├── hadoop-conf/       # Hadoop config for Sqoop
│   ├── sqoop-env.sh       # Sqoop environment variables
│   └── import-data.sh     # Data import script
└── webapp/                # Flask web application
    ├── Dockerfile         # Webapp Docker image
    ├── app.py             # Flask application
    ├── requirements.txt   # Python dependencies
    └── templates/         # HTML templates
        └── index.html     # Dashboard template
```

## How It Works

1. **MySQL Container**: Initializes with sample employee data
2. **Hadoop Container**: Starts HDFS and YARN services
3. **Sqoop Container**: Imports data from MySQL to Hadoop HDFS
4. **Webapp Container**: Visualizes the data from Hadoop

## Running the Demo

1. Start all services:
   ```
   docker-compose up -d
   ```

2. Watch the logs to monitor the process:
   ```
   docker-compose logs -f
   ```

3. Access the web dashboard at http://localhost:8080

4. Stop all services when done:
   ```
   docker-compose down
   ```

## Data Visualization

The web dashboard provides:
- Gender distribution pie chart
- Employee hire years bar chart
- Complete employee data table

## Troubleshooting

### Common Issues:

1. **Hadoop services not starting**
   - Check Hadoop logs: `docker-compose logs hadoop`
   - Ensure JAVA_HOME is set correctly in hadoop-env.sh

2. **Sqoop import failing**
   - Check Sqoop logs: `docker-compose logs sqoop`
   - Verify MySQL is accessible from the Sqoop container
   - Ensure tables exist in MySQL database

3. **Web app not displaying data**
   - Check if sample_data.csv was created
   - Restart the webapp container: `docker-compose restart webapp`
   - Check webapp logs: `docker-compose logs webapp`

4. **Permission issues with volumes**
   - Ensure volume permissions are set correctly
   - Try recreating volumes: `docker-compose down -v` then `docker-compose up -d`

### Fixing Hadoop Download Issues:

If you encounter Hadoop download problems, modify the Dockerfile to use the archive.apache.org URLs:
```
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
```

## Advanced Usage

### Customizing the Data Source

To use your own MySQL data:
1. Modify the SQL scripts in `mysql/init/`
2. Update the Sqoop import script in `sqoop/import-data.sh`
3. Adjust the column names in `webapp/app.py`

### Scaling Hadoop

For a more realistic Hadoop cluster:
1. Add additional worker nodes in `docker-compose.yml`
2. Configure HDFS DataNodes and YARN NodeManagers
3. Update the Hadoop configuration files

## License

This project is licensed under the MIT License - see the LICENSE file for details.
