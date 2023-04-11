# DataLab Cloud IoT

## Contiene

1. sendData.py . : un script python para ejecutar para publicar en pub/sub en GCP
2. sensorData.txt : un archivo de texto con la temperatura y la presión ambiental de un sensor HATHub de Rainbow

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

Desplegar Cloud Function

```
gcloud functions deploy write_to_bigquery 
  --runtime python37 \
  --trigger-http \
  --entry-point write_to_bigquery \
  --requirements requirements.txt \
  --allow-unauthenticated
```