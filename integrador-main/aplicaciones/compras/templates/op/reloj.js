(function (){

    var actualizarHora = function(){
        var fecha = new Date()
            horas = fecha.getHours(),
            minutos = fecha.getMinutes(),
            segundos = fecha.getSeconds(),
            diaSEM = fecha.getDay(),
            dia = fecha.getDate(),
            mes = fecha.getMonth(),
            year = fecha.getFullYear();
        
        var pHoras = document.getElementById('horas');
            pMinutos = document.getElementById('minutos');
            pSegundos = document.getElementById('segundos');
            pdiaSEM = document.getElementById('diaSEM');
            pdia = document.getElementById('dia');
            pmes = document.getElementById('mes');
            pyear = document.getElementById('year');

        var semana =['Domingo', 'Lunes','Martes','Miercoles','Jueves','Viernes','Sabado'];
        pdiaSEM.textContent = semana[diaSEM];

        pdia.textContent = dia;

        var meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'];
        pmes.textContent = meses[mes];

        pyear.textContent = year;
        pHoras.textContent = horas;

        if (minutos < 10) {minutos = "0"+ minutos};
        if (segundos < 10) {segundos = "0"+ segundos};
        pMinutos.textContent = minutos;
        pSegundos.textContent = segundos;  

    };

    actualizarHora();
    var intervalo = setInterval(actualizarHora, 1000);
    
}())