const usernameField = document.querySelector("#UserNameField");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#EmailField");
const emailFeedBackArea = document.querySelector(".EmailFeedbackArea");
const passwordField = document.querySelector("#PasswordField");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const showPasswordToggle = document.querySelector(".showPasswordToggle");

const BreakerUsername = document.querySelector("#breakerusername");
const BreakerEmail = document.querySelector("#breakeremail");



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

emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;
  BreakerEmail.style.display = "none";
  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display = "none";
  document.getElementById("main-submit-btn").disabled =false;
  console.log("In outside - ",document.getElementById("main-submit-btn").disabled);
  if (emailVal.length > 0) {
    fetch("/authentication/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.email_error) {
          document.getElementById("main-submit-btn").disabled =true;
          emailField.classList.add("is-invalid");
          BreakerEmail.style.display = "block";
          emailFeedBackArea.style.display = "block";
          emailFeedBackArea.innerHTML = `<small>${data.email_error}</small>`;
          console.log("In outside - ",document.getElementById("main-submit-btn").disabled);
        } else {
          document.getElementById("main-submit-btn").disabled =false;
          emailFeedBackArea.style.display = "none";
          emailField.classList.remove("is-invalid");
          BreakerEmail.style.display = "none";
          console.log("In outside - ",document.getElementById("main-submit-btn").disabled);
        }
      });
  }
});

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;

  BreakerUsername.style.display = "none";
  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";
  document.getElementById("main-submit-btn").disabled =false;

  if (usernameVal.length > 0) {
    fetch("/authentication/validate-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("resultusername", data);
        usernameSuccessOutput.style.display = "none";
        
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          BreakerUsername.style.display = "block";
          feedBackArea.innerHTML = `<small>${data.username_error}</small> <br>`;
          document.getElementById("main-submit-btn").disabled =true;
        } 
        else {
          BreakerUsername.style.display = "none";
          document.getElementById("main-submit-btn").disabled =false;
          usernameField.classList.remove("is-invalid");
          feedBackArea.style.display = "none";

        }
      });
  }
});
