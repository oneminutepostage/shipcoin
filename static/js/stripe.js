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
  // Uncomment the following lines, and remove the sendLabelReuest
  // function to activate the client-side Stripe code
  //handler.open({
  //  name: 'Shipcoin',
  //  description: 'USPS shipping label',
  //  amount: parseInt(rateAmount*100)
  //});
  sendLabelRequest("faketoken");
  e.preventDefault();
});

// Close Checkout on page navigation
$(window).on('popstate', function() {
  handler.close();
});