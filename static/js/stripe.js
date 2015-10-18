var handler = StripeCheckout.configure({
  key: stripe_publishable_token,
  image: '/static/img/shipcoin.png',
  locale: 'auto',
  bitcoin: true,
  token: function(token) {
    sendLabelRequest(token.id);
  }
});

$('#buy_button_stripe').on('click', function(e) {
  // Open Checkout with further options
  handler.open({
    name: 'One Minute Label',
    description: 'Instant shipping label purchase',
    amount: (rateAmount*100)
  });
  e.preventDefault();
});

// Close Checkout on page navigation
$(window).on('popstate', function() {
  handler.close();
});