jQuery(document).ready(function(){
// masonry
    var $container = $('.grid-boxes');
    $container.imagesLoaded( function(){
        $container.masonry({
            itemSelector:'.grid-box',
            isAnimated:true
        });
    });

// Scroll
	$(window).scroll(function(){
		if($(window).scrollTop()>0){
			$('body').addClass('scroll_start');
            alert("$(window).scrollTop():"+$(window).scrollTop())
		} else {
			$('body').removeClass('scroll_start');
		};
	});

$.event.special.scrollstart = {
    enabled: true,

        setup: function() {
            var thisObject = this,
                $this = $( thisObject ),
                    scrolling,
                    timer;

            function trigger( event, state ) {
                scrolling = state;
                var originalType = event.type;
                event.type = scrolling ? "scrollstart" : "scrollstop";
                $.event.handle.call( thisObject, event );
                event.type = originalType;
            }

            // iPhone triggers scroll after a small delay; use touchmove instead
            $this.bind( scrollEvent, function( event ) {
                if ( !$.event.special.scrollstart.enabled ) {
                    return;
                }

                if ( !scrolling ) {
                    trigger( event, true );
                }

                clearTimeout( timer );
                timer = setTimeout(function() {
                    trigger( event, false );
                }, 50 );
            });
        }
};


// bxslider
	$('.bxslider').bxSlider({
		
	});

// menu
	$('div.wrapper').append('<button type="button" id="sidebar_tg" onclick="menuClose();"><b class="blind">Close</b></button>');

// modal
	$('.modal2 button[data-dismiss=modal]').click(function(){
		$('body').addClass('modal-open2');
		setTimeout('$(\'body\').addClass(\'modal-open\').removeClass(\'modal-open2\')',550)
	});
	$('body').on('click','[data-toggle=modal]',function(){
		if($($(this).attr('data-target')).hasClass('modal2')){
			$('body').addClass('modal_blk');
		} else {
			$('body').addClass('modal_wh').removeClass('modal_blk');
		};
	});
});

// Menu Open
function menuOpen(o){
	$('#'+o).show(function(){
		$('body').addClass('nav_open '+o+'_open');
	},0);
}

// Menu Close
function menuClose(){
	$('body').removeClass('nav_open snb_open mypage_open');
	setTimeout(function(){
		$('div.side_nav').hide()
	},500);
}