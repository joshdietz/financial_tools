// onclick method for the login button
function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var data = JSON.stringify({
        "email": email,
        "password": password
    });
    sendHTTPAsync("/login", "POST", data, function(response) {
        if (response.status == 200) {
            window.location.href = "/home";
        } else {
            alert("Login failed");
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
document.getElementById("login").onclick = login;