const body = document.querySelector("body");
const modal = document.querySelector(".recommend_modal");
const btnOpenPopup = document.querySelector(".recommend_btn");

btnOpenPopup.addEventListener("click", () => {
  modal.classList.toggle("show");

  if (modal.classList.contains("show")) {
    body.style.overflow = "hidden";
  }
});

modal.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.classList.toggle("show");

    if (!modal.classList.contains("show")) {
      body.style.overflow = "auto";
    }
  }
});
