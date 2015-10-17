def get_objects_from_request(request):
    address_from = {
        "name": request.POST.get("fromName"),
        "street1": request.POST.get("fromStreet1"),
        "street2": request.POST.get("fromStreet2"),
        "city": request.POST.get("fromCity"),
        "state": request.POST.get("fromState"),
        "zip": request.POST.get("fromZip"),
        "country": "US",
        "email": "oneminutelabel@gmail.com",
        "object_purpose": "PURCHASE"
    }
    address_to = {
        "name": request.POST.get("toName"),
        "street1": request.POST.get("toStreet1"),
        "street2": request.POST.get("toStreet2"),
        "city": request.POST.get("toCity"),
        "state": request.POST.get("toState"),
        "zip": request.POST.get("toZip"),
        "country": "US",
        "email": "oneminutelabel@gmail.com",
        "object_purpose": "PURCHASE"
    }
    if request.POST.get("packaging") == "flat_rate":
        package_template = request.POST.get("flatRateOptions")
    else:
        package_template = None
    package = {
        "length": request.POST.get("packageLength", "1"),
        "width": request.POST.get("packageWidth", "1"),
        "height": request.POST.get("packageHeight", "1"),
        "distance_unit": "in",
        "weight": request.POST.get("packageWeight"),
        "mass_unit": request.POST.get("packageWeightUnit"),
        "template": package_template
    }
    service = request.POST.get("service")
    return address_from, address_to, package, service
    