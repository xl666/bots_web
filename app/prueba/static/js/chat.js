
$(function(){

    function generar_respuestas(respuesta) {
	let res = "";
	for(var i = 0; i < respuesta.length-1; i++) {
	    res += '<span class="badge  bg-danger"><b>' + respuesta[i] + '</b></span><br />';
	}
	res += '<span class="badge  bg-danger"><b>' + respuesta[i] + '</b></span>';
	return res;
    }
    
    function mandar_recibir_mensaje() {
	var url = "/enviar_mensaje/";
	if(prefijo_sitio != "") {
	    url = "/" + prefijo_sitio + "enviar_mensaje/";
	}
	$.post(url, {
	    mensaje: $("#mensaje").val(),
	    host: host_bot,
	    puerto: puerto_bot,
	}, function(data, status){
	    var contenido = $("#mensajesBox").html() + "<br />";
	    var mensaje = '<span class="badge  bg-primary" style="float: right;"><b>' + data.mensaje + '</b></span>';    
	    var respuesta = generar_respuestas(data.respuesta);
	    $("#mensajesBox").html(contenido + mensaje + "<br />" + respuesta);
		$('#mensajesBox').scrollTop($('#mensajesBox')[0].scrollHeight);
		$('#mensaje').val("");
	    });
    }
    
    $("#bEnviar").click(mandar_recibir_mensaje);
    $('#mensaje').keydown(function(event){
	if (event.which == 13){
	    mandar_recibir_mensaje();
	}
    });

});
