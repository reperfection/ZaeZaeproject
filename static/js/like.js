const like = document.querySelector(".like");
const animationLike = document.querySelector(".animation-like");

like.addEventListener("click", () => {
  animationLike.classList.add("animation");
  like.classList.add("fill-color");
});

animationLike.addEventListener("click", () => {
  animationLike.classList.remove("animation");
  like.classList.remove("fill-color");
});
