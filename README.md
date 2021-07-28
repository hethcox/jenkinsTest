Video Source

This process consumes video frames from kafka and sends them to the RTMP server

The following parameters are available:

- KAFKA_CLUSTER - IP of kafka cluster
- KAFKA_PORT - IP of kafka port (default 9092)
- LOGLEVEL - FATAL, ERROR, WARN, INFO, DEBUG
- SERVER_IP - IP address to bind Flask to
- SERVER_PORT - port to bind Flask to
- RTMP_LIVE_STREAM_URL - URL for RTMP process e.g. rtmp://172.31.99.148:1935/live
- LIVE_STREAM_KEY - key for RTMP endpoint

The following endpoints are available:
- /activateVideoFeed - [POST] capture frames from kafka to the supplied file name. Parameters:
    * topic - kafka topic
    * group - kafka group

- /deactivateVideoFeed = [POST] stop capturing frames and close the file

- /videoList = [GET] retrieve list of files - this is not yet implemented

Examples:
# jenkinsTest
