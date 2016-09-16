$(document).ready(function(){

    $('form').submit(function(){
        //build url
        var city = $("form [type='text']").val().split(" ").join("%20")
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city
        url += "&APPID=" + appid

        $.get(url, function(res) {
            // parse data from res JSON object
            description = res['weather'][0]['description']
            degK = res['main']['temp']
            degF = degK * (9/5) - 459.67 // convert to farenheight
            degF = Math.round(degF)
            //update page
            $( "#description" ).text(description);
            $( "#temp" ).text(degF);
        }, 'json');
        
        return false
    })
})
