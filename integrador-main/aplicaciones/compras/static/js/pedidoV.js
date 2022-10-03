const expresiones = {

	nombref: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	correof: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0]+\.[a-zA-Z0-]+$/,
	telefonof: /^\d{10}$/, // 7 a 14 numeros.
	ref: /^\d{7}$/
}

function validar() {
	var referencia, producto, cantidad, precio;
	referencia = document.getElementById("id_referencia").value;
	producto = document.getElementById("id_producto").value;
	cantidad = document.getElementById("id_cantidad").value;
	precio = document.getElementById("id_precio").value;


	if(referencia === "" || producto==="" || cantidad===""|| precio===""){
        alert("TODOS LOS CAMPOS DEBEN SER LLENADOS!");
        return false;
    }
	else if(isNaN(referencia)){
		alert("Sólo puede ingresar números en la referencia");
        return false;
	}
	else if(!expresiones.nombref.test(producto)){
		alert("Ingrese un producto correcto");
        return false;
	}
	else if(isNaN(cantidad)){
		alert("Sólo puede ingresar números");
        return false;
	}
	else if(isNaN(precio)){
		alert("Sólo puede ingresar números");
        return false;
	}

}