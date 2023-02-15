from django.shortcuts import get_object_or_404
from .models import Drone,Medication,Loads, EnventLog
from .serializers import DronesSerializer, MedicationSerializer, LoadSerializer, BSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import schedule

# view for registering a new drone
@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        drones = Drone.objects.all()
        serializer = DronesSerializer(drones, many = True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = DronesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data
            serializer.save()
            return Response("Drones saved") 
        else:
            return Response(serializer.errors, status=404)

# view for loading a drone
@api_view(['GET', 'POST'])
def load_drone(request,did,mid):
    drone = get_object_or_404(Drone, id=did)
    medication = get_object_or_404(Medication, id = mid)

    if medication.weight <= drone.weight_limit:
        if drone.battery_capacity > 25:
            load = Loads(drone=drone, medication = medication)
            load.save()
            drone.state ="LOADING"
            drone.save()
            return Response("Load created")
        else:
            return Response("drone battery percentage is below 25%")
    else:
        return Response("the medication wheighs more than the drone's weight limit")



# view to check available drones
@api_view()
def check_available(request):
    drones = Drone.objects.filter(state = "IDLE")
    serializer = DronesSerializer(drones, many=True)
    return Response(serializer.data)


# view to check medication loaded to the drone
@api_view()
def check_med(request,id):
    drone = Drone.objects.get(id =id)
    load = Loads.objects.get(drone=drone)
    medication = Medication.objects.get(id = load.medication.id)
    serializer = MedicationSerializer(medication)
    return Response(serializer.data)


#view to check battery percentage of the drone
@api_view()
def check_battery(request,id):
    drone = Drone.objects.get(id =id)
    serializer = BSerializer(drone)
    return Response(serializer.data)



# function to periodically log battery percentages
def log_percentage() :
    drones = Drone.objects.all()
    for drone in drones:
        log = EnventLog(drone = drone, battery = drone.battery_capacity)
        log.save()

#calling the log_percentage function every 5 minutes
schedule.every(5).minutes.do(log_percentage)