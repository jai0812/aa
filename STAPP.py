import streamlit as st
import boto3
import pandas as pd

# AWS S3 configuration
s3 = boto3.client('s3')
bucket_name = 'myfilesupload'
file_key = 'your-file-key'

# Function to read file from S3
def read_s3_file(bucket, key):
    obj = s3.get_object(Bucket=bucket, Key=key)
    return pd.read_csv(obj['Body'])

# Streamlit app
st.title("Display File from S3")
df = read_s3_file(bucket_name, file_key)
st.write(df)
