# ============================================
# Script de prueba para verificar conexión
# ============================================

import boto3
import json
from botocore.exceptions import ClientError

def test_dynamodb_connection():
    """Prueba la conexión y estructura de la tabla CorporateData"""
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('CorporateData')
        
        print("=" * 60)
        print("TEST DE CONEXIÓN A DYNAMODB")
        print("=" * 60)
        
        # Obtener información de la tabla
        table_info = table.table_status
        print(f"\n Conexión exitosa a tabla: CorporateData")
        print(f"   Estado: {table_info}")
        
        # Obtener esquema de claves
        key_schema = table.key_schema
        print(f"\n Esquema de claves:")
        for key in key_schema:
            print(f"   - {key['AttributeName']}: {key['KeyType']}")
        
        # Intentar insertar un registro de prueba
        test_data = {
            'id': 'TEST-01',
            'nombre': 'Prueba',
            'descripcion': 'Registro de prueba'
        }
        
        print(f"\n Intentando insertar registro de prueba...")
        print(f"   Datos: {json.dumps(test_data, indent=2)}")
        
        table.put_item(Item=test_data)
        print(f"   Inserción exitosa!")
        
        # Leer el registro
        print(f"\n Leyendo registro insertado...")
        response = table.get_item(Key={'id': 'TEST-001'})
        item = response.get('Item')
        print(f"   Datos leídos: {json.dumps(item, indent=2, default=str)}")
        
        # Eliminar el registro de prueba
        print(f"\n  Eliminando registro de prueba...")
        table.delete_item(Key={'id': 'TEST-001'})
        print(f"    Eliminación exitosa!")
        
        print("\n" + "=" * 60)
        print("TODAS LAS PRUEBAS PASARON CORRECTAMENTE")
        print("=" * 60)
        
    except ClientError as e:
        print(f"\n Error de DynamoDB: {e}")
        print(f"   Código: {e.response['Error']['Code']}")
        print(f"   Mensaje: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"\n Error inesperado: {e}")

if __name__ == "__main__":
    test_dynamodb_connection()
