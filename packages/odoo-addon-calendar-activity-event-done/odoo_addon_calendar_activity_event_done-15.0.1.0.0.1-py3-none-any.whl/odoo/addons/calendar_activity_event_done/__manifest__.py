# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Calendar Activity Event Done",
    "summary": "Calendar events linked with done activities will be shown as done",
    "version": "15.0.1.0.0",
    "category": "Productivity/Calendar",
    "website": "https://github.com/sygel-technology/sy-calendar",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "calendar",
    ],
    "data": [
        "views/calendar_event_views.xml",
    ],
}
