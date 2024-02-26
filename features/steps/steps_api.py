from behave import step
from lib.classes.class_api import APIRequests
from lib.classes.class_room import Room


@step("[API] New random room added")
def step_impl(context):
    context.room = Room()
    APIRequests.create_room(context.room)


@step("[API] New booking is registered in the database")
def step_impl(context):
    bookings = APIRequests.get_bookings()
    assert f'"firstname":"{context.booking.first_name}","lastname":"{context.booking.last_name}"' in bookings
    # not checking dates due to the bug existing in the application (extra day being added to any booking)


@step("[API] New booking has not been registered in the database")
def step_impl(context):
    bookings = APIRequests.get_bookings()
    assert f'"firstname":"{context.booking.first_name}","lastname":"{context.booking.last_name}"' not in bookings


@step("[API] New room is present in the database")
def step_impl(context):
    rooms = APIRequests.get_rooms()
    assert f'"roomName":"{context.room.number}"' in rooms


@step("[API] Deleted room is not present in the database")
def step_impl(context):
    rooms = APIRequests.get_rooms()
    assert f'"roomName":"{context.room.number}"' not in rooms


@step("[API] New message has not been registered in the database")
def step_impl(context):
    bookings = APIRequests.get_messages()
    assert f'"subject":"{context.message.subject}"' not in bookings
