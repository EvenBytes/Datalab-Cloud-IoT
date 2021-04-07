# sensor-sim

Contains </br>
    1. sendData.py . : a python file for running a simple script to publish to a pub/sub topic on GCP</br>
    2. sensorData.txt : a text file of temperature and ambient pressure from a Rainbow HAT sensorHub. </br>
    </br></br>
Copy these files to your computer. </br>
In GCP console, upload using Cloud shell. </br>

There is an auth_certificate that is recognized by Cloud IoT Core. 

## BigQuery table schema

```json
[
    {
        "name": "data",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {
                "name": "timestamp_ambient_pressure",
                "type": "STRING"
            },
            {
                "name": "ambient_pressure",
                "type": "FLOAT"
            },
            {
                "name": "timestamp_temperature",
                "type": "STRING"
            },
            {
                "name": "temperature",
                "type": "FLOAT"
            }
        ]
    }
]
```