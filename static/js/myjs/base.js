$(function(){
        renderArticle();
    })
    function renderArticle(){
        var articles={{articles|safe}};
        var master_card=$('.master-card');
        var left=$('.left-part');
        var right=$('.right-part');
        var lHeight=0,rHeight=0;
        for(i=0;i<articles.length;i++){
            var isLeft=false;
            var sub_card;
            if(lHeight<rHeight){
                isLeft=true;
                master_card.clone(false).appendTo(left);
                sub_card=left.children().last();
            }
            else{
                master_card.clone(false).appendTo(right);
                sub_card=right.children().last();
            }
            sub_card.children().children('.time-views').children('.c-time').text(articles[i].create_time);
            sub_card.children().children('.time-views').children('.views').html(articles[i].browse+'&nbspviews');
            sub_card.children().children('.card-title').html(articles[i].title);
            sub_card.children().children('.card-text').html(articles[i].content);
            sub_card.children().children('.read-more').children('a').attr('href','/blog/'+articles[i].id+'.html');
            sub_card.children('.card-footer').children('.category').html('<b>#</b>'+articles[i].category);
            var height=Math.random()*100+350;
            sub_card.children().children('.card-text').css({'max-height':height,'overflow':'hidden'});
            sub_card.removeClass('d-none');
            if(isLeft){
                lHeight+=height;
            }
            else{
                rHeight+=height;
            }
        }
    }