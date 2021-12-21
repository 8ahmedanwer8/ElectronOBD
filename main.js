// Modules to control application life and create native browser window
const {app, BrowserWindow, ipcMain, dialog} = require('electron')
const path = require('path')
const ipc = ipcMain
let {PythonShell} = require('python-shell')

// let shell1 = new PythonShell('python_engine/getMetadata.py', {
//     pythonOptions: ['-u']
// }); 

let shell1 = new PythonShell('python_engine/getData.py', {
    pythonOptions: ['-u'], 
    mode: 'json'
}); //this shell variable declaration here is a game changer

function createWindow () {
  // Create the browser window.
  console.log("HELLO ELECTRONOBD USER. Data received from python (sensor units, description and values) will be printed here as well as in the client side.");
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true,
    }
  })

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')


  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.






var optionsConnect = {
  mode: 'json'
};


// ipcMain.on('getMetadata', function(event){
//   shell2.on('message', function (message) {
//     console.log("Got the click")
//     console.log(message);
//     event.sender.send('getMetadata', message)
//   });  
// })

function getMetaData() {
    return new Promise((resolve, reject)=>{
        ipcMain.on('getMetadata', function(event){
          PythonShell.run('python_engine/getMetadata.py', optionsConnect, function (err, results) {
            if (err) throw err;
            console.log(results)
            event.sender.send('getMetadata', results[0])
            resolve()
          }); 
        })      
    })
}

function getData() {
    return new Promise((resolve, reject)=>{
        ipcMain.on('start', function(event){
          console.log("got the click to start the script")
          shell1.on('message', function (message) {
            console.log("now returning message from the script")
            console.log(message);
            // ipcMain.send('start', message)
            event.sender.send('start', message)
            resolve(message)
          });  
        })         
    })
}

;(async function runFunctions() {
    await getMetaData();
    
    await getData();
})()

function exportCSV() {
    return new Promise((resolve, reject)=>{
        ipcMain.on('stop', function(event){
          shell1.send("end data collection and export to csv!")  
          event.sender.send('stop', "Exported successfully as a CSV")
          resolve()
        })      
    })
}

function endScript() {
    return new Promise((resolve, reject)=>{
      shell1.end(function (err) {
          console.log("finished data collection. disconnected from car, probably.")
      });  
      resolve('finished')   
    })
}

;(async function runFunctions() {
    await exportCSV();
    await endScript();
})()

// ipcMain.on('stop', function(event){
//   shell2.send("end data collection and export to csv")  
//   event.sender.send('stop', "Exported successfully as a CSV")
//   shell2.end(function (err) {
//       if (err){
//           throw err;
//       };

//       console.log('finished');
//   });  
// });  
