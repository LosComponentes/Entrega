from flask import redirect,render_template,request,session
from flask import Response
import saludtech.seedwork.presentacion.api as api
from saludtech.modulos.manejador_datos.aplicacion.mapeadores import MapeadorImagenDTOJson
bp = api.crear_blueprint('manejador_datos', '/manejador_datos')

@bp.route('/imagen', methods=('POST',))
def agregar_imagen():
    try:
        imagen_dict = request.json
        map_imagen = MapeadorImagenDTOJson()
        imagen_dto = map_imagen.externo_a_dto(imagen_dict)

        sr = ServicioImagen()
        dto_final = sr.crear_imagen(imagen_dto)

        return map_imagen.dto_a_externo(dto_final)
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))),status=400,mimetype='application/json')

@bp.route('/imagen', methods=('GET',))
@bp.route('/imagen/<id>', methods=('GET',))
def dar_imagen(id=None):
    if id:
        sr = ServicioReserva()
        
        return sr.obtener_imagen_por_id(id)
    else:
        return [{'message': 'GET!'}]