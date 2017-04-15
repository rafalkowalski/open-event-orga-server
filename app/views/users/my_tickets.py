from flask import Blueprint
from flask import render_template

from app.helpers.data_getter import DataGetter
from app.helpers.ticketing import TicketingManager

my_tickets = Blueprint('my_tickets', __name__, url_prefix='/mytickets')


@my_tickets.route('/')
def display_my_tickets():
    page_content = {
        "tab_upcoming_events": "Upcoming Events",
        "tab_past_events": "Past Events",
        "title": "My Tickets"
    }

    upcoming_events_orders = TicketingManager.get_orders_of_user(upcoming_events=True)
    past_events_orders = TicketingManager.get_orders_of_user(upcoming_events=False)
    placeholder_images = DataGetter.get_event_default_images()
    custom_placeholder = DataGetter.get_custom_placeholders()
    im_config = DataGetter.get_image_configs()
    im_size = ''
    for config in im_config:
        if config.page == 'mysession':
            im_size = config.size

    return render_template('gentelella/users/mytickets/mytickets_list.html',
                           page_content=page_content,
                           upcoming_events_orders=upcoming_events_orders,
                           past_events_orders=past_events_orders,
                           placeholder_images=placeholder_images,
                           custom_placeholder=custom_placeholder,
                           im_size=im_size)
