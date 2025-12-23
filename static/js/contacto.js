let boton = document.getElementById('enviar--form');

boton.addEventListener('click', async () => {
  let presupuesto = document.querySelector('input[name="presupuesto"]').value;
  try {
    if (isNaN(presupuesto)) throw new Error();
    if (Number(presupuesto) < 0) throw new Error(); 
  } catch (error) {
    alert("El presupuesto debe ser un número válido.");
    return;
  }
  const respuesta = await fetch('/contacto', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      nombre: document.querySelector('input[name="nombre"]').value,
      presupuesto: document.querySelector('input[name="presupuesto"]').value,
      correo: document.querySelector('input[name="correo"]').value,
      mensaje: document.querySelector('textarea[name="mensaje"]').value
    })
  });
  const data = await respuesta.json();
  console.log(data);
});