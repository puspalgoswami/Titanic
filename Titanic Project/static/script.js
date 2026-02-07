const fareSlider = document.getElementById("fare");
const fareValue = document.getElementById("fareValue");

if (fareSlider && fareValue) {

    fareValue.innerText = fareSlider.value;

    fareSlider.addEventListener("input", () => {
        fareValue.innerText = fareSlider.value;
    });
}
