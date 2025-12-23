const menu = document.getElementById("menu-hamburguesa");
const nav = document.getElementById("main-menu");

menu.addEventListener("click", () => {
  const abierto = nav.classList.toggle("open");
  menu.setAttribute("aria-expanded", abierto);
});

nav.querySelectorAll("a").forEach((a) => {
  a.addEventListener("click", () => {
    nav.classList.remove("open");
    menu.setAttribute("aria-expanded", "false");
  });
});