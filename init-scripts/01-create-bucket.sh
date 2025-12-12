#!/bin/bash
awslocal s3 mb s3://db-bucket

awslocal s3 cp /tmp/code/classes.parquet s3://db-bucket/classes/classes.parquet