$(function(){
    console.log('fooo');
    $('#add').submit(function(){

        data = $(this).serialize()

        $.post("/notes/create",data,function(res){
            $('.all_da_notes').html(res)
        })
        return false
    })

    $('.all_da_notes').on('submit',"form",function(){
        _id = $(this).children("input[type='hidden']").val()
        url = "notes/destroy/"  + _id
        $.post(url,function(res){
            $('.all_da_notes').html(res)
        })
        return false
    })


})
