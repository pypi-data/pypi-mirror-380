import socket

from django.contrib.sites.models import Site
from django.http import HttpRequest
from django.conf import settings


def site_and_node(request: HttpRequest):
    """Provide current Site and Node based on request host.

    Returns a dict with keys ``badge_site`` and ``badge_node``.
    ``badge_site`` is a ``Site`` instance or ``None`` if no match.
    ``badge_node`` is a ``Node`` instance or ``None`` if no match.
    ``badge_site_color`` and ``badge_node_color`` provide the configured colors.
    """
    host = request.get_host().split(":")[0]
    site = Site.objects.filter(domain__iexact=host).first()

    node = None
    try:
        from nodes.models import Node

        node = Node.get_local()
        if not node:
            hostname = socket.gethostname()
            try:
                addresses = socket.gethostbyname_ex(hostname)[2]
            except socket.gaierror:
                addresses = []

            node = Node.objects.filter(hostname__iexact=hostname).first()
            if not node:
                for addr in addresses:
                    node = Node.objects.filter(address=addr).first()
                    if node:
                        break
            if not node:
                node = (
                    Node.objects.filter(hostname__iexact=host).first()
                    or Node.objects.filter(address=host).first()
                )
    except Exception:
        node = None

    site_color = "#28a745"
    if site:
        try:
            site_color = site.badge.badge_color
        except Exception:
            pass

    node_color = "#28a745"
    if node:
        node_color = node.badge_color

    site_name = site.name if site else ""
    node_role_name = node.role.name if node and node.role else ""
    return {
        "badge_site": site,
        "badge_node": node,
        # Public views fall back to the node role when the site name is blank.
        "badge_site_name": site_name or node_role_name,
        # Admin site badge uses the site display name if set, otherwise the domain.
        "badge_admin_site_name": site_name or (site.domain if site else ""),
        "badge_site_color": site_color,
        "badge_node_color": node_color,
        "current_site_domain": site.domain if site else host,
        "TIME_ZONE": settings.TIME_ZONE,
    }
