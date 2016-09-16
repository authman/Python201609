$(document).ready(function(){

    $('form').submit(function(){
        var appid = "1086e6ef833eda7246bfe1fa90897b94"
        var city = $("form [type='text']").val().split(" ").join("%20")
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city
        url += "&APPID=" + appid
        $.get(url, function(res) {
            console.log(res)
            if (res['message']){
                description =res['message']
                temp=""
            }else{
                description = res['weather'][0]['description']
                temp = res['main']['temp']
                temp = temp * (9/5) - 459.67
                temp = Math.round(temp)
            }

            $( "#description" ).text(description);
            $( "#temp" ).text(temp);

        }, 'json');


        return false
    })
})
