var service_group = $('input[name=service]');
var label_letter = $('#label_header_service_letter');
var label_service_header = $('#label_service_header');
var label_header_text_service = $('#label_header_text_service');
var label_header_text_rate = $('#label_header_text_rate');
var label_header_zip = $('#label_header_zip');
var from_zip = $("input[name=fromZip]");

service_group.on('change', function() {
	var service = service_group.filter(':checked').attr('value');
	if (service == 'first') {
		label_letter.text("F");
		label_header_text_service.text("FIRST CLASS PACKAGE");
		label_header_text_rate.text("First Class Package");
		label_service_header.text("FIRST CLASS PACKAGE");
	} else if (service == 'priority') {
		label_letter.text("P");
		label_header_text_service.text("PRIORITY MAIL");
		label_header_text_rate.text("Priority Mail");
		label_service_header.text("PRIORITY MAIL");
	} else {
		label_letter.text("E");
		label_header_text_service.text("PRIORITY MAIL EXPRESS");
		label_header_text_rate.text("Priority Mail Express");
		label_service_header.text("PRIORITY MAIL EXPRESS");
	}
});

from_zip.on('keyup', function(){
	label_header_zip.text($(this).val());
});