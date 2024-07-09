from app.sensores.models.leituraSensorModel import LeituraSensorModel
from app.base.baseController import baseController
from app.sensores.models.sensorModel import SensorModel
from app.sensores.schemas.leituraSensorSchema import LeiturasSensor
from utils.exceptions.exceptions import NotFound


class leituraSensorController(baseController):
    def __init__(self, db, params=None):
        super().__init__(LeituraSensorModel, "Leitura Sensor", db, params)

    def list_leituras_by_sensor(self, id):
        sensor_db = self.db.get(SensorModel, id)

        if not sensor_db:
            raise NotFound("Sensor")
        sensor_dict = {}

        for sensor in sensor_db.leituras:
            if sensor.data_ocorrencia.date() not in sensor_dict:
                sensor_dict[sensor.data_ocorrencia.date()] = sensor
                sensor_dict[sensor.data_ocorrencia.date()] = {'qtd': 1, 'valor': sensor.valor}
            else:
                sensor_dict[sensor.data_ocorrencia.date()]['qtd'] += 1
                sensor_dict[sensor.data_ocorrencia.date()]['valor'] += sensor.valor

        for key, _ in sensor_dict.items():
            sensor_dict[key]['valor'] = sensor_dict[key]['valor'] / sensor_dict[key]['qtd']

        leituras_list = [LeiturasSensor(
            data_ocorrencia=key,
            valor=val['valor']
        ) for key, val in sensor_dict.items()]

        return {
            "id": sensor_db.id,
            "ip": sensor_db.ip,
            "logitude": sensor_db.logitude,
            "latitude": sensor_db.latitude,
            "active": sensor_db.active,
            "items": leituras_list
        }
