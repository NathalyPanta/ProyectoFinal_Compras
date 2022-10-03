function pedido(){
    let cantidad = Number(document.getElementById("id_cantidad").value)
    let precio = Number(document.getElementById("id_precio").value)
        console.log(cantidad)
        console.log(precio)
    x = cantidad * precio
    subtotal = x.toFixed(2)
    let subtotalf = document.getElementById("id_subtotal")
    subtotalf.value= subtotal

    iva1 = subtotal * 0.12
    iva2 = iva1.toFixed(2)
    let ivaf = document.getElementById("id_iva")
    ivaf.value = iva2
    console.log(iva1)

    s=(Number(iva1))
    console.log(s)
    d=(Number(subtotal))
    console.log(d)

    totfinal= s+d
    let final = document.getElementById(("id_total"))
    final.value = totfinal
    // console.log(Number(subtotal + iva1))
    // console.log(Number(s + d))




}