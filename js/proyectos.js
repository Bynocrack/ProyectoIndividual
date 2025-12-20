let sliderInner = document.querySelector('.slider--inner');

let proyectos = document.querySelectorAll('.proyecto');
let index = 0;

setInterval(() => {
  let percentaje = index * -100;
  sliderInner.style.transform = "translateX(" + percentaje + "%)";

  index++;
  if (index > proyectos.length - 1) {
    index = 0;
  }
}, 5000);