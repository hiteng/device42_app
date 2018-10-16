




from sqlalchemy import Column, Integer, String
from device42_app.dal import Base




class DeviceVM(Base):

    __tablename__ = "device_vm"

    serial_no = Column(Integer, primary_key=True, autoincrement=True)
    device_type = Column(String(100))
    ip_address = Column(String(50), nullable=False)
    hostname = Column(String(100))
    service_level = Column(String(100))
    customer = Column(String(100))
    notes = Column(String(250))







