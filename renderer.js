// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.
var largeGridItem = document.querySelectorAll(".large-grid-item");
var gridItem = document.querySelectorAll(".grid-item");
var descCheck = document.getElementById("descCheck");
var csvBtn = document.getElementById("csvBtn");
var dataList = []
var descList = [];
var unitsList = [];
var indexOfLargeGridItem; 
const maxItemsPerPage = 20;

const electron = require("electron")
const ipc = electron.ipcRenderer


////////////////////              Utility Functions           ////////////////////
function disableButton(button){
  button.disabled = true
  console.log(button.disabled)
}

function enableButton(button){
  button.disabled = false
}

function setStatusMessage(text, color){
  statusBar.value = text
  statusBar.style.setProperty("color",color)
}

function setMaxDisplay(){
    grid = document.querySelectorAll(".grid-item");
    if (descList.length >= 20){
      for (let i = maxItemsPerPage;i < gridItem.length;i++){
        gridItem[i].style.display = "none"
      }
      for (let i = 0;i < maxItemsPerPage;i++){
        gridItem[i].style.display = "block"
      }      
    }
    if (descList.length < 20){
      for (let i = descList.length;i < gridItem.length;i++){
        gridItem[i].style.display = "none"
      }
    }
}

function toggleWelcomePage(){
  welcomePage.style.display = "none"
}

function isLastPage(){
  for (let i = 0; i<gridItem.length; i++){
      console.log(i, gridItem[i].style.display, "desc length", descList.length-1)  
      if (gridItem[i].style.display == "block" && i == descList.length-1){
        return true
      }
      else{
        continue
      } 
  }
  return false
}

function isFirstPage(){
  for (let i = 0; i<gridItem.length; i++){
      if (gridItem[i].style.display == "block" && i == 0){
        return true
      }
      else{
        continue
      } 
  }
  return false
}

function arrowBtnStatus(){//dims or glows the arrow button as user navigates
  if (descList.length/maxItemsPerPage<=2){
    nextBtn.style.setProperty("opacity", "1")
    prevBtn.style.setProperty("opacity", "1")  
  }
  else if (isFirstPage()){
    prevBtn.style.setProperty("opacity", "0.2") 
    console.log("off prev")   
  }
  else if (isLastPage()){
    nextBtn.style.setProperty("opacity", "0.2")    
    console.log("off next")     
  }
  else{
    nextBtn.style.setProperty("opacity", "1")
    prevBtn.style.setProperty("opacity", "1")      
  }      
}

function getCurrentPage(){//hardcoded to search for 6 pages that contain hardcoded amount of ~115 grid items
  if (gridItem[0*maxItemsPerPage].style.display == "block"){
    return 1 //means we are on first page (grid item 1-20)
  }
  else if(gridItem[1*maxItemsPerPage].style.display == "block"){
    return 2    
  }
  else if(gridItem[2*maxItemsPerPage].style.display == "block"){
    return 3    
  }
  else if(gridItem[3*maxItemsPerPage].style.display == "block"){
    return 4    
  }        
  else if(gridItem[4*maxItemsPerPage].style.display == "block"){
    return 5    
  }
  else {
    return 6    
  }   
}

function prev(gridItem, current_page){ 
    //delete not needed grid items
  if (isLastPage()){
    for (let i = (current_page)*maxItemsPerPage;i < descList.length;i++){
      gridItem[i].style.display = "none"
    }           
  }
  else{
    for (let i = (current_page+1)*maxItemsPerPage;i < gridItem.length;i++){
      gridItem[i].style.display = "none"
    }    
    for (let i = (current_page)*maxItemsPerPage;i < (current_page+1)*maxItemsPerPage;i++){
    gridItem[i].style.display = "none"
    }  
  }

  //adding grid items accordingly. if its the first page, nothing needs to be done.
  if (!isFirstPage()){
    for (let i = (current_page-1)*maxItemsPerPage;i < (current_page)*maxItemsPerPage ;i++){
      gridItem[i].style.display = "block"
    }     
  }
  arrowBtnStatus()    
}

function next(gridItem, current_page){ 

    //delete not needed grid items
  console.log(current_page)
  for (let i = (current_page-1)*maxItemsPerPage;i < (current_page)*maxItemsPerPage;i++){
    gridItem[i].style.display = "none"
  }
  for (let i = (current_page+1)*maxItemsPerPage;i < gridItem.length;i++){
    gridItem[i].style.display = "none"

  }
  //adding grid items depending if its the last page or not
  if ((current_page+1)*maxItemsPerPage > descList.length){         
    for (let i = (current_page)*maxItemsPerPage;i < descList.length ;i++){
      gridItem[i].style.display = "block"
    }
  }
  if ((current_page+1)*maxItemsPerPage <= descList.length){         
    for (let i = (current_page)*maxItemsPerPage;i < (current_page+1)*maxItemsPerPage ;i++){
      gridItem[i].style.display = "block"
    }
  }     
  arrowBtnStatus()          
}
////////////////////              Utility Functions           ////////////////////


////////////////////              UI Event Listeners          ////////////////////
nextBtn.addEventListener("click",function(e){
  if (!isLastPage()){
    if (getCurrentPage(gridItem) == 1){
      next(gridItem,1) //going from page 1 to next page
    }
    else if(getCurrentPage(gridItem) == 2){
      next(gridItem,2)    
    }
    else if(getCurrentPage(gridItem) == 3){
      next(gridItem, 3)  
    }
    else if(getCurrentPage(gridItem) == 4){
      next(gridItem, 4)  
    }        
    else if(getCurrentPage(gridItem) == 5){
      next(gridItem, 5)  
    }
    else {
      next(gridItem, 6)  
    }
  }
  else{
    console.log("can't go past last page")
  }      
})

prevBtn.addEventListener("click",function(e){
  if (!isFirstPage()){
    if(getCurrentPage(gridItem) == 2){
      prev(gridItem,1)    
    }
    else if(getCurrentPage(gridItem) == 3){
      prev(gridItem, 2)  
    }
    else if(getCurrentPage(gridItem) == 4){
      prev(gridItem, 3)  
    }        
    else if(getCurrentPage(gridItem) == 5){
      prev(gridItem, 4)  
    }
    else if(getCurrentPage(gridItem) == 6){
      prev(gridItem, 5)  
    }    
  }
  else{
    console.log("can't go before first page")
  }        
})
descCheck.addEventListener("change", function(e){// render description tags on grid items when they are available
  if (descCheck.checked){
    largeGridItem[0].firstChild.nextSibling.style.opacity = "1"; 
    largeGridItem[0].firstChild.style.opacity = "1";
    largeGridItem[0].firstChild.nextSibling.nextSibling.style.opacity = "0";
    var ctr = 0;
    Array.from(gridItem).forEach((gridItem)=> {
      gridItem.firstChild.nextSibling.style.opacity = "1"; 
      gridItem.firstChild.style.opacity = "1";
      gridItem.firstChild.nextSibling.nextSibling.style.opacity = "0";

      ctr=ctr+1;
    });  
  } 

  if (!descCheck.checked){
    var ctr = 0;
    largeGridItem[0].firstChild.nextSibling.style.opacity = "0"; 
    largeGridItem[0].firstChild.style.opacity = "0";
    largeGridItem[0].firstChild.nextSibling.nextSibling.style.opacity = "1";    
    Array.from(gridItem).forEach((gridItem)=> {
      gridItem.firstChild.nextSibling.style.opacity = "0";
      gridItem.firstChild.style.opacity = "0";
      gridItem.firstChild.nextSibling.nextSibling.style.opacity = "1";  

      if(descList && descList.length){
        gridItem.firstChild.nextSibling.nextSibling.textContent = descList[ctr];
      }
      else{
        gridItem.firstChild.nextSibling.nextSibling.textContent = "Waiting for connection to vehicle"
      }
      ctr=ctr+1;});    
  }
});


csvBtn.addEventListener("click", function(e){
  ipc.send('stop')
  disableButton(csvBtn)
});

startBtn.addEventListener("click", function(e){
  console.log("getting getMetadata from main.js")
  ipc.send('getMetadata')
  setStatusMessage("Finding compatible ECU sensors", "red")  
});
////////////////////              UI Event Listeners          ////////////////////


////////////////////              IPC with main.js           ////////////////////

ipc.on('getMetadata', function(event, arg){
  setStatusMessage("Found compatible ECU sensors","limegreen") 
  disableButton(startBtn)

  var ctr = 0;
  const commandNames = arg[0]
  const commandNameDesc = arg[1]
  const commandNameUnits = arg[2]

  unitsList = commandNameUnits
  descList = commandNameDesc;
  // console.log(descList)

  toggleWelcomePage()
  setMaxDisplay()

  gridItem.forEach((gridItem,i)=> {
    gridItem.firstChild.nextSibling.textContent = commandNameUnits[i]; //set units for each sensor
  });

  gridItem.forEach((gridItem)=> {
    if (gridItem.firstChild.nextSibling.textContent.length > 20){
      gridItem.firstChild.nextSibling.style.fontSize = "0.85em"       //adjust size if unit name is too long
    }
  });

  ipc.send('start')
  setStatusMessage("Initiating data collection with car", "red")
})

ipc.on('start', function(event,arg){
  if (arg){
    var ctr = 0
    dataList = arg //store a global reference of data just in case
    // console.log(dataList)
    gridItem.forEach((gridItem,i)=> {
      setStatusMessage("Data collection in progress", "limegreen")
      gridItem.firstChild.textContent = arg[ctr]
      ctr=ctr+1;

      if (largeGridItem[0].firstChild.textContent.length > 15){//dynamically change size of largeGridItem/modal based on text length
        largeGridItem[0].firstChild.style.fontSize = "1em"
        largeGridItem[0].firstChild.nextSibling.style.fontSize = "1.5em"
      }
      else{
        largeGridItem[0].firstChild.style.fontSize = "5em"
      }

      largeGridItem[0].firstChild.textContent = arg[indexOfLargeGridItem];//magical line that shows data in the pop-up modal
      
      if (!descCheck.checked){
        largeGridItem[0].firstChild.nextSibling.nextSibling.textContent =  descList[indexOfLargeGridItem] //show description in large grid item as well

      }

    });  

    gridItem.forEach((gridItem)=> {
      let h1Tag = gridItem.firstChild;
      let h2Tag = gridItem.firstChild.nextSibling;
      if (h1Tag.textContent.length > 8){
        h1Tag.textContent = "Too large, click to see"
        h1Tag.style.fontSize = "2em";
      }    

      else if (h1Tag.textContent.length > 6 && h1Tag.textContent.length <= 8){
        h1Tag.style.fontSize = "2em";
      }

      else if (h1Tag.textContent.length > 4 && h1Tag.textContent.length <= 6){
        h1Tag.style.fontSize = "3.5em";
      }
      else{
        h1Tag.style.fontSize = "4.5em";
      }  
    });  
  }
  else{  setStatusMessage("Data collection failed", "red")}//signal when, after getting metadata, the data received from car is null
})

ipc.on('stop', function(event,arg){ 
  setStatusMessage(arg, "limegreen")
  enableButton(startBtn)
  enableButton(csvBtn)  
  var delayInMilliseconds = 1500; //1 second
  setTimeout(function() {
    setStatusMessage("Disconnected from car", "red")  
  }, delayInMilliseconds);
})


