// onclick method for the login button
function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var data = JSON.stringify({
        "email": email,
        "password": password
    });
    sendHTTPAsync("/login", "POST", data, function(response) {
        server_response = JSON.parse(response).response;
        if (server_response == "success") {
            // trigger the page to reload
            window.location.href = "/dashboard";
        } else {
            console.log(server_response);
            document.getElementById("login_error").innerHTML = server_response;
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