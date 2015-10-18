from django.shortcuts import render
from django.conf import settings
from django.views.decorators.http import require_POST, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json

import models
import helpers
import shippo_requestor
import stripe_requestor

log = logging.getLogger(__name__)

def home(request):
    context = {
        'STRIPE_PUBLISHABLE_TOKEN': settings.STRIPE_PUBLISHABLE_TOKEN
    }
    return render(request, 'base.html', context)

@csrf_exempt
@require_POST
def rate(request):
    log.info("Received rate request")
    address_from, address_to, package, service = helpers.get_objects_from_request(request)
    log.info("Sending rate request to Shippo")
    rate = shippo_requestor.get_rate(address_from, address_to, package, service)
    log.info("Selected rate from Shippo: %s" % rate)
    response = ""
    if rate is not None:
        models.Rate.objects.create(
            amount = rate.amount,
            shippo_object_id = rate.object_id
            )
        response = {
            "object_id": rate.object_id,
            "amount": rate.amount
        }
        response = json.dumps(response)
    return HttpResponse(response, status="200")

@csrf_exempt
@require_POST
def label(request):
    token = request.POST.get("token")
    rate_object_id = request.POST.get("rate_object_id")
    log.info("Received label request for rate id %s" % rate_object_id)
    rate = models.Rate.objects.get(shippo_object_id=rate_object_id)
    shippo_label = shippo_requestor.get_label(rate.shippo_object_id)
    if shippo_label is not None and shippo_label.object_status == "SUCCESS":
        label = models.Label.objects.create(
            rate = rate,
            amount = rate.amount,
            shippo_object_id = shippo_label.object_id,
            tracking_number = shippo_label.tracking_number,
            label_url = shippo_label.label_url
            )
        charged = stripe_requestor.charge(token, rate.amount)
        if charged:
            response = {
                "label_url": shippo_label.label_url,
                "tracking_number": shippo_label.tracking_number
            }
            log.info("Label %s successfully purchased" % label.shippo_object_id)
            return HttpResponse(json.dumps(response), status="200")
        else:
            log.warning("Failed to charge on Stripe")
            shippo_requestor.refund_label(shippo_label.object_id)
            log.warning("Refunded label on Shippo")
            response = { "error": "We couldn't charge you for this label. Please verify your payment information and try again." }
            return HttpResponse(json.dumps(response), status="400")
    else:
        log.warning("Label creation failed: %s" % shippo_label)
        if hasattr(shippo_label, "messages") and len(shippo_label.messages >= 1):
            response = { "error": shippo_label.messages }
        else:
            response = { "error": "There was an error connecting to our label provider. Please try again or contact Shipcoin support." }
        return HttpResponse(json.dumps(response), status="400")

