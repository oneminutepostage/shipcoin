def access_settings(request):
    from django.conf import settings
    return {
    	'STRIPE_PUBLISHABLE_TOKEN': settings.STRIPE_PUBLISHABLE_TOKEN
    }