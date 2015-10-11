function validateFields(){
	fields = fromAddressGroupRequired.concat(toAddressGroupRequired, packageGroupRequired);
	result = validateAddressGroup(fields);
	return result.valid;
}

function validateAddressGroup(fields){
	var valid = true;
	var invalid_field_group = [];
	$.each(fields, function(index, value){
		value.removeClass("input-error");
		if ( !(value.val()) ){
			valid = false;
			value.addClass("input-error");
			invalid_field_group.push(value);
		}
	});
	return {
		valid: valid,
		invalid_fields: invalid_field_group
	};
}