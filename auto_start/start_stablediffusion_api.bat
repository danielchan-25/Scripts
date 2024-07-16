@echo off
title Run Stable Diffusion API
cd /d E:\stable-diffusion-webui
start E:\conda_files\envs\stable-diffusion-webui\python.exe launch.py --port 7860 --api --no-half --disable-nan-check


rem --nowebui
rem start E:\conda_files\envs\stable-diffusion-webui\python.exe launch.py --port 7860 --nowebui --no-half --disable-nan-check --listen
