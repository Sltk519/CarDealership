// burger menu
const menu_btn = document.getElementById("menu-btn");
const menu = document.querySelector("#menu");
menu_btn.addEventListener("click", () => {
  menu.classList.toggle("hidden");
  menu.classList.toggle("flex");
});

// selecting cars for car comparisson
let selectedCars = [];

function toggleCarSelection(carId) {
  const index = selectedCars.indexOf(carId);
  if (index > -1) {
    selectedCars.splice(index, 1);
  } else {
    selectedCars.push(carId);
  }
}

function compareCars() {
  const url = new URL(window.location.origin + "/compare/");
  selectedCars.forEach((carId) => url.searchParams.append("car_ids", carId));
  window.location.href = url.toString();
}
