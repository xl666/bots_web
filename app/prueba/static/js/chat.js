
$(function(){

    function generar_respuestas(respuesta) {
	let res = "";
	for(var i = 0; i < respuesta.length; i++) {
	    if(!respuesta[i].trim().startsWith("<pre")) {
		res += '<div class="from-them">' + respuesta[i] + '</div>';
	    } else {
		res += '<div">' + respuesta[i] + '</div>';
	    }
	}
	let path_prism = "/static/js/prism.js"
	if(prefijo_sitio != "") {
	    path_prism = "/" + prefijo_sitio + "static/js/prism.js";
	}
	res += `<script src="${path_prism}"></script>`;
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
	    var contenido = $("#mensajesBox").html();
	    var mensaje = '<div class="from-me">' + data.mensaje + '</div>';    
	    var respuesta = generar_respuestas(data.respuesta);
	    $("#mensajesBox").html(contenido + mensaje + respuesta);
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
