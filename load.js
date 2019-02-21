var loader;

			function loadit (opacity) {
				if(opacity<=0){
					displayContent();
				}
				else{
					loader.style.opacity=opacity;
					window.setTimeout(function(){
						loadit(opacity-0.03)
					},100);
				}
			}

			function displayContent(){
				loader.style.display='none';
				document.getElementById("content").style.display='block';
			}

			document.addEventListener('DOMContentLoaded', function(){
				loader=document.getElementById('load');
				loadit(1);
			});