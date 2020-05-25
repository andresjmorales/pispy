# PiSpy
PiSpy


How to use

Install sFlow on sFlow agent/sender

Run sFlow on agent Pi using sflow_sender.sh script




Run sflow_collecter.sh script on the sFlow collecter devicem (PiSpy) which will decode sFlow datagrams using sflowtool -> pysflow -> datagram as JSON. JSON is read and averaged.

prfiles.py is run on PiSpy in order to generate profiles and continously monitor new incoming datagrams.

Based on those datagrams, gNMI commands are sent off to the sFlow agent/router to whitelist/graylist/config.
