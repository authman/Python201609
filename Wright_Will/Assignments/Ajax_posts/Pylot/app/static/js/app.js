
$(function(){
    $.get('/posts/html',$(this).serialize(),function(res){
        $('#all_da_posts').html(res)
    })


    //event handlers
    $('.add_post').submit(function(){
        $.post('/posts/create',$(this).serialize(),function(res){
            $('#all_da_posts').html(res)
        })
        return false;
    })

    $(document).on('submit','.delete_post',function(){
        $.post('/posts/destroy',$(this).serialize(),function(res){
            $('#all_da_posts').html(res)
        })
        return false;
    })

})
