$(function(){
	$('.req').change(function(){
		if($('#food').val() == '' || $('#shirt').val() == '' || $('#name').val() == '') {
			alert("Disabled");
			$('#button').attr('disabled',true)
		} else {
			alert("Enabled");
			$('#button').attr('disabled',false)
		}
	});
});
