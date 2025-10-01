"""Spec for Common Links spec used across the packages."""

from .route_link import RouteLink
from .widget_field import WidgetField

GenericLink = WidgetField | RouteLink
