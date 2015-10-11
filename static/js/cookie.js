var addressFromCookieName = "oml_addfr";  
var packageCookieName = "oml_packg";
readCookies();

function getCookie(cookieName){
    var name = cookieName + "=";
    var cookieArray = document.cookie.split(';'); //break cookie into array
    for(var i = 0; i < cookieArray.length; i++){
      var cookie = cookieArray[i].replace(/^\s+|\s+$/g, ''); //replace all space with '' = delete it
      if (cookie.indexOf(name)==0){
         return cookie.substring(name.length,cookie.length);
      }
    }
    return null;
}

function setCookie(cookie, value, expiryDays){
    var expires = new Date();
    var domain = window.location.hostname;
    expires.setTime(expires.getTime() + (1000*60*60*24*expiryDays));
    document.cookie = cookie + "=" + value + "; expires=" + expires.toGMTString() + "; domain=" + domain + "; path=/";
}

function updateCookies(){
  var addressFromCookieValue = encodeURIComponent(serializeFields(fromAddressGroup));
  var packageCookieValue = encodeURIComponent(serializeFields(packageGroup));
  setCookie(addressFromCookieName, addressFromCookieValue, 365);
  setCookie(packageCookieName, packageCookieValue, 365);
}

function readCookies(){
  updateFieldsFromCookie(addressFromCookieName);
  updateFieldsFromCookie(packageCookieName);
}

function updateFieldsFromCookie(cookieName){
  var cookieText = getCookie(cookieName);
  if (!(cookieText)){
    return null;
  }
  var cookieValues = JSON.parse(decodeURIComponent(cookieText));
  $.each(cookieValues, function(index, obj){
    $("#"+obj.id).val(obj.value);
  })
}

function serializeFields(fields){
  data = [];
  $.each(fields, function(index, value){
    if ( value.val() ){
      data.push({id: value.attr('id'), value: value.val()});
    }
  });
  return JSON.stringify(data);
}