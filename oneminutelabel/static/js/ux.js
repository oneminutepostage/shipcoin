packaging_group.on('change', function() {
	var packaging = packaging_group.filter(':checked').attr('value');
	if (packaging == 'own_packaging') {
		flat_rate_choices.hide();
		own_packaging_choices.fadeIn('fast');
	} else {
		own_packaging_choices.hide();
		flat_rate_choices.fadeIn('fast');
	}
});

$(".changes_rates_field").on('change', function(){
	rateButton.show();
	buyButton.hide();
	ratePrice.html(" ");
});

function displayRateResult(data){
	rateButton.hide();
	buyButton.show();
	ratePrice.html("$"+data);
}

function displayRateError(){
	rateButton.show();
	buyButton.hide();
	ratePrice.html(" ");
	alert("We couldn't find any rates - please try again or change your package information.");
}