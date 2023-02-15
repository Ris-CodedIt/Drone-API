//Description
This is a drone API that allows the following functions:
>> rigister a drone
>> check drone battery percentage
>> load a drone with some medication:
        1) does not allow a drone to load medication that weighs more than the drone's weight limit.
        2) does not allow the drone to load if it's battery percentage is below 25%.
>> check the medication loaded to a drone.
>> check for available drones (those in the idle state).
>> logs battery percentages periodically(after every 5 minutes)


// build and run

pip install -r requirements .text
> python manage.py runserver

//testing

urls
register drone '' *homepage            **to add  a new drone sroll to the bottom of the page
check available 'available/'
load medication 'load/<drone_id>/<medication_id>/'
check medication 'check_med/<drone_id>'
check battery percentage  'check_battery/<id>/'


Test scenarios

1) loading drone(id=12) results in an error because it has a battery percentage below 25%
2) loading medication(id = 2) to drone(id=7) results in an error because the medication weighs more than the drone's weight limit


//Admin Access

username: admin
password: 1234






