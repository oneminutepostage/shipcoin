var handler = StripeCheckout.configure({
  key: 'pk_test_EGy5lvIR91G9LihccXJ6fewV',
  image: '/img/documentation/checkout/marketplace.png',
  locale: 'auto',
  bitcoin: true,
  token: function(token) {
    // Use the token to create the charge with a server-side script.
    // You can access the token ID with `token.id`
  }
});

$('#buy_button_stripe').on('click', function(e) {
  // Open Checkout with further options
  handler.open({
    name: 'One Minute Label',
    description: 'Instant shipping label purchase',
    amount: 2000
  });
  e.preventDefault();
});

// Close Checkout on page navigation
$(window).on('popstate', function() {
  handler.close();
});