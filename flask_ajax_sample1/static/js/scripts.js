
$(document).ready(function() {

    var search_word ="konfu";
    var qurl="http://localhost:8080/api/hello";
    $.ajax({
            type: "POST",
            cache: false,
            data:{keyword:search_word},
            url: qurl,
            dataType: "json",
            success: function(data) { 
                alert(data);
                // console.log(data);                    
            },
            error: function(jqXHR) {
                alert("error: " + jqXHR.status);
                console.log(jqXHR);
            }
        })
});
