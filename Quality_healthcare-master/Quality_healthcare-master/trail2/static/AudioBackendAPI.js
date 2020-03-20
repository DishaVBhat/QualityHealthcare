var SpeechRecognition = window.webkitSpeechRecognition;
  
			var recognition = new SpeechRecognition();

			var instructions = $('instructions');

			var Content = '';

			recognition.continuous = true;

			recognition.onresult = function(event) {

			  var current = event.resultIndex;

			  var transcript = event.results[current][0].transcript;
			 
				Content += transcript;
				document.getElementById("demo").innerHTML = Content;
				document.getElementById('ajaxbtn').click();
				
			};

			recognition.onstart = function() { 
			  instructions.text('Voice recognition is ON.');
			}

			recognition.onspeechend = function() {
			  instructions.text('No activity.');
			}

			recognition.onerror = function(event) {
			  if(event.error == 'no-speech') {
				instructions.text('Try again.');  
			  }
			}

			$('#start-btn').on('click', function(e) {
			  if (Content.length) {
				Content += ' ';
			  }
			  recognition.start();
			});

			
	    $(document).ready(function() {
		     $('form').on('submit', function(event) {
		       $.ajax({
			  data : {
			     info : Content,
				 },
			     type : 'POST',
			     url : '/process'
			    })
			.done(function(data) {
			    $(".sub").remove()
			    var f = document.createElement("form");
			    f.setAttribute('method',"post");
			    f.setAttribute('action',"/");
			    f.className="sub"

			    var i;
			    var j=0;
			    var word;
			    word=data.output;

			    for(i=0;i<word.length;i++){
				if(word.slice(i,i+1)=='/'){
				    var s = document.createElement("input");
				    s.type = "submit";
				    s.value = word.slice(j,i);
				    f.appendChild(s);
				    j=i+1;
				}
			    }
			    
			    $("body").append(f);   //using jQuery or
			    document.getElementsByTagName('body')[0].appendChild(f); //pure javascript


			    //document.getElementsByClassName("tilting")[0].innerHTML= data.output+"heloooo";    
			    //document.getElementsById("tilt").innerHTML= data.key2;
			    
		      });
		      event.preventDefault();
		      });
		});	
