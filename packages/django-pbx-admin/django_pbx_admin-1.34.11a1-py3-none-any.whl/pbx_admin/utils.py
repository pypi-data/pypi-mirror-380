from __future__ import annotations

import logging
from functools import reduce
from numbers import Number
from typing import Any

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import ProgrammingError, connection
from django.db.models import QuerySet
from django.http import HttpRequest

log = logging.getLogger(__name__)


def get_pbx_admin_url(obj, site):
    model = obj._meta.model

    admin = site.get_admin(model)
    if admin is None and model._meta.proxy:
        admin = site.get_admin(model._meta.proxy_for_model)

    if admin is None:
        raise ValueError(f"Model admin for {model.__name__} not found")

    base_admin = admin
    kwargs = {admin.url_kwarg: getattr(obj, admin.slug_field or "id")}

    while admin.parent:
        p_obj = getattr(obj, admin.parent_field.name)
        p_field = admin.parent.slug_field or "id"
        kwargs[admin.parent.pk_url_kwarg] = getattr(p_obj, p_field)
        obj = p_obj
        admin = admin.parent

    endpoint = base_admin.edit_url(**kwargs)

    host = getattr(settings, "PRINTBOX_SITE_HOST", None)
    if not host:
        raise ImproperlyConfigured("settings.PRINTBOX_SITE_HOST not defined")
    schema = "https" if settings.PRINTBOX_SITE_HOST_SSL else "http"

    return f"{schema}://{host}{endpoint}"


def get_related_field(model, field, separator="__"):
    fields = field.split(separator)
    related_model = reduce(lambda m, f: m._meta.get_field(f).related_model, fields[:-1], model)
    return related_model._meta.get_field(fields[-1])


def count_estimate(qs: QuerySet, precision: int) -> int:
    """
    Estimate the number of objects in a queryset using the `django_pbx_admin_count_estimate`
    predefined PostgreSQL function.

    `precision` is the maximum number of objects for which the precise count will be returned.
     all above will be the estimated count.
    """
    cursor = connection.cursor()
    query, params = qs.query.sql_with_params()
    params = tuple(_escape_postgres_param(p) for p in params)
    sql = f"SELECT django_pbx_admin_count_estimate('{query}')" % params
    try:
        cursor.execute(sql)
    except ProgrammingError:
        log.exception("Failed to use django_pbx_admin_count_estimate")
    else:
        estimated_count = int(cursor.fetchone()[0])
        if estimated_count > precision:
            return estimated_count
    return qs.count()


def _escape_postgres_param(param: Any) -> str | Number:
    """
    Double quotes for non-numeric values to use them inside a postgres function.
    """
    if isinstance(param, Number):
        return param
    param = str(param).replace("'", "''")
    return f"$${param}$$"


def get_client_ip(request: HttpRequest) -> str:
    ip = (
        request.META.get("HTTP_X_ORIGINAL_FORWARDED_FOR")
        or request.META.get("HTTP_X_FORWARDED_FOR")
        or request.META.get("REMOTE_ADDR")
        or ""
    )
    return ip.split(",")[0].strip()
