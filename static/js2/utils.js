// JavaScript Document

	$(document).ready(function(){
		
        $('#iid_password').focusin(setFocusIn);
		
		$("#publicidad_2").hide();
		var publicidad_interval = setInterval(function() { $('#publicidad_2').load(baseurl + 'index.php/mypublicidad/get_ads/5', function(response, status, xhr) { fader($("#publicidad_1"), $("#publicidad_2"), response) });}, 40000);
	
	});
	
//estas funciones setFocusIn y setFocusOut las uso para el input del password en la linea de logueo....	 	
	function setFocusIn() {	
       if (($(this).attr('type') == 'text') && ($(this).attr('value') == 'Contraseña')) {
			  $(this).remove();              
              $("#password_div").append('<input id="id_password" class="text" name="password" type="password" value=""/>');
              $('#id_password').focusout(setFocusOut);
              setTimeout(function() { $('#id_password').focus(); }, 0);
			 
	   }
       return false;
     }
	 
	 function setFocusOut() {
	   if (($(this).attr('type') == 'password') && ($(this).attr('value') == '')) {
			  $(this).remove();              
              $("#password_div").append('<input id="id_password" class="text" name="password" type="text" value="Contraseña"/>');
              $('#id_password').focusin(setFocusIn);
	   }
       return false;
     }
	 
	 
	 
	 function fader(obj1, obj2, html_value) {
		 obj1.hide(800);
		 obj2.show(800, function() { obj1.html(html_value); obj1.show(); obj2.hide(); });
     }
