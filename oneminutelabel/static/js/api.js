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
        	if (data.responseText && data.responseText != "None"){
				displayRateResult(data.responseText);
			} else {
				displayRateError();
			}
        }
	});
}