from cassandra.cluster import Cluster
import os
from secret_utils import secrets


# Get secret values from AWS Secrets Manager
cassandra_username = secrets['cassandra_username']
cassandra_password = secrets['cassandra_password']


# Initialize Cassandra cluster and session
cluster = Cluster([os.environ['CASSANDRA_HOST']], auth_provider={'username': cassandra_username, 'password': cassandra_password})
session = cluster.connect(os.environ['CASSANDRA_KEYSPACE'])
