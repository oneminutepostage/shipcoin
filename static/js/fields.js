var labelForm = $("#labelForm");
// FROM ADDRESS
var fromName = $("input[name=fromName]");
var fromStreet1 = $("input[name=fromStreet1]");
var fromStreet2 = $("input[name=fromStreet2]");
var fromCity = $("input[name=fromCity]");
var fromState = $("select[name=fromState]");
var fromZip = $("input[name=fromZip]");
var fromAddressGroupRequired = [fromName, fromStreet1, fromCity, fromState, fromZip];
var fromAddressGroup = [fromName, fromStreet1, fromStreet2, fromCity, fromState, fromZip];
// TO ADDRESS
var toName = $("input[name=toName]");
var toStreet1 = $("input[name=toStreet1]");
var toStreet2 = $("input[name=toStreet2]");
var toCity = $("input[name=toCity]");
var toState = $("select[name=toState]");
var toZip = $("input[name=toZip]");
var toAddressGroupRequired = [toName, toStreet1, toCity, toState, toZip];
var toAddressGroup = [toName, toStreet1, toStreet2, toCity, toState, toZip];
// PACKAGE
var packaging_group = $('input[name=packaging]');
var own_packaging_choices = $('#own_packaging_choices');
var flat_rate_choices = $('#flat_rate_choices');
var flat_rate_options = $('#flatRateOptions');
var packageLength = $("input[name=packageLength]");
var packageWidth = $("input[name=packageWidth]");
var packageHeight = $("input[name=packageHeight]");
var packageWeight = $("input[name=packageWeight]");
var packageWeightUnit = $("select[name=packageWeightUnit]");
var packageGroupRequired = [packageLength, packageWidth, packageHeight, packageWeight];
var packageGroup = [packaging_group, packageLength, packageWidth, packageHeight, packageWeight, packageWeightUnit];
// RATE
var rateButton = $("#rate_button");
var buyButton = $("#buy_button");
var ratePrice = $("#rate_price");
var buyTable = $("#buy-table");
var rateLoadingImage = $("#rate-loading-image");
var rateObjectId = null;
var rateAmount = null;
// LABEL
var labelModal = $("#labelModal");
var labelUrlButton = $("#labelUrlButton");
var labelTrackingNumber = $("#labelTrackingNumber");
var UspsTrackingUrl = $("#UspsTrackingUrl");