const usernameField = document.querySelector("#UserNameField");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#EmailField");
const emailFeedBackArea = document.querySelector(".EmailFeedbackArea");
const passwordField = document.querySelector("#PasswordField");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitBtn = document.querySelector(".submit-btn");


emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;
  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/Dashboard/validate-employee-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.email_error) {
          submitBtn.setAttribute = ('disabled', 'disabled');
          emailField.classList.add("is-invalid");
          emailFeedBackArea.style.display = "block";
          emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
          emailFeedBackArea.style.display = "none";
          emailField.classList.remove("is-invalid");
        }
      });
  }
});


usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;
  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";
  if (usernameVal.length > 0) {
    fetch("/Dashboard/validate-employee-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        usernameSuccessOutput.style.display = "none";
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
          submitBtn.setAttribute = ('disabled', 'disabled')
        } 
        else {
          submitBtn.removeAttribute("disabled");
          usernameField.classList.remove("is-invalid");
          feedBackArea.style.display = "none";
        }
      });
  }
});




const handleToggleInput = (e) => {
  if (showPasswordToggle.textContent === "SHOW") {
    showPasswordToggle.textContent = "HIDE";
    passwordField.setAttribute("type", "text");
  } else {
    showPasswordToggle.textContent = "SHOW";
    passwordField.setAttribute("type", "password");
  }
};

showPasswordToggle.addEventListener("click", handleToggleInput);



