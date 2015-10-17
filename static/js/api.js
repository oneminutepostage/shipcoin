function getRate(){
	var all_fields_filled_out = validateFields();
	updateCookies();
	if (!(all_fields_filled_out)) {
		return null;
	}
	var data = labelForm.serialize();
	buyTable.hide();
    rateLoadingImage.show();
    sendRateRequest("/rate/", data);
}

function sendRateRequest(url, data){
	$.ajax({
        url : url,
        type: "POST",
        data : data,
        complete: function(data){
        	buyTable.show();
        	rateLoadingImage.hide();
        	if (data.responseText){
				displayRateResult(data.responseText);
			} else {
				displayRateError();
			}
        }
	});
}

function sendLabelRequest(token){
	url = "/label/";
	data = {
		token: token,
		rate_object_id: rateObjectId
	};
	$.ajax({
        url : url,
        type: "POST",
        data : data,
        complete: function(data){
        	console.log(data);
        	if (data.responseText){
				displayRateResult(data.responseText);
			} else {
				displayRateError();
			}
        }
	});
}