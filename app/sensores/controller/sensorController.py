from app.sensores.models.sensorModel import SensorModel
from app.base.baseController import baseController
from app.sensores.schemas.sensorSchema import SensorResponseLastDistance


class sensorController(baseController):
    def __init__(self, db, params=None):
        super().__init__(SensorModel, "Sensor", db, params)

    def add_sensor(self, request):
        request_dict = request.__dict__

        sensor_db = self.db.query(self.main_model).filter(
            self.main_model.ip == request_dict['ip']).first()

        if sensor_db:
            for key, value in request.dict().items():
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
            color_index = 0
            color_options = {0: "blue",
                             1: "green",
                             2: "yellow",
                             3: "red"}
            if last_distance:
                for layer, value in sensor.distance_layer.items():
                    if last_distance <= value:
                        color_index = color_index + 1

            list_response.append(SensorResponseLastDistance(
                id=sensor.id,
                ip=sensor.ip,
                logitude=sensor.logitude,
                latitude=sensor.latitude,
                active=sensor.active,
                distance_layer=sensor.distance_layer,
                color_icon=color_options[color_index],
                last_distance=last_distance))
        return {"items": list_response}
