// Modules to control application life and create native browser window
const {app, BrowserWindow, ipcMain, dialog} = require('electron')
const path = require('path')
const ipc = ipcMain
let {PythonShell} = require('python-shell')

let shell1 = new PythonShell('python_engine/getMetadata.py', {
    pythonOptions: ['-u']
}); //this shell variable declaration here is a game changer

let shell2 = new PythonShell('scrap_files_ignore/pseudoGetData.py', {
    pythonOptions: ['-u'], 
    mode: 'json'
}); //this shell variable declaration here is a game changer

function createWindow () {
  // Create the browser window.
  console.log("HELLO FROM MAIN.JS");
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

//IPC TUTORIAL

// ipcMain.on('open-error-dialog', function(event){
//   // dialog.showErrorBox('An error message', 'body of error msg')
//   // shell.send('hello')
//   shell.send("HEELLLOO")
//   console.log("sent msg from main.js")
// })



// PythonShell.run('engine/main.py', optionsConnect, function (err,results) {
// if (err) throw err;
// console.log(results[0]);
// connection = results;
// console.log('finished connection');
// });

// shell.on('message', function(message){
//     console.log("\n")
//     console.log('message', message.length)
//     console.log("\n");
//     console.log("finished")

// })

// while (c < 3){
//   PythonShell.run('test.py', optionsDataCollect, function (err,results) {
//   if (err) throw err;
//   console.log(results);
//   console.log('finished data collection');
// });
//   c = c+1;
// }


// var pyshell = new PythonShell('test.py');

// pyshell.send(JSON.stringify([1,2,3,4,5]));


// pyshell.on('message', function (message) {
//     console.log(message);
// });
// pyshell.end(function (err) {
//     if (err){
//         throw err;
//     };

//     console.log('finished');
// });


/////////////////////////////////////////////////////



// shell2.end(function (err) {
//     if (err){
//         throw err;
//     };

//     console.log('finished');
// });


// shell2.send(JSON.stringify([1,2,3,4,60]));

// shell2.end(function (err) {
//     if (err){
//         throw err;
//     };

//     console.log('finished');
// });
////////////////////////////////////////////

// shell1.on('message', function (message) {
//     console.log(message);
// });

// ipcMain.on('getMetadata', function(event){
//   shell2.send("1");

//   shell2.on('message', function (message) {
//       console.log(message);
//   });

//   console.log("sent msg from main.js")
// })

// ipcMain.on('getMetadata', function(event){
//   PythonShell.run('linkers/getMetadata.py', optionsConnect, function (err, results) {
//     if (err) throw err;
//     event.sender.send('getMetadata', results[0])
//   }); 
// })




// ipcMain.on('start', function(event){
//   shell2.on('message', function (message) {
//       console.log(message);
//       event.sender.send('start', message)
//   }); 
// })

// ipcMain.on('u', function(event){
//   PythonShell.run('python_engine/getMetadata.py', optionsConnect, function (err, results) {
//     if (err) throw err;
//     event.sender.send('getMetadata', results[0])
//     resolve()
//   }); 
// })       

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
          PythonShell.run('scrap_files_ignore/pseudoGetMetaData.py', optionsConnect, function (err, results) {
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
          shell2.on('message', function (message) {
            console.log("now returning message from thescript")
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
          shell2.send("end data collection and export to csv!")  
          event.sender.send('stop', "Exported successfully as a CSV")
          resolve()
        })      
    })
}

function endScript() {
    return new Promise((resolve, reject)=>{
      shell2.end(function (err) {
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
