/* Javascript for SandBlock. */
function SandBlock(runtime, element) {

	function updateCount(result) {
		$('.count', element).text(result.count);
	}

	var handlerUrl = runtime.handlerUrl(element, 'increment_count');

	$('p', element).click(function(eventObject) {
		$.ajax({
			type: "POST",
			url: handlerUrl,
			data: JSON.stringify({"hello": "world"}),
			success: updateCount
		});
	});
	$('iframe', element).css('height','500');
	$('iframe', element).css('width','700');
	$('iframe', element).css('border','10px solid white');
	$('iframe', element).css('box-shadow','0px 0px 80px gray');
	 

	var opened = false;
	var _to = null;

	var otop = $('iframe', element).offset().top;
	var oleft = $('iframe', element).offset().left;
	var owidth = $('iframe', element).width();
	var oheight = $('iframe', element).height()

	$('iframe', element).mouseover(function()
	{

		if(_to)
		{
			window.clearTimeout(_to);
			_to=null;
		}

		_to = window.setTimeout(function(){


			$('iframe', element).css('position','fixed');
			$('iframe', element).css('z-index','1000000');
			$('iframe', element).css('box-shadow','0px 0px 180px gray');
			$('iframe', element).css('top',otop)
			$('iframe', element).css('left',oleft)
			$('iframe', element).css('width',owidth)
			$('iframe', element).css('height',oheight)

			$('iframe', element).animate({
				'top':'15%',
				'left':'15%',
				'width':'70%',
				'height':'70%'
			});

		},1500);
			  		
	});

	$('iframe', element).mouseout(function()
	{
		if(_to)
		{
			window.clearTimeout(_to);
			_to=null;
		}

		_to = window.setTimeout(function(){
			$('iframe', element).animate(
				{
					'top':otop,
					'left':oleft,
					'width':owidth,
					'height':oheight
				},
				function(){
					$('iframe', element).css('top','')
					$('iframe', element).css('left','')
					$('iframe', element).css('height','500');
					$('iframe', element).css('width','700');
					$('iframe', element).css('position','');
					$('iframe', element).css('z-index','');
					$('iframe', element).css('box-shadow','0px 0px 80px gray');
				}
			);
		},1500);
	});
 
	$(function ($) {
		/* Here's where you'd do things on page load. */
	});
}
