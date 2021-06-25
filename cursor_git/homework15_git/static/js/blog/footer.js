$(document).ready(function () {
    $.ajax({
        method: "GET",
        url: "/contacts",
        success: function (data) {
            if (data.success) {
                for (let el of data.items){
                    let contact = "<li class=\"nav-item\">\n" +
                        "<p>" + el.name + ":" +
                        "<a class=\"nav-link active nav-link-footer\" aria-current=\"page\" href=\""+ el.link +"\">" + el.link +"</a>" + "</p>" +
                        " </li>"
                        $("#ContactListfooter").append(contact)
                }
            }
        }
    });
});