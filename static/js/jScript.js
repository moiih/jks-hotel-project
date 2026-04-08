
// function expand() {
//     if( document.getElementById("card1").hovered == true ) {
//         $("#card1").animate({ 'zoom': 1.2 }, 200);
//         $("#card2").animate({ 'zoom': 1 }, 200);
//         $("#card3").animate({ 'zoom': 1 }, 200);
//     }

//     if( document.getElementById("card2").hovered == true ) {
//         $("#card2").animate({ 'zoom': 1.2 }, 200);
//         $("#card1").animate({ 'zoom': 1 }, 200);
//         $("#card3").animate({ 'zoom': 1 }, 200);
//     }

//     if( document.getElementById("card3").click == true ) {
//         $("#card3").animate({ 'zoom': 1.2 }, 200);
//         $("#card1").animate({ 'zoom': 1 }, 200);
//         $("#card2").animate({ 'zoom': 1 }, 200);
//     }
// }




// Wrap every letter in a span
var textWrapper = document.querySelector('.ml2');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: true})
  .add({
    targets: '.ml2 .letter',
    scale: [4,1],
    opacity: [0,1],
    translateZ: 0,
    easing: "easeOutExpo",
    duration: 2000,
    delay: (el, i) => 70*i
  }).add({
    targets: '.ml2',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1000
  });
 
      
function mySlideDown() {
  $(".dropdown").click(function() {
    $("#dmenu").slideDown();
    alert("sdgkdsjn");
  });
}


// $(document).ready(function() {          
  
//   $('#btn-chat').click(function() {
      
//     if (!$('#btn-input').val()) {
//         alert('First Write Something To Send...!!');                            
//     }
//     else {                   
//         $("#chat-form").submit();
//     }    

//   }); 
  
// });


