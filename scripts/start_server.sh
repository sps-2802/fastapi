#!/bin/bash
cd /home/ec2-user/my-fastapi-app
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &