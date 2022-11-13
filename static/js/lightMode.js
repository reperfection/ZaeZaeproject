const lightMode = document.querySelector(".js_lightMode");
const slide = document.querySelector(".slider");
const sideBar = document.querySelector(".sidebar");
lightMode.onclick = function () {
  slide.classList.toggle("light");
  sideBar.classList.toggle("light");
};
