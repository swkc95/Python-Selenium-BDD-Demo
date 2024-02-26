from behave import step
from lib.pages import AdminRoomsPage
from lib.classes.class_room import Room


@step("Admin enters the rooms page")
def step_impl(context):
    page = AdminRoomsPage(context)
    page.rooms_tab.click()


@step("Admin provides a valid room info with type of {room_type}")
def step_impl(context, room_type):
    context.room = Room()
    context.room.type = room_type
    page = AdminRoomsPage(context)
    page.fill_room_form(context.room)


@step("Admin adds a room feature - {feature}")
def step_impl(context, feature):
    context.room.features = [feature]
    page = AdminRoomsPage(context)
    page.add_room_features(context.room)


@step("Admin sends a new room form")
def step_impl(context):
    page = AdminRoomsPage(context)
    page.create_button.click()


@step("Admin finds newly added room and deletes it")
def step_impl(context):
    page = AdminRoomsPage(context)
    page.delete_room(context.room)


@step("Admin sees the new room on the rooms list")
def step_impl(context):
    page = AdminRoomsPage(context)
    page.set_format_variable(context.room.number)
    new_room = page.room_entry_by_room_number.text
    assert context.room.type in new_room
    assert str(context.room.is_accessible).lower() in new_room
    assert context.room.price in new_room
    assert all(element in new_room for element in context.room.features)


@step("Admin does not see the new room on the rooms list")
def step_impl(context):
    page = AdminRoomsPage(context)
    assert context.room.number not in page.rooms_table.text



