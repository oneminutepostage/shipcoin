from django.conf import settings
import stripe

def charge(token, amount):
	amount = amount * 100
	stripe.api_key = settings.STRIPE_TOKEN
	try:
	  charge = stripe.Charge.create(
	      amount=amount,
	      currency="usd",
	      source=token,
	      description=settings.STRIPE_DESCRIPTION
	  )
	  log.info("Charged successfully on Stripe")
	  return True
	except stripe.error.CardError, e:
	  log.info("The card has been declined by Stripe")
	  return False