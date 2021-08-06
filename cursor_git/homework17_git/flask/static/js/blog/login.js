let signinButton = document.getElementById('signin');
signinButton.addEventListener('click', function (e) {
    e.preventDefault();

    let data = {
         username: document.getElementById('username').value,
         password: document.getElementById('password').value,
    };
    fetch("/api/login", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(response => {
        if (response.status == 200) {
            window.location.replace('http://localhost/');
        } else {
            alert("You type wrong password or username.Try again");
        }
    })
})