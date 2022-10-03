// const formulario = document.getElementById('formularioProveedor');
// const inputs = document.querySelectorAll('#formularioProveedor input');

const expresiones = {
	// usuariof: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombref: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	correof: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0]+\.[a-zA-Z0-]+$/,
	telefonof: /^\d{10}$/ // 7 a 14 numeros.
}

function validar() {
    var nombre, ruc, email, telefono, ciudad, direccion;
    nombre = document.getElementById('id_nombre').value;
    ruc = document.getElementById('id_ruc').value;
    email = document.getElementById('id_email').value;
    telefono = document.getElementById('id_telefono').value;
    ciudad = document.getElementById('id_ciudad').value;
    direccion = document.getElementById('id_direccion').value;

    if(nombre === "" || ruc==="" || email===""|| telefono==="" || ciudad ==="" || direccion===""){
        alert("TODOS LOS CAMPOS DEBEN SER LLENADOS!");
        return false;
    }
    else if (!expresiones.nombref.test(nombre)){
        alert("El nombre que usted ha ingresado es incorrecto...");
        return false;
    }
    else if (!expresiones.nombref.test(ciudad)){
        alert("Ingrese una ciudad válida...");
        return false;
    }
    else if (!expresiones.nombref.test(direccion)){
        alert("Ingrese una dirección válida...");
        return false;
    }
    else if(!expresiones.telefonof.test(ruc)){
        alert("Ingrese un RUC correcto...")
        return false;
    }
    else if(!expresiones.telefonof.test(telefono)){
        alert("El número de teléfono ingresado está incorrecto...")
        return false;
    }
    else if(!expresiones.correof.test(email)){
        alert("El correo ingresado no está correcto...")
        return false;
    }
}







