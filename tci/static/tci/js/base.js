$(function() {
   
	
	$('.res-nav_click').click(function(){
		$('.main-nav').slideToggle();
		return false    

	});
	
	
	$('#goport').click(function()
   	{ 
	
		
		 
		 window.location = 'http://svn.bitasync.com/_Client/Client_Setup/BitaSyncInst.exe ';
			
	});
	
	$(window).resize(function() {
	
		var bh=$('body').height();
		var wh=$(window).height();

		if(bh<wh)
		{
			$('.main-section').height( (wh- bh)+$('.main-section').height());

			
		}
	}).resize();	
	
	
});

	