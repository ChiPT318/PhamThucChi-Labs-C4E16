from models.service import Service
import mlab

mlab.connect()

# all_services = Service.objects()
#
# print(all_services[10].name)

id_to_find = "5ac4f4a836011e0a9cd3b3a9"

# kieu_anh = Service.objects(id=id_to_find)[0]
# kieu_anh = Service.objects.get(id = id_to_find)
service = Service.objects.with_id(id_to_find)

if service is None:
    print("Service not found")

else:
    # kieu_anh.delete()
    # print("Deleted")

    service.update(set__address="Tran Duy Hung")
    service.reload()
    print(service.address)
