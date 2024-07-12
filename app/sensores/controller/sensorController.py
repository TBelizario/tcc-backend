import datetime
from app.sensores.models.sensorModel import SensorModel
from app.base.baseController import baseController
from app.sensores.schemas.sensorSchema import SensorResponseLastDistance
import requests


class sensorController(baseController):
    def __init__(self, db, params=None):
        super().__init__(SensorModel, "Sensor", db, params)

    def add_sensor(self, request):
        request_dict = request.__dict__
        
        lat, lon = self.buscar_lat_lon(request_dict['address'], request_dict['city'])

        sensor_db = self.db.query(self.main_model).filter(
            self.main_model.ip == request_dict['ip']).filter(
                self.main_model.nome == request_dict['nome']).first()
        request_dict['latitude'] = lat
        request_dict['logitude'] = lon
        if sensor_db:
            for key, value in request_dict.items():
                setattr(sensor_db, key, value)
            self.db.commit()
            return sensor_db

        return self.add(request)

    def patch(self, request, id):
        try:
            sensor = self.db.get(self.main_model, id)
            sensor.distance_layer = {'baixo': request.baixo,
                                     'medio': request.medio,
                                     'alta': request.alta}
            self.db.commit()
        except Exception as err:
            return {"error": err}
        return sensor

    def list_maps(self):
        sensores = self.db.query(self.main_model).all()
        list_response = []
        for sensor in sensores:
            last_distance = sensor.leituras[-1].valor if sensor.leituras else 0
            
            data_ocorrencia = datetime.datetime.now()
            
            if last_distance:
                data_ocorrencia = sensor.leituras[-1].data_ocorrencia
                
            color_index = 0
            color_options = {0: "blue",
                             1: "green",
                             2: "yellow",
                             3: "red"}
            if last_distance and sensor.distance_layer:
                for layer, value in sensor.distance_layer.items():
                    if last_distance <= value:
                        color_index = color_index + 1

            list_response.append(SensorResponseLastDistance(
                data_insert=sensor.date_insert,
                id=sensor.id,
                ip=sensor.ip,
                nome=sensor.nome,
                address=sensor.address,
                city=sensor.city,
                logitude=sensor.logitude,
                latitude=sensor.latitude,
                active=sensor.active,
                distance_layer=sensor.distance_layer,
                color_icon=color_options[color_index],
                last_distance=last_distance,
                data_ocorrencia=data_ocorrencia))
        return {"items": list_response}

    def buscar_lat_lon(self, address, city):
        try:
            headers = {
                'User-Agent': 'TCC_APP/1.0 Faculdade Uninter Thiago Belizario'
            }
            url = f"http://nominatim.openstreetmap.org/search?q={address}, {city}&format=json"
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                response = response.json()[0]
                return float(response['lat']), float(response['lon'])
            return None, None
        except Exception as err:
            print(err)
            return 0, 0
