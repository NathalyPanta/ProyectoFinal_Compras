const expresiones = {

	nombref: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	correof: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0]+\.[a-zA-Z0-]+$/,
	telefonof: /^\d{10}$/ // 7 a 14 numeros.
}

function validar() {
    var producto, cantidad, precio;
	producto = document.getElementById("id_producto").value;
	cantidad = document.getElementById("id_cantidad").value;
	precio = document.getElementById("id_precio").value;

	if(producto === "" || cantidad==="" || precio===""){
        alert("TODOS LOS CAMPOS DEBEN SER LLENADOS!");
        return false;
    }
	else if(expresiones.nombref.test(producto)){
		alert("Ingrese producto válido")
		return false;
	}
	else if(isNaN(cantidad)){
		alert("Sólo debe ingresar número")
		return false;
	}
	else if(isNaN(precio)){
		alert("Sólo debe ingresar número")
		return false;
	}


}