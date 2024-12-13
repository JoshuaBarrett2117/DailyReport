#!/usr/bin/env bash
# cron:1 1 1 1 1
# new Env("依赖环境")

echo "开始安装依赖"
pip install -r requirements.txt
echo "依赖安装完成"
