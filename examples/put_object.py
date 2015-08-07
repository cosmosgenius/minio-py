# -*- coding: utf-8 -*-
# Minio Python Library for Amazon S3 Compatible Cloud Storage, (C) 2015 Minio, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from minio import Minio

__author__ = 'minio'

# find out your s3 end point here:
# http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region

client = Minio('https://<your-s3-endpoint>',
               access_key='YOUR-ACCESSKEYID',
               secret_key='YOUR-SECRETACCESSKEY')

# Put a new object
client.put_object('my-bucket', 'my_key', 11, 'hello world',
                  content_type='text/plain')

# Put a file
file_stat = os.stat('file.dat')
with open('file.dat', 'rb') as file_data:
    client.put_object('my-bucket', 'my_key', file_stat.st_size, file_data)
