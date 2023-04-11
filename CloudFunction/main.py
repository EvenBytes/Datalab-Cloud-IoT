from flask import escape
from google.cloud import bigquery
from datetime import datetime

#gcloud functions deploy <nombre_de_la_funcion> --runtime python37 --trigger-http --entry-point <nombre_de_la_funcion> --source <directorio_de_la_funcion> --requirements <archivo_requirements.txt>


# Función que se ejecutará en la Cloud Function
def write_to_bigquery(request):
    # Recupera los parámetros desde la solicitud HTTP
    dataset = escape(request.args.get('dataset', default='sensorHubData'))
    table = escape(request.args.get('table', default='Temperatures'))
    temperature = escape(request.args.get('data', default=0.00))
    
    # Obtiene la fecha y hora actual
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    
    # Inicializa el cliente de BigQuery
    client = bigquery.Client()
    
    # Configura la referencia a la tabla destino
    table_ref = client.dataset(dataset).table(table)
    
    # Crea el objeto de registro que se escribirá en la tabla
    data = {"temperature": temperature, "timestamp_temperature": timestamp}
    
    # Inserta el registro en la tabla
    errors = client.insert_rows_json(table_ref, [data])
    
    # Si hay algún error al insertar los datos, devuelve un mensaje de error
    if errors:
        return f'Error al insertar los datos en BigQuery: {errors}', 500
    else:
        return 'Datos insertados correctamente en BigQuery.', 200
