# TexasLaborStatisticsAPICall
A script that automates the download of Texas Labor Statistics Supply Reports. 
The example API request in ex.py downloads the reports for all Technical Schools/Universities in Texas. 
Downloads of other data will require looking at API requests through something like the XHR tab in a browser's (e.g., Firefox) DevTools.

## Setup
First, clone this repository (or optionally download the zip and extract the files), and then open the repository's root directory:
```shell
git clone https://github.com/aptitudepi/TexasLaborStatisticsAPICall.git
cd TexasLaborStatisticsAPICall/
```
Install prerequisites:
```shell
pip3 install requests
```
And execute the script! This should take ~15 minutes on a PC with a download speed of 4 MB/s
```shell
python3 ex.py
```
You should see the download JSON files in ```out/```
