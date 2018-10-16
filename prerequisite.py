

from device42_app.dal import Base
from device42_app.dal.model.device import DeviceVM
from device42_app.common.mysql_connector import engine


print Base.metadata.create_all(engine)