function getRate(){
	var all_fields_filled_out = validateFields();
	updateCookies();
	if (!(all_fields_filled_out)) {
		return null;
	}
	var data = labelForm.serialize();
	showLoadingGraphic();
    sendRateRequest("/rate/", data);
}

function showLoadingGraphic(){
	buyTable.hide();
    rateLoadingImage.show();
}
function hideLoadingGraphic(){
	buyTable.show();
    rateLoadingImage.hide();
}

function sendRateRequest(url, data){
	$.ajax({
        url : url,
        type: "POST",
        data : data,
        complete: function(data){
        	hideLoadingGraphic();
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
	showLoadingGraphic();
	$.ajax({
        url : url,
        type: "POST",
        data : data,
        complete: function(data){
        	hideLoadingGraphic();
        	if (data.status == 200 && data.responseText){
				displayLabelResult(data.responseText);
			} else {
				displayLabelError(data.responseText);
			}
        }
	});
}