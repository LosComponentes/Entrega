import saludtech.seedwork.presentacion.api as api
import json
from saludtech.modulos.manejador_datos.aplicacion.servicios import ServicioImagen
from saludtech.modulos.manejador_datos.aplicacion.dto import ImagenDTO
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio


from flask import redirect,render_template,request,session
from flask import Response
from saludtech.modulos.manejador_datos.aplicacion.mapeadores import MapeadorImagenDTOJson

bp = api.crear_blueprint('manejador_datos', '/manejador_datos')

@bp.route('/imagen', methods=('POST',))
def agregar_imagen():
    try:
        imagen_dict = request.json
        map_imagen = MapeadorImagenDTOJson()
        imagen_dto = map_imagen.externo_a_dto(imagen_dict)
        print('externo_a_dto')
        sr = ServicioImagen()
        print('ServicioImagen')
        dto_final = sr.crear_imagen(imagen_dto)
        print('crear_imagen')
        return map_imagen.dto_a_externo(dto_final)
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))),status=400,mimetype='application/json')

@bp.route('/imagen', methods=('GET',))
@bp.route('/imagen/<id>', methods=('GET',))
def dar_imagen(id=None):
    if id:
        sr = ServicioImagen()
        return [{'message': 'GET!'}]
        # return sr.obtener_imagen_por_id(id)
    else:
        return [{'message': 'GET ALL!'}]