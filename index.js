var body = document.getElementById("body");
var gui = document.getElementById("gui");
var grid = document.getElementById("grid");
var gridItem = document.querySelectorAll(".grid-item");
var largeGridItem = document.querySelectorAll(".large-grid-item");
var shadeCheck = document.getElementById("shadeCheck");
var stopBtn = document.getElementById("stopBtn");
var startBtn = document.getElementById("startBtn");
var prevBtn = document.getElementById("prevBtn");
var nextBtn = document.getElementById("nextBtn");
var csvBtn = document.getElementById("csvBtn");
var modalContent = document.getElementById("modalContent");
var modal = document.getElementById("modal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
var welcomePage = document.getElementById("welcomePage")
var statusBar = document.getElementById('statusBar')


//Data description Slider
shadeCheck.addEventListener("change", function(e){
	if (shadeCheck.checked){
		body.style.setProperty('background-color',"rgb(255,255,255)");
		gui.style.setProperty('background-color',"rgb(236,236,236)");

		modalContent.style.setProperty("background-color", "rgb(236,236,236)");
		modalContent.style.setProperty("color", "black");
		Array.from(gridItem).forEach((f)=> {
    	f.style.setProperty('color', "black");});	}
	if (!shadeCheck.checked) {
		body.style.setProperty('background-color',"rgb(54, 57, 63)");
		gui.style.setProperty('background-color',"rgb(47, 49, 54)");

		modalContent.style.setProperty("background-color", "rgb(54, 57, 63)");
		modalContent.style.setProperty("color", "white");
		Array.from(gridItem).forEach((f)=> {
		    f.style.setProperty('color', "white");
		});	}
});
//Data description Slider

//Darkmode and Lightmode switching
shadeCheck.addEventListener("change", function(e){
	if (shadeCheck.checked){//lightmode
		body.style.setProperty('background-color',"rgb(255,255,255)");
		gui.style.setProperty('background-color',"rgb(255,255,255)");

   		prevBtn.classList.remove("arrowDark");
   		prevBtn.classList.add("arrowLight");
   		nextBtn.classList.remove("arrowDark");
   		nextBtn.classList.add("arrowLight");

   		welcomePage.style.setProperty('color', "black");

		Array.from(gridItem).forEach((f)=> {
    	f.style.setProperty('color', "black");});	}

	if (!shadeCheck.checked){
		body.style.setProperty('background-color',"rgb(54, 57, 63)");

   		prevBtn.classList.remove("arrowLight");
   		prevBtn.classList.add("arrowDark");
   		nextBtn.classList.remove("arrowLight");
   		nextBtn.classList.add("arrowDark");   	

   		welcomePage.style.setProperty('color', "white");

		gui.style.setProperty('background-color',"rgb(47, 49, 54)");
		Array.from(gridItem).forEach((f)=> {
		    f.style.setProperty('color', "white");
		});	}
});
//Darkmode and Lightmode switching

Array.from(gridItem).forEach((gridItem)=> {
	gridItem.style.display = "none" //no grid items should be showing when car is not connected

});

//Pop-up for grid items with live data update
gridItem.forEach((gridItem,i)=> {
  gridItem.addEventListener("click", function(){
  if (!descCheck.checked){//shows desc 
    largeGridItem[0].firstChild.nextSibling.style.opacity = "0"; 
    largeGridItem[0].firstChild.style.opacity = "0";
    largeGridItem[0].firstChild.nextSibling.nextSibling.style.opacity = "1";  
    indexOfLargeGridItem = i //for large display when gridItem is clicked, we send index of gridItem to view it on largeGridItem

  }
  if (descCheck.checked){//shows data with units
    largeGridItem[0].firstChild.nextSibling.style.opacity = "1"; 
    largeGridItem[0].firstChild.style.opacity = "1";
    largeGridItem[0].firstChild.nextSibling.nextSibling.style.opacity = "0";
    largeGridItem[0].firstChild.nextSibling.textContent = gridItem.firstChild.nextSibling.textContent;
    indexOfLargeGridItem = i //for large display when gridItem is clicked, we send index of gridItem to view it on largeGridItem
  }
  modal.style.display = "block";
  span.onclick = function() {
    modal.style.display = "none";
  }
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  } 
  });
});
//Pop-up for grid items with live data update


 	
