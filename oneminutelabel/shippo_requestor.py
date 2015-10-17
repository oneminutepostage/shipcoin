from django.conf import settings
import logging
import shippo

log = logging.getLogger(__name__)

def get_rates(address_from, address_to, package):
    log.info("Calling Shippo")
    shippo.api_key = settings.SHIPPO_TOKEN
    shipment = shippo.Shipment.create(
        object_purpose = 'PURCHASE',
        address_from = address_from,
        address_to = address_to,
        parcel = package 
    )
    log.info("Received Shippo Shipment object_id %s" % shipment.object_id)
    try:
        return shippo.Shipment.get_rates(shipment.object_id, sync=True)
    except Exception as ex:
        log.warning("Shippo connection failed: %s" % ex)
        return None

def get_rate(address_from, address_to, package, service):
    shippo_service = map_service(service)
    if not shippo_service:
        log.error("Couldn't find Shippo service %s" % service)
        return None
    rates = get_rates(address_from, address_to, package)
    if not rates:
        log.warning("Didn't get Shippo rate response")
        return None
    rate_objects = rates.results
    if rate_objects and len(rate_objects) > 0:
        for rate in rate_objects:
            if rate.servicelevel_name == shippo_service:
                log.info("Got rate for service %s with amount %s" % (service, rate.amount))
                return rate
    return None

def map_service(service):
    mapping = {
        "first": "First-Class Package/Mail Parcel",
        "priority": "Priority Mail",
        "express": "Priority Mail Express"
    }
    return mapping[service] if service in mapping else None

def get_label(object_id):
    try:
        return shippo.Transaction.create(rate=object_id, sync=True)
    except Exception as ex:
        log.warning("Shippo connection failed: %s" % ex)
        return None
