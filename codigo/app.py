import os
from flask import Flask, request, jsonify
from datetime import datetime
import pymysql
import pandas as pd
import numpy as np
 
app = Flask(__name__)
db = pymysql.connect(host='localhost',
                    user='root',
                    password='',
                    db='trescerritos')


#------------------------  CLIENTES --------------------------

@app.route('/crearCliente', methods=['POST'])
def crearCliente():

    Nombre=request.json['Nombre']
    Apellido=request.json['Apellido']
    Direccion=request.json['Direccion']
    Telefono=request.json['Telefono']
    Correo=request.json['Correo']
    Cuit=request.json['Cuit']
    Referente=request.json['Referente']
    Razon_social=request.json['Razon_social']
    Habilitacion_senasa=request.json['Habilitacion_senasa']
 
    try:
        cursor=db.cursor()
        sql = (" INSERT INTO clientes " + 
               " VALUES (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,'Si') ")
        tupla=(Nombre,Apellido,Direccion,Telefono,Correo,Cuit,Referente,Razon_social,Habilitacion_senasa)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error' , 'mensaje': 'Error al crear cliente: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"cliente creado correctamente"})


@app.route('/listarClientes', methods=['GET'])
def listarClientes():
    
    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM clientes FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM clientes WHERE Activo='Si' ")
        cursor.execute(sql)
        clientesBusqueda = cursor.fetchall()
        cursor.close()

        cantidadClientes=0
        clientes=[]
        for i in clientesBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            clientes.append(elemento)      
            cantidadClientes=cantidadClientes+1     
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error' , 'mensaje': 'Error al buscar clientes: '+str(e)})
    return jsonify({'result':'success', 'clientes':clientes, 'cantidadClientes':cantidadClientes})


@app.route('/buscarClientes', methods=['POST'])
def buscarClientes():

    Id = "%" + request.json['Id'] + "%"
    Nombre = "%" + request.json['Nombre'] + "%"
    Apellido = "%" + request.json['Apellido'] + "%"
    Direccion = "%" + request.json['Direccion'] + "%"
    Telefono = "%" + request.json['Telefono'] + "%"
    Correo = "%" + request.json['Correo'] + "%"
    Cuit = "%" + request.json['Cuit'] + "%"
    Referente = "%" + request.json['Referente'] + "%"
    Razon_social= "%" + request.json['Razon_social'] + "%"
    Habilitacion_senasa = "%" + request.json['Habilitacion_senasa'] + "%"

    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM clientes FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM clientes "+
               " WHERE Id like %s and Nombre like %s and Apellido like %s and "+
               " Direccion like %s and Telefono like %s and Correo like %s and " +
               " Cuit like %s and Referente like %s and Razon_social like %s and Habilitacion_senasa like %s and Activo='Si'  " ) 
        tupla=(Id,Nombre,Apellido,Direccion,Telefono,Correo,Cuit,Referente,Razon_social,Habilitacion_senasa)     
        cursor.execute(sql,tupla)
        clientesBusqueda = cursor.fetchall()
        cursor.close()

        cantidadClientes=0
        clientes=[]
        for i in clientesBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            clientes.append(elemento)      
            cantidadClientes=cantidadClientes+1  
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar clientes: '+str(e)})
    return jsonify({'result':'success', 'clientes':clientes, 'cantidadClientes':cantidadClientes})


@app.route('/buscarDatosCliente', methods=['POST'])
def buscarDatosCliente():
    
    Id=request.json['Id']
    try:

        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM clientes FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM clientes WHERE Id=%s ")       
        cursor.execute(sql, Id)
        clientesBusqueda = cursor.fetchall()
        cursor.close()
       
        cliente=[]
        for i in clientesBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            cliente.append(elemento)      
                     
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar clientes: '+str(e)})
    return jsonify({'result':'success', 'datosCliente':cliente})


@app.route('/modificarCliente', methods=['POST'])
def modificarCliente():

    Id=request.json['Id']
    Nombre=request.json['Nombre']
    Apellido=request.json['Apellido']
    Direccion=request.json['Direccion']
    Telefono=request.json['Telefono']
    Correo=request.json['Correo']
    Cuit=request.json['Cuit']
    Referente=request.json['Referente']
    Razon_social=request.json['Razon_social']
    Habilitacion_senasa=request.json['Habilitacion_senasa']
 
    try:
        cursor=db.cursor()
        sql = (" UPDATE clientes " + 
               " SET Nombre=%s,	Apellido=%s, Direccion=%s, Telefono=%s, Correo=%s, Cuit=%s, Referente=%s, Razon_social=%s,	Habilitacion_senasa=%s "+
               " WHERE Id=%s " )
        tupla=(Nombre,Apellido,Direccion,Telefono,Correo,Cuit,Referente,Razon_social,Habilitacion_senasa,Id)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al modificar cliente: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Cliente modificado correctamente"})


@app.route('/eliminarCliente', methods=['POST'])
def eliminarCliente():

    Id=request.json['Id']
    
    try:
        cursor=db.cursor()
        sql = (" UPDATE clientes SET Activo='No' " + 
               " WHERE Id=%s " )
        tupla=(Id)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al eliminar cliente: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Cliente elimininado correctamente"})
    

#------------------------  BROKERS --------------------------

@app.route('/crearBroker', methods=['POST'])
def crearBroker():

    Nombre=request.json['Nombre']
    Apellido=request.json['Apellido']
    Direccion=request.json['Direccion']
    Telefono=request.json['Telefono']
    Correo=request.json['Correo']
    Certificado_habilitacion=request.json['Certificado_habilitacion']
    Cuit=request.json['Cuit']   
 
    try:
        cursor=db.cursor()
        sql = (" INSERT INTO brokers " + 
               " VALUES (default,%s,%s,%s,%s,%s,%s,%s,'Si') ")
        tupla=(Nombre,Apellido,Direccion,Telefono,Correo,Certificado_habilitacion,Cuit)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al crear Broker: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Broker creado correctamente"})


@app.route('/listarBrokers', methods=['GET'])
def listarBrokers():
    
    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM brokers FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM brokers WHERE Activo='Si' ")
        cursor.execute(sql)
        brokersBusqueda = cursor.fetchall()
        cursor.close()

        cantidadBrokers=0
        brokers=[]
        for i in brokersBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            brokers.append(elemento)      
            cantidadBrokers=cantidadBrokers+1     
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar brokers: '+str(e)})
    return jsonify({'result':'success', 'brokers':brokers, 'cantidadBrokers':cantidadBrokers})


@app.route('/buscarBrokers', methods=['POST'])
def buscarBrokers():

    Id = "%" + request.json['Id'] + "%"
    Nombre = "%" + request.json['Nombre'] + "%"
    Apellido = "%" + request.json['Apellido'] + "%"
    Direccion = "%" + request.json['Direccion'] + "%"
    Telefono = "%" + request.json['Telefono'] + "%"
    Correo = "%" + request.json['Correo'] + "%"
    Certificado_habilitacion = "%" + request.json['Certificado_habilitacion'] + "%"
    Cuit = "%" + request.json['Cuit'] + "%"
    

    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM brokers FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM brokers "+
               " WHERE Id like %s and Nombre like %s and Apellido like %s and "+
               " Direccion like %s and Telefono like %s and Correo like %s and " +
               " Cuit like %s and Certificado_habilitacion like %s and Activo='Si' " ) 
        tupla=(Id,Nombre,Apellido,Direccion,Telefono,Correo,Cuit,Certificado_habilitacion)     
        cursor.execute(sql,tupla)
        brokersBusqueda = cursor.fetchall()
        cursor.close()

        cantidadBrokers=0
        brokers=[]
        for i in brokersBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            brokers.append(elemento)      
            cantidadBrokers=cantidadBrokers+1  
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar brokers: '+str(e)})
    return jsonify({'result':'success', 'brokers':brokers, 'cantidadBrokers':cantidadBrokers})


@app.route('/buscarDatosBroker', methods=['POST'])
def buscarDatosBroker():
    
    Id=request.json['Id']
    try:

        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM brokers FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM brokers WHERE Id=%s ")       
        cursor.execute(sql, Id)
        brokerBusqueda = cursor.fetchall()
        cursor.close()
       
        broker=[]
        for i in brokerBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            broker.append(elemento)      
                     
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar broker: '+str(e)})
    return jsonify({'result':'success', 'datosBroker':broker})


@app.route('/modificarBroker', methods=['POST'])
def modificarBroker():

    Id=request.json['Id']
    Nombre=request.json['Nombre']
    Apellido=request.json['Apellido']
    Direccion=request.json['Direccion']
    Telefono=request.json['Telefono']
    Correo=request.json['Correo']
    Certificado_habilitacion=request.json['Certificado_habilitacion']
    Cuit=request.json['Cuit']
 
    try:
        cursor=db.cursor()
        sql = (" UPDATE brokers " + 
               " SET Nombre=%s,	Apellido=%s, Direccion=%s,	Telefono=%s, Correo=%s,	Certificado_habilitacion=%s, Cuit=%s "+
               " WHERE Id=%s " )
        tupla=(Nombre, Apellido, Direccion, Telefono, Correo, Certificado_habilitacion, Cuit, Id)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al modificar broker: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Broker modificado correctamente"})
       

@app.route('/eliminarBroker', methods=['POST'])
def eliminarBroker():

    Id=request.json['Id']
    
    try:
        cursor=db.cursor()
        sql = (" UPDATE brokers SET Activo='No' " + 
               " WHERE Id=%s " )
        tupla=(Id)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al eliminar broker: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Broker elimininado correctamente"})
       
  
#------------------------  CAMION --------------------------

@app.route('/crearCamion', methods=['POST'])
def crearCamion():

    Chofer=request.json['Chofer']
    DNI=request.json['DNI']
    Telefono=request.json['Telefono']
    Direccion=request.json['Direccion']
    Marca=request.json['Marca']
    Patente_chasis=request.json['Patente_chasis']
    Patente_semi_acoplado=request.json['Patente_semi_acoplado']   
    Detalle_camion=request.json['Detalle_camion'] 
 
    try:
        cursor=db.cursor()
        sql = (" INSERT INTO camiones " + 
               " VALUES (default,%s,%s,%s,%s,%s,%s,%s,%s,'Si') ")
        tupla=(Chofer,DNI,Telefono,Direccion,Marca,Patente_chasis,Patente_semi_acoplado,Detalle_camion)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al crear Camion: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Camion creado correctamente"})


@app.route('/listarCamiones', methods=['GET'])
def listarCamiones():
    
    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM camiones FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM camiones WHERE Activo='Si' ")
        cursor.execute(sql)
        camionesBusqueda = cursor.fetchall()
        cursor.close()

        cantidadCamiones=0
        camiones=[]
        for i in camionesBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            camiones.append(elemento)      
            cantidadCamiones=cantidadCamiones+1     
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar camiones: '+str(e)})
    return jsonify({'result':'success', 'camiones':camiones, 'cantidadCamiones':cantidadCamiones})


@app.route('/buscarCamiones', methods=['POST'])
def buscarCamiones():

    Id = "%" + request.json['Id'] + "%"
    Chofer = "%" + request.json['Chofer'] + "%"
    DNI = "%" + request.json['DNI'] + "%"
    Telefono = "%" + request.json['Telefono'] + "%"
    Direccion = "%" + request.json['Direccion'] + "%"
    Marca = "%" + request.json['Marca'] + "%"
    Patente_chasis = "%" + request.json['Patente_chasis'] + "%"
    Patente_semi_acoplado = "%" + request.json['Patente_semi_acoplado'] + "%"
    Detalle_camion = "%" + request.json['Detalle_camion'] + "%"

    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM camiones FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM camiones "+
               " WHERE Id like %s and Chofer like %s and DNI like %s and "+
               " Direccion like %s and Telefono like %s and Marca like %s and " +
               " Patente_chasis like %s and Patente_semi_acoplado like %s and Detalle_camion like %s and Activo='Si'" ) 
        tupla=(Id,Chofer,DNI,Direccion,Telefono,Marca,Patente_chasis,Patente_semi_acoplado,Detalle_camion)     
        cursor.execute(sql,tupla)
        camionesBusqueda = cursor.fetchall()
        cursor.close()

        cantidadCamiones=0
        camiones=[]
        for i in camionesBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            camiones.append(elemento)      
            cantidadCamiones=cantidadCamiones+1  
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar camiones: '+str(e)})
    return jsonify({'result':'success', 'camiones':camiones, 'cantidadCamiones':cantidadCamiones})


@app.route('/buscarDatosCamion', methods=['POST'])
def buscarDatosCamion():
    
    Id=request.json['Id']
    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM camiones FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM camiones WHERE Id=%s ")       
        cursor.execute(sql, Id)
        camionBusqueda = cursor.fetchall()
        cursor.close()
       
        camion=[]
        for i in camionBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            camion.append(elemento)    
                             
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar camion: '+str(e)})
    return jsonify({'result':'success', 'datosCamion':camion})


@app.route('/modificarCamion', methods=['POST'])
def modificarCamion():

    Id=request.json['Id']
    Chofer=request.json['Chofer']
    DNI=request.json['DNI']
    Telefono=request.json['Telefono']
    Direccion=request.json['Direccion']
    Marca=request.json['Marca']
    Patente_chasis=request.json['Patente_chasis']
    Patente_semi_acoplado=request.json['Patente_semi_acoplado']   
    Detalle_camion=request.json['Detalle_camion'] 
 
    try:
        cursor=db.cursor()
        sql = (" UPDATE camiones " + 
               " SET Chofer=%s,	DNI=%s, Direccion=%s, Telefono=%s, Marca=%s, Patente_chasis=%s, Patente_semi_acoplado=%s, Detalle_camion=%s "+
               " WHERE Id=%s " )
        tupla=(Chofer, DNI, Direccion, Telefono, Marca, Patente_chasis, Patente_semi_acoplado, Detalle_camion, Id)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al modificar camion: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Camion modificado correctamente"})
       

@app.route('/eliminarCamion', methods=['POST'])
def eliminarCamion():

    Id=request.json['Id']    
    try:
        cursor=db.cursor()
        sql = (" UPDATE camiones SET Activo='No' " + 
               " WHERE Id=%s " )
        tupla=(Id)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error', 'mensaje': 'Error al eliminar camion: '+str(e)})    
    return jsonify({'result':'success', 'mensaje':"Camion elimininado correctamente"})
   

#---------------------  IMPORTACIONES ----------------------

#------------------------  COMPRA --------------------------

@app.route('/cargarCompraImportaciones', methods=['POST'])
def cargarCompraImportaciones():

    Nombre_empresa=request.json['Nombre_empresa']
    Nro_factura=request.json['Nro_factura']
    Telefono=request.json['Telefono']
    Localidad=request.json['Localidad']
    Pais=request.json['Pais']
    Cliente=request.json['Cliente']
    Nro_transaccion=request.json['Nro_transaccion']   
    Nro_remito=request.json['Nro_remito'] 
    Broker=request.json['Broker']   
    Precio_dolar_transaccion=request.json['Precio_dolar_transaccion']
 
    Producto=request.json['Producto']
    Precio_unitario_USD=request.json['Precio_unitario_USD']
    Precio_flete_USD=request.json['Precio_flete_USD']
    Precio_flete_unitario_USD=request.json['Precio_flete_unitario_USD']
    Gasto_despacho_USD=request.json['Gasto_despacho_USD']
    Gasto_despacho_unitario_USD=request.json['Gasto_despacho_unitario_USD']
    Fecha_emision_factura_=request.json['Fecha_emision_factura']   

    Fecha_ingreso_pais_=request.json['Fecha_ingreso_pais']
    Detalle_pago=request.json['Detalle_pago']
    Camion=request.json['Camion']
    Cantidad_bulto=request.json['Cantidad_bulto']
    Precio_unitario_ARS=request.json['Precio_unitario_ARS']
    Precio_flete_ARS=request.json['Precio_flete_ARS']
    Precio_flete_unitario_ARS=request.json['Precio_flete_unitario_ARS']
   
    Gasto_despacho_ARS=request.json['Gasto_despacho_ARS']
    Gasto_despacho_unitario_ARS=request.json['Gasto_despacho_unitario_ARS']
    Fecha_deposito_=request.json['Fecha_deposito']
    Observaciones=request.json['Observaciones']
    CRT=request.json['CRT']
    Nro_MIC=request.json['Nro_MIC']	
    Nro_CUVE=request.json['Nro_CUVE']

    Fecha_emision_factura = datetime.strptime(Fecha_emision_factura_, '%d/%m/%Y')
    Fecha_ingreso_pais = datetime.strptime(Fecha_ingreso_pais_, '%d/%m/%Y')
    Fecha_deposito = datetime.strptime(Fecha_deposito_, '%d/%m/%Y')

    try:
        cursor=db.cursor()
        sql = (" INSERT INTO importaciones_compra " + 
               " VALUES (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
        tupla=(Nombre_empresa,Nro_factura,Telefono,Localidad,Pais,Cliente,Nro_transaccion,Nro_remito,Broker,Precio_dolar_transaccion,Producto,Precio_unitario_USD,Precio_flete_USD,Precio_flete_unitario_USD,Gasto_despacho_USD,Gasto_despacho_unitario_USD,Fecha_emision_factura,Fecha_ingreso_pais,Detalle_pago,Camion,Cantidad_bulto,Precio_unitario_ARS,Precio_flete_ARS,Precio_flete_unitario_ARS,Gasto_despacho_ARS,Gasto_despacho_unitario_ARS,Fecha_deposito,Observaciones,CRT,Nro_MIC,Nro_CUVE)
        cursor.execute(sql,tupla)
        db.commit()
        cursor.close()       
        
    except Exception as e:        
        return jsonify({'result':'Error', 'mensaje': 'Error al cargar Compra Importacion: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Compra Importacion cargada correctamente"})


@app.route('/listarComprasImportaciones', methods=['GET'])
def listarComprasImportaciones():
   
    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM importaciones_compra FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM importaciones_compra ORDER BY Id DESC ")
        cursor.execute(sql)
        comprasImportacionesBusqueda = cursor.fetchall()
        cursor.close()

        cantidadComprasImportaciones=0
        ComprasImportaciones=[]
        for i in comprasImportacionesBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            ComprasImportaciones.append(elemento)      
            cantidadComprasImportaciones=cantidadComprasImportaciones+1         
           
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar Compras Importaciones: '+str(e)})

    return jsonify({'result':'success', 'ComprasImportaciones':ComprasImportaciones, 'cantidadComprasImportaciones':cantidadComprasImportaciones})


#------------------------  VENTA --------------------------

@app.route('/cargarVentaImportaciones', methods=['POST'])
def cargarVentaImportaciones():

    Cliente=request.json['Cliente']
    Nro_factura=request.json['Nro_factura']
    Telefono=request.json['Telefono']
    Precio_dolar_transaccion=request.json['Precio_dolar_transaccion']
    Producto=request.json['Producto']
    Precio_bulto=request.json['Precio_bulto']
    Precio_total=request.json['Precio_total']   
    
    Nro_transaccion=request.json['Nro_transaccion']
    Importe_compra=request.json['Importe_compra']
    Nro_remito=request.json['Nro_remito']
    Pais=request.json['Pais']
    Provincia=request.json['Provincia']
    Localidad=request.json['Localidad']
    Establecimiento=request.json['Establecimiento']  

    Camion=request.json['Camion']    
    Observaciones=request.json['Observaciones']    

    formas_de_pago = request.json['formas_de_pago']

    try:
        cursor=db.cursor()
        sql = (" INSERT INTO importaciones_venta " + 
               " VALUES (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
        tupla=(Cliente,Nro_factura,Telefono,Precio_dolar_transaccion,Producto,Precio_bulto,Precio_total,Nro_transaccion,Importe_compra,Nro_remito,Pais,Provincia,Localidad,Establecimiento,Observaciones,Camion)
        cursor.execute(sql,tupla)
        db.commit()

        sql1 = "SELECT MAX(Id) as Id FROM importaciones_venta"
        cursor.execute(sql1)
        IdImportacionVenta=cursor.fetchone()

        for f in formas_de_pago:
            Tipo = f['tipo']
            Monto = f['monto']
            Fecha_ = f['fecha']
            Fecha = datetime.strptime(Fecha_, '%d/%m/%Y')
           
            sql = (" INSERT INTO importaciones_forma_de_pago " + 
               " VALUES (default,%s,%s,%s,%s) ")
            tupla=(IdImportacionVenta[0], Tipo, Monto, Fecha)
            cursor.execute(sql,tupla)
            db.commit()        
        
        cursor.close() 
           
    except Exception as e:        
        return jsonify({'result':'Error', 'mensaje': 'Error al cargar Venta Importacion: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Venta Importacion cargada correctamente"})


@app.route('/listarVentasImportaciones', methods=['GET'])
def listarVentasImportaciones():
   
    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM importaciones_venta FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM importaciones_venta ORDER BY Id DESC ")
        cursor.execute(sql)
        ventasImportacionesBusqueda = cursor.fetchall()
        cursor.close()

        cantidadVentasImportaciones=0
        VentasImportaciones=[]
        for i in ventasImportacionesBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            VentasImportaciones.append(elemento)      
            cantidadVentasImportaciones=cantidadVentasImportaciones+1         
           
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar Ventas Importaciones: '+str(e)})

    return jsonify({'result':'success', 'VentasImportaciones':VentasImportaciones, 'cantidadVentasImportaciones':cantidadVentasImportaciones})


#---------------------  MERCADO INTERNO -------------------------

#------------------------  COMPRA --------------------------

@app.route('/cargarCompraMercadoInterno', methods=['POST'])
def cargarCompraMercadoInterno():

    Nombre_empresa=request.json['Nombre_empresa']
    Nro_factura=request.json['Nro_factura']
    Telefono=request.json['Telefono']
    Pais=request.json['Pais']
    Provincia=request.json['Provincia']
    Cliente=request.json['Cliente']
    Nro_transaccion=request.json['Nro_transaccion']
    Nro_remito=request.json['Nro_remito']
    
    Producto=request.json['Producto']
    Fecha_emision_factura_=request.json['Fecha_emision_factura']
    Fecha_emision_factura = datetime.strptime(Fecha_emision_factura_, '%d/%m/%Y')
    Detalle_pago=request.json['Detalle_pago']
    Camion=request.json['Camion']    
    Cantidad_bulto=request.json['Cantidad_bulto']

    Precio_unitario_ARS=request.json['Precio_unitario_ARS']
    Precio_flete_ARS=request.json['Precio_flete_ARS']
    Precio_flete_unitario_ARS=request.json['Precio_flete_unitario_ARS']
    Observaciones=request.json['Observaciones']    

    depositos = request.json['depositos']     
  
    try:
        cursor=db.cursor()
        sql = (" INSERT INTO mercado_interno_compra " + 
               " VALUES (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
        tupla=(Nombre_empresa,Nro_factura,Telefono,Pais,Provincia,Cliente,Nro_transaccion,Nro_remito,Producto,Fecha_emision_factura,Detalle_pago,Camion,Cantidad_bulto,Precio_unitario_ARS,Precio_flete_ARS,Precio_flete_unitario_ARS,Observaciones)
        cursor.execute(sql,tupla)
        db.commit()

        sql1 = "SELECT MAX(Id) as Id FROM mercado_interno_compra"
        cursor.execute(sql1)
        IdMercadoIntCompra=cursor.fetchone()

        for d in depositos:
            Monto = d['monto']
            Fecha_ = d['fecha']
            Fecha = datetime.strptime(Fecha_, '%d/%m/%Y')

            sql = (" INSERT INTO mercado_int_compra_depositos " + 
               " VALUES (default,%s,%s,%s) ")
            tupla=(IdMercadoIntCompra[0], Monto, Fecha)
            cursor.execute(sql,tupla)
            db.commit()        
        
        cursor.close() 
           
    except Exception as e:        
        return jsonify({'result':'Error', 'mensaje': 'Error al cargar Compra Mercado Interno: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Compra Mercado Interno cargada correctamente"})


@app.route('/listarComprasMercadoInterno', methods=['GET'])
def listarComprasMercadoInterno():
   
    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM mercado_interno_compra FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM mercado_interno_compra ORDER BY Id DESC ")
        cursor.execute(sql)
        comprasMercadoInternoBusqueda = cursor.fetchall()
        cursor.close()

        cantidadComprasMercadoInterno=0
        ComprasMercadoInterno=[]
        for i in comprasMercadoInternoBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            ComprasMercadoInterno.append(elemento)      
            cantidadComprasMercadoInterno=cantidadComprasMercadoInterno+1         
           
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar Compras Mercado Interno: '+str(e)})

    return jsonify({'result':'success', 'ComprasMercadoInterno':ComprasMercadoInterno, 'cantidadComprasMercadoInterno':cantidadComprasMercadoInterno})


#------------------------  VENTA --------------------------
	
@app.route('/cargarVentaMercadoInterno', methods=['POST'])
def cargarVentaMercadoInterno():

    Cliente=request.json['Cliente']
    Telefono=request.json['Telefono']
    Provincia=request.json['Provincia']
    Producto=request.json['Producto']
    Precio_por_bulto=request.json['Precio_por_bulto']
    Cantidad_por_bulto=request.json['Cantidad_por_bulto']
    
    Precio_por_KG=request.json['Precio_por_KG']
    Precio_total=request.json['Precio_total']
    Forma_de_pago=request.json['Forma_de_pago']
    Operacion=request.json['Operacion']
    Nro_transaccion=request.json['Nro_transaccion']
    Nro_factura=request.json['Nro_factura']

    Importe_compra=request.json['Importe_compra']
    Nro_remito=request.json['Nro_remito']
    Establecimiento=request.json['Establecimiento']  
    Observaciones=request.json['Observaciones']    
    Camion=request.json['Camion']      
  
    try:
        cursor=db.cursor()
        sql = (" INSERT INTO mercado_interno_venta " + 
               " VALUES (default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
        tupla=(Cliente,Telefono,Provincia,Producto,Precio_por_bulto,Cantidad_por_bulto,Precio_por_KG,Precio_total,Forma_de_pago,Operacion,Nro_transaccion,Nro_factura,Importe_compra,Nro_remito,Establecimiento,Observaciones,Camion)
        cursor.execute(sql,tupla)
        db.commit()         
        cursor.close() 
           
    except Exception as e:        
        return jsonify({'result':'Error', 'mensaje': 'Error al cargar Venta Mercado Interno: '+str(e)})
    
    return jsonify({'result':'success', 'mensaje':"Venta Mercado Interno cargada correctamente"})


@app.route('/listarVentasMercadoInterno', methods=['GET'])
def listarVentasMercadoInterno():
   
    try:
        cursor=db.cursor()
        sql0 = "SHOW COLUMNS FROM mercado_interno_venta FROM trescerritos;"
        cursor.execute(sql0)
        columnas = cursor.fetchall()        
        columnasItem = []
        for c in columnas:
            nombreColumna = c[0]
            columnasItem.append(nombreColumna)

        sql = (" SELECT * FROM mercado_interno_venta ORDER BY Id DESC ")
        cursor.execute(sql)
        ventasMercadoInternoBusqueda = cursor.fetchall()
        cursor.close()

        cantidadVentasMercadoInterno=0
        VentasMercadoInterno=[]
        for i in ventasMercadoInternoBusqueda:
            elemento = {}
            for index in range(len(columnasItem)):
                elemento[columnasItem[index]] = i[index]
            VentasMercadoInterno.append(elemento)      
            cantidadVentasMercadoInterno=cantidadVentasMercadoInterno+1         
           
    except Exception as e:        
        return jsonify({'result':'Error' , 'mensaje': 'Error al buscar Ventas Mercado Interno: '+str(e)})

    return jsonify({'result':'success', 'VentasMercadoInterno':VentasMercadoInterno, 'cantidadVentasMercadoInterno':cantidadVentasMercadoInterno})


if __name__ == "__main__":
    app.run(debug=True,
            port=4000)