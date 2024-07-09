from sqlalchemy.exc import IntegrityError

from utils.exceptions.exceptions import (BadRequest,
                                         NotFound,
                                         UnprocessableEntity,
                                         ServerError)


class baseController():
    def __init__(self, main_model, module_name, db, query_params=None) -> None:
        self.main_model = main_model
        self.module_name = module_name
        self.db = db
        self.query_params = query_params.dict() if query_params else {}

    def _get_columns(self):
        pass

    def list(self, id=None):
        response = {}
        if id:
            return self.find_by_id(id)
        else:
            response['items'] = self.db.query(self.main_model).all()

        return response

    def add(self, request):
        try:
            request_dict = request.__dict__
            new_data = self.main_model(**request_dict)

            self.db.add(new_data)
            self.db.flush()
            self.db.refresh(new_data)
            self.db.commit()

            return new_data

        except IntegrityError as err:
            raise BadRequest(err)

        except Exception as err:
            raise ServerError(err)

    def put(self, request, id):
        data_db = self.find_by_id(id)

        try:
            for key, value in request.dict().items():
                setattr(data_db, key, value)
        except IntegrityError as err:
            raise BadRequest(err)
        except Exception as err:
            raise ServerError(err)

        self.db.commit()
        return data_db

    def delete(self, id):
        data_db = self.find_by_id(id)
        self.db.delete(data_db)
        self.db.commit()
        return {"mensagem": f"{self.module_name} delete id {id}"}

    def find_by_id(self, id):
        data_db = self.db.get(self.main_model, id)

        if not data_db:
            raise NotFound(f"{self.module_name} id {id}")

        return data_db
