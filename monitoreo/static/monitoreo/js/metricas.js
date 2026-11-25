
async function actualizarMetricas() {
    try {
        const respuesta = await fetch("/api/metricas/", {
            cache: "no-store"
        });

        if (!respuesta.ok) {
            throw new Error("Error de conexion");
        }

        const datos = await respuesta.json();

        actualizarTarjeta("cpu", datos.cpu, "%");
        actualizarTarjeta("ram", datos.ram, "%");
        actualizarTarjeta("temperatura", datos.temperatura, "°C");

        document.getElementById("estado").textContent =
            "Última actualización: " +
            new Date().toLocaleTimeString();

    } catch (error) {
        document.getElementById("estado").textContent =
            "Error al conectar con el servidor";

        console.error(error);
    } finally {
        setTimeout(actualizarMetricas, 3000);
    }
}


function actualizarTarjeta(nombre, valor, unidad) {
    const texto = document.getElementById(nombre);
    const barra = document.getElementById("barra-" + nombre);

    if (valor === null) {
        texto.textContent = "-- " + unidad;
        barra.style.width = "0%";
        return;
    }

    texto.textContent = valor.toFixed(1) + " " + unidad;

    barra.style.width =
        Math.max(0, Math.min(valor, 100)) + "%";

    if (valor >= 80) {
        barra.style.backgroundColor = "#dc2626";
    } else if (valor >= 60) {
        barra.style.backgroundColor = "#f59e0b";
    } else {
        barra.style.backgroundColor = "#2563eb";
    }
}

actualizarMetricas();

