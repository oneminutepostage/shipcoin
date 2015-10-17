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
	hideRateFields();
});

function displayRateResult(data){
	var data = JSON.parse(data);
	var amount = data.amount;
	var object_id = data.object_id;
	rateObjectId = object_id;
	rateAmount = amount;
	rateButton.hide();
	buyButton.show();
	ratePrice.html("$"+amount);
}

function hideRateFields(){
	rateButton.show();
	buyButton.hide();
	ratePrice.html(" ");
}

function displayRateError(){
	hideRateFields();
	alert("We couldn't find any rates - please try again or change your package information.");
}

function displayLabelResult(data){
	var data = JSON.parse(data);
	labelUrlButton.attr("href", data.label_url);
	labelTrackingNumber.text(data.tracking_number);
	var usps_link = "https://tools.usps.com/go/TrackConfirmAction.action?tLabels=" + data.tracking_number;
	UspsTrackingUrl.attr("href", usps_link);
	labelModal.modal('show');
	hideRateFields();
}

function displayLabelError(data){
	var data = JSON.parse(data);
	if (data){
		alert(data);
	} else {
		alert("Unknown error");
	}
}