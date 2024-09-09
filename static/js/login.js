const showPasswordToggle = document.querySelector(".showPasswordToggle")
const PasswordField = document.querySelector("#PasswordField")


const handleToggleInput = (e) => {
    if (showPasswordToggle.textContent === "SHOW"){
        showPasswordToggle.textContent = "HIDE";
        PasswordField.setAttribute("type", "text");
    }
    else {
        showPasswordToggle.textContent = "SHOW";
        PasswordField.setAttribute("type", "password");

    }

};
showPasswordToggle.addEventListener("click", handleToggleInput);
