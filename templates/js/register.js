// onclick method for the login button
function register() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var data = JSON.stringify({
        "email": email,
        "password": password
    });
    sendHTTPAsync("/register", "POST", data, function(response) {
        if (response.status == 200) {
            server_response = JSON.parse(response).response;
            if (server_response == "success") {
                window.location = "/dashboard";
            } else {
                document.getElementById("register_error").innerHTML = server_response;
            }
        } else {
            // get the error message from the response
            var error = JSON.parse(response).response;
            // put the error message into login_error span
            document.getElementById("register_error").innerHTML = error;
        }
    });
}

function sendHTTPAsync(url, method, data, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            callback(xhr.responseText);
        }
    }
    xhr.send(data);
}

// assign the onclick method to the login button
document.getElementById("register").onclick = register;

// add form validation to the password fields
document.getElementById("password").onkeyup = function() {
    var password = document.getElementById("password").value;
    if (password.length < 8) {
        document.getElementById("password_error").innerHTML = "Password must be at least 8 characters long";
    } else {
        document.getElementById("password_error").innerHTML = "";
    }
}

document.getElementById("confirm_password").onkeyup = function() {
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;
    if (password != confirm_password) {
        document.getElementById("confirm_password_error").innerHTML = "Passwords do not match";
    } else {
        document.getElementById("confirm_password_error").innerHTML = "";
    }
}