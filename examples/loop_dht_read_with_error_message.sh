#!/bin/bash

DHTTYPE=22

while true
do
	RESULT=`python3 dht_read_with_error_message.py $DHTTYPE`
	TIME=`date '+%F %T'`
	if expr "$RESULT" : "^\\s\{2\}.*" > /dev/null; then
		echo ${TIME} DHT${DHTTYPE}, ${RESULT}
	else
		ARY=(`echo "${RESULT}"`)
		echo ${TIME} DHT${DHTTYPE}, humidity ${ARY[0]}%, temperature ${ARY[1]}*
	fi
	sleep 3
done
