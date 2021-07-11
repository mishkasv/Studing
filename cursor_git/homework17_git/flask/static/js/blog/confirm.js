let button_code = document.getElementById('code_confirm');
button_code.addEventListener('click', function (e) {
    e.preventDefault();
    e.stopPropagation();
    let code = document.getElementById('code');
    var token = document.get("{{token}}");
    if (code.value != token) {
    console.log(code.value, token);
    alert("Something went wrong! Please try again!");
    } else {
    fetch("/user-register", {
        method: "POST",
        body: '{{data}}',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        if (response.status == 200) {
            windows.location.replace('http://localhost:5000/');
        }})};
});