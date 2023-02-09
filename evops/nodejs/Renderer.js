const { app, BrowserWindow } = require('electron')
const ejse = require('ejs-electron')
const axios = require('axios')

function createWindow () {
 const win = new BrowserWindow({
 width: 800,
 height: 600,
 webPreferences: {
 nodeIntegration: true,
 }
 })
win.loadFile('frontend/views/index.ejs')
//win.webContents.openDevTools()
}
app.whenReady().then(createWindow)
app.on('window-all-closed', () => {
 if (process.platform !== 'darwin') {
 app.quit()
 }
})
app.on('activate', () => {
 if (BrowserWindow.getAllWindows().length === 0) {
 createWindow()
 }
})

test = 'Hello'
console.log('asdf')
async function makePostRequest(test) {
 axios.get('http://127.0.0.1:5000/test')
 .then(function (response) {
  console.log("It says: ", response.data);
 })
 .catch(function (error) {
  console.log(error);
 });
}
makePostRequest(test)

ejse.data('username', 'Some Guy')